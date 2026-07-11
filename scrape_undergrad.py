#!/usr/bin/env python3
"""Scrape UP Diliman undergraduate programs from website and map to colleges."""

import requests
import re
import json
import sys
from pathlib import Path

WEBSITE_URL = "https://upd.edu.ph/academics/undergraduate/"
ACADEMIC_PROGRAMS_PATH = Path(__file__).parent / "ACADEMIC PROGRAMS.md"
OUTPUT_PATH = Path(__file__).parent / "undergraduate_programs.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


def fetch_page_html(url):
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.text


def parse_website_programs(html):
    """Extract program entries from the WordPress page HTML.

    Structure:
      <div class="entry-content">
        <p><strong>A</strong></p>
        <p><a href="...">Program</a><br>... (optional specializations)</p>
        ...
        <p>Last Updated: ...</p>
      </div>
    """
    # Find the entry-content div using string positions
    start_marker = '<div class="entry-content">'
    idx = html.find(start_marker)
    if idx < 0:
        raise ValueError("Could not find entry-content div")
    inner_start = idx + len(start_marker)

    # Find the </div> that closes it (after "Last Updated")
    lu = html.find("Last Updated", inner_start)
    if lu < 0:
        raise ValueError("Could not find 'Last Updated' marker")
    end = html.find("</div>", lu)
    if end < 0:
        raise ValueError("Could not find closing </div>")
    content = html[inner_start:end]

    # Find all letter sections: <strong>LETTER</strong> followed by content
    # The content is in the same or next <p> tag
    # Pattern: <strong>A</strong>...content until next <strong> or end
    sections = re.split(r"<strong>\s*([A-Z])\s*</strong>", content)
    programs = []

    # After splitting, indices: [preamble, letter1, content1, letter2, content2, ...]
    for i in range(1, len(sections) - 1, 2):
        letter = sections[i].strip()
        section_content = sections[i + 1]

        # Find all <a href="URL">NAME</a> in this section
        for m in re.finditer(
            r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"[^>]*>(.*?)</a>',
            section_content, re.DOTALL
        ):
            url = m.group(1).strip()
            name_html = m.group(2)
            # Strip any nested HTML tags from name
            name = re.sub(r"<[^>]+>", "", name_html).strip()
            if not name:
                continue

            # Check for specialization text after this </a>
            # Specializations appear as "(Art History, Interdisciplinary, Philippine Art)"
            rest = section_content[m.end():]
            specs_match = re.match(r"\s*\(([^)]*)\)", rest)
            specializations = None
            if specs_match:
                specs_text = specs_match.group(1)
                specializations = [
                    s.strip() for s in specs_text.split(",") if s.strip()
                ]

            programs.append({
                "name": name,
                "url": url,
                "alphabetical_section": letter,
                "specializations": specializations,
            })

    return programs


def parse_academic_programs_md(path):
    """Parse ACADEMIC PROGRAMS.md into a hierarchical tree.

    Returns list of colleges, each with departments and their programs.
    """
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    colleges = []
    current_college = None
    current_department = None

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Skip preamble lines before first college
        if not colleges and not re.match(
            r"^(?:COLLEGE|SCHOOL|INSTITUTE|ASIAN|CESAR|NATIONAL|TECHNOLOGY|ARCHAEOLOGICAL|UP DILIMAN)",
            stripped,
        ):
            continue

        # College/unit header: all caps (but not department numbering)
        if not re.match(r"^\(\d+\)", stripped) and re.match(
            r"^[A-Z][A-Z\s&,'\.-]{3,}$", stripped
        ):
            current_college = {
                "college": stripped,
                "departments": [],
            }
            colleges.append(current_college)
            current_department = None
            continue

        # Department: numbered like (1), (2), etc.
        dept_match = re.match(r"^\(\d+\)\s+(.+)$", stripped)
        if dept_match:
            current_department = {
                "department": dept_match.group(1),
                "programs": [],
            }
            if current_college:
                current_college["departments"].append(current_department)
            continue

        # Footnote lines (start with *)
        if stripped.startswith("*"):
            continue

        # Program line
        if re.match(
            r"^(?:Bachelor|Doctor|Master|Diploma|Certificate|Juris|Professional|Sertipiko)",
            stripped,
        ):
            program_name = re.sub(r"[ab*]$", "", stripped.strip())
            if not re.match(
                r"^(?:Bachelor|Doctor|Master|Diploma|Certificate|Juris|Professional|Sertipiko)",
                program_name,
            ):
                continue
            is_undergrad = (
                program_name.startswith("Bachelor")
                or program_name.startswith("Juris")
                or program_name.startswith("Certificate")
                or program_name.startswith("Diploma")
            )
            program_entry = {
                "name": program_name,
                "level": "undergraduate" if is_undergrad else "graduate",
            }
            if current_department:
                current_department["programs"].append(program_entry)
            elif current_college:
                if "direct_programs" not in current_college:
                    current_college["direct_programs"] = []
                current_college["direct_programs"].append(program_entry)
            continue

    return colleges


def extract_core_name(website_name):
    """Extract the core program name for matching."""
    name = website_name.strip()
    name = re.sub(r"\s*\(UPDEPPO\)", "", name, flags=re.IGNORECASE)
    # Handle "English Studies: Language" -> "english studies language"
    name = name.replace(":", " ")
    # Handle "Malikhaing Pagsulat" (matches "Malikhaing Pagsulat sa Filipino")
    return name


def _program_priority(prog_name):
    """Return priority score: Bachelor (higher) > others."""
    if prog_name.lower().startswith("bachelor"):
        return 2
    if prog_name.lower().startswith(("certificate", "diploma")):
        return 1
    return 0


def build_program_lookup(colleges):
    """Build a flat lookup from core program keywords to college/department.

    Returns dict: {keyword: (college_name, department_name_or_None, full_program_name)}
    Bachelor programs take priority over Certificate/Diploma for the same keyword.
    """
    lookup = {}

    for college in colleges:
        depts = college.get("departments", [])
        for prog in college.get("direct_programs", []):
            if prog["level"] not in ("undergraduate",):
                continue
            keywords = [k for k in generate_keywords(prog["name"]) if k]
            priority = _program_priority(prog["name"])
            for kw in keywords:
                if kw not in lookup or priority > _program_priority(lookup[kw][2]):
                    lookup[kw] = (college["college"], None, prog["name"])

        for dept in depts:
            for prog in dept.get("programs", []):
                if prog["level"] not in ("undergraduate",):
                    continue
                keywords = [k for k in generate_keywords(prog["name"]) if k]
                priority = _program_priority(prog["name"])
                for kw in keywords:
                    if kw not in lookup or priority > _program_priority(lookup[kw][2]):
                        lookup[kw] = (college["college"], dept["department"], prog["name"])

    return lookup


def generate_keywords(full_program_name):
    """Generate matchable keywords from a full program name.

    E.g. 'Bachelor of Arts (Anthropology)' -> ['anthropology']
         'Juris Doctor' -> ['juris doctor']
    """
    kw = full_program_name.lower().strip()
    # Remove trailing footnote markers
    kw = re.sub(r"[ab*]\s*$", "", kw)

    # Handle Juris Doctor before stripping
    if kw == "juris doctor":
        return ["juris doctor"]

    # Known degree qualifiers
    degree_qualifiers = (
        r"arts|science|fine arts|music|physical education|sports science|"
        r"elementary education|secondary education|landscape architecture|"
        r"public administration|library and information science"
    )

    # Strip common prefixes: "Bachelor of X in/()", "Certificate in X", "Diploma in X"
    prefixes = (
        rf"^(?:bachelor of (?:{degree_qualifiers})\s*(?:in\s+|major in\s+)?|"
        r"certificate in\s+|diploma in\s+)"
    )
    m = re.match(f"{prefixes}(.+)", kw)
    if m:
        kw = m.group(1)
    else:
        # "Bachelor of <qualifier>" (standalone program)
        m = re.match(rf"^bachelor of ({degree_qualifiers})\s*$", kw)
        if m:
            kw = m.group(1)
        else:
            # "Bachelor of Arts-Master of Arts Honors (...)"
            m = re.match(r"^bachelor of arts-master of arts honors\s*(.+)", kw)
            if m:
                kw = m.group(1)
            else:
                # Generic fallback
                kw = re.sub(
                    r"^(?:bachelor of \w+(?:\s+\w+){0,3}|certificate in\s+|diploma in\s+)\s*"
                    r"(?:in\s+)?",
                    "", kw,
                )

    kw = kw.strip()

    # Remove parentheses but keep content
    kw_clean = re.sub(r"[()]", "", kw).strip()
    keywords = []

    if kw_clean:
        keywords.append(kw_clean)

    # Variant without parenthetical content
    kw_no_paren = re.sub(r"\s*\([^)]*\)", "", kw).strip()
    if kw_no_paren and kw_no_paren not in keywords:
        keywords.append(kw_no_paren)

    # "and" vs "&" variants
    for k in list(keywords):
        if " and " in k:
            keywords.append(k.replace(" and ", " & "))

    # Colon variants: "English Studies: Language" -> "english studies language"
    for k in list(keywords):
        if ":" in k:
            keywords.append(k.replace(":", " ").replace("  ", " ").strip())

    return keywords


def fuzzy_match(website_name, lookup):
    """Match a website program name to the closest entry in the lookup."""
    core = extract_core_name(website_name).lower().strip()
    if not core:
        return None

    # Known alternate names (website name -> lookup key)
    KNOWN_ALIASES = {
        "library and information studies": "library and information science",
    }
    if core in KNOWN_ALIASES and KNOWN_ALIASES[core] in lookup:
        return KNOWN_ALIASES[core]

    if core in lookup:
        return core

    # Try substring containment - prefer matches where core appears near the start
    candidates = []
    for lookup_kw in lookup:
        if not lookup_kw:
            continue
        if core in lookup_kw:
            pos = lookup_kw.index(core)
            candidates.append((pos, len(lookup_kw), lookup_kw))
        elif lookup_kw in core:
            candidates.append((0, len(lookup_kw), lookup_kw))
    if candidates:
        candidates.sort()
        return candidates[0][2]

    # Word-level prefix matching (handles "sport" vs "sports", "institution" vs "institutional")
    stopwords = {"in", "of", "and", "the", "a", "an", "for", "on", ","}
    core_words = [w for w in core.split() if w not in stopwords]

    if core_words:
        for lookup_kw in lookup:
            if not lookup_kw:
                continue
            kw_words = [w for w in lookup_kw.split() if w not in stopwords]
            if len(core_words) != len(kw_words):
                continue
            all_match = True
            for cw, kw_word in zip(core_words, kw_words):
                if cw == kw_word:
                    continue
                if len(cw) >= 4 and len(kw_word) >= 4 and (
                    cw.startswith(kw_word) or kw_word.startswith(cw)
                ):
                    continue
                all_match = False
                break
            if all_match:
                return lookup_kw

    # Subset of words (all core words appear as prefixes in kw words)
    for lookup_kw in lookup:
        if not lookup_kw:
            continue
        kw_words = [w for w in lookup_kw.split() if w not in stopwords]
        if not core_words or not kw_words:
            continue
        matched = 0
        for cw in core_words:
            for kw_word in kw_words:
                if cw == kw_word or (
                    len(cw) >= 4 and len(kw_word) >= 4
                    and (cw.startswith(kw_word) or kw_word.startswith(cw))
                ):
                    matched += 1
                    break
        if matched == len(core_words) and len(kw_words) <= len(core_words) + 1:
            return lookup_kw

    return None


def main():
    print(f"Fetching {WEBSITE_URL} ...")
    html = fetch_page_html(WEBSITE_URL)
    website_programs = parse_website_programs(html)
    print(f"Found {len(website_programs)} programs on website")

    print(f"Parsing {ACADEMIC_PROGRAMS_PATH} ...")
    colleges = parse_academic_programs_md(ACADEMIC_PROGRAMS_PATH)

    dept_count = sum(len(c.get("departments", [])) for c in colleges)
    print(f"Parsed {len(colleges)} colleges with {dept_count} departments")

    lookup = build_program_lookup(colleges)
    print(f"Built lookup with {len(lookup)} keyword entries")

    # Match and build output
    output = []
    matched = 0
    unmatched = []

    for wp in website_programs:
        kw = fuzzy_match(wp["name"], lookup)
        entry = {
            "website_name": wp["name"],
            "website_url": wp["url"],
            "section": wp["alphabetical_section"],
        }
        if wp["specializations"]:
            entry["specializations"] = wp["specializations"]

        if kw:
            college, dept, full_name = lookup[kw]
            entry["college"] = college
            if dept:
                entry["department"] = dept
            entry["full_program_name"] = full_name
            matched += 1
        else:
            unmatched.append(wp["name"])
            entry["college"] = None
            entry["department"] = None
            entry["full_program_name"] = None

        output.append(entry)

    # Write output
    result = {
        "source_url": WEBSITE_URL,
        "total_programs": len(website_programs),
        "matched": matched,
        "unmatched": len(unmatched),
        "programs": output,
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {OUTPUT_PATH}")
    print(f"Matched: {matched}/{len(website_programs)}")
    if unmatched:
        print(f"\nUnmatched programs ({len(unmatched)}):")
        for name in unmatched:
            print(f"  - {name}")

    # Print summary
    colleges_found = {}
    for p in output:
        c = p.get("college", "UNKNOWN")
        colleges_found[c] = colleges_found.get(c, 0) + 1
    print(f"\nCollege distribution ({len(colleges_found)}):")
    for c, count in sorted(colleges_found.items(), key=lambda x: -x[1]):
        print(f"  {c}: {count}")


if __name__ == "__main__":
    main()
