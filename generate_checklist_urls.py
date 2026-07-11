#!/usr/bin/env python3
"""Generate curriculum checklist download URLs for all 78 undergraduate programs."""

import json
import urllib.parse
from pathlib import Path

JSON_PATH = Path(__file__).parent / "undergraduate_programs.json"
OUTPUT_TXT = Path(__file__).parent / "checklist_urls.txt"
OUTPUT_SH = Path(__file__).parent / "download_checklists.sh"

# College name (from JSON) -> unit code for URL
UNIT_CODES = {
    "COLLEGE OF ARCHITECTURE": "CA",
    "COLLEGE OF ARTS AND LETTERS": "CAL",
    "ASIAN INSTITUTE OF TOURISM": "AIT",
    "CESAR E.A. VIRATA SCHOOL OF BUSINESS": "VSB",
    "SCHOOL OF ECONOMICS": "SE",
    "COLLEGE OF EDUCATION": "EDUC",
    "COLLEGE OF ENGINEERING": "COE",
    "COLLEGE OF FINE ARTS": "CFA",
    "COLLEGE OF HOME ECONOMICS": "CHE",
    "COLLEGE OF HUMAN KINETICS": "CHK",
    "COLLEGE OF LAW": "LAW",
    "SCHOOL OF LIBRARY AND INFORMATION STUDIES": "SLIS",
    "COLLEGE OF MASS COMMUNICATION": "CMC",
    "COLLEGE OF MUSIC": "CM",
    "NATIONAL COLLEGE OF PUBLIC ADMINISTRATION AND": "NCPAG",
    "GOVERNANCE": "NCPAG",
    "COLLEGE OF SCIENCE": "CS",
    "COLLEGE OF SOCIAL SCIENCES AND PHILOSOPHY": "CSSP",
    "COLLEGE OF SOCIAL WORK AND COMMUNITY DEVELOPMENT": "CSWCD",
    "SCHOOL OF STATISTICS": "STAT",
    "UP DILIMAN EXTENSION PROGRAM IN PAMPANGA": "UPDEPP",
}

# Website program name -> override unit code (for UPDEPPO duplicates)
UNIT_OVERRIDES = {
    "Business Economics (UPDEPPO)": "UPDEPP",
    "Applied Psychology (UPDEPPO)": "UPDEPP",
    "Business Management (UPDEPPO)": "UPDEPP",
}

# Program name fixes for URL compatibility
def fix_program_name(name):
    """Fix known typos/formatting issues in ACADEMIC PROGRAMS.md names."""
    fixes = {
        "andCommunications": "and Communications",
        " in  ": " in ",
        "Instiution": "Institution",
    }
    for old, new in fixes.items():
        name = name.replace(old, new)
    return name


def generate_urls():
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)

    base = "https://our.upd.edu.ph/files/Checklist/UG"
    urls = []

    for prog in data["programs"]:
        website_name = prog["website_name"]
        college = prog["college"]
        full_name = prog["full_program_name"]

        # Determine unit code
        unit = UNIT_OVERRIDES.get(website_name, UNIT_CODES.get(college))
        if not unit:
            print(f"WARNING: No unit code for college '{college}' ({website_name})")
            continue

        # Fix program name
        clean_name = fix_program_name(full_name)

        # Build URL
        encoded = urllib.parse.quote(clean_name, safe="")
        url = f"{base}/{unit}/{unit}_{encoded}.pdf"
        urls.append((website_name, url))

    return urls


def main():
    urls = generate_urls()

    # Write plain text URL list (one per line, for curl -K or xargs)
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        for _, url in urls:
            f.write(url + "\n")

    # Write shell script for batch download
    with open(OUTPUT_SH, "w", encoding="utf-8") as f:
        f.write("#!/bin/bash\n")
        f.write("# Download all UP Diliman undergraduate curriculum checklists\n")
        f.write(f"# Generated from {len(urls)} programs\n\n")
        f.write("mkdir -p checklists\n")
        f.write("cd checklists || exit 1\n\n")
        for name, url in urls:
            # Sanitize filename
            safe_name = name.replace("/", "-").replace(" ", "_")
            f.write(f"# {name}\n")
            f.write(f'curl -fSL -o "{safe_name}.pdf" "{url}" || echo "FAILED: {name}"\n')
            f.write("\n")

    print(f"Generated {len(urls)} URLs")
    print(f"  {OUTPUT_TXT}  - plain URL list (one per line)")
    print(f"  {OUTPUT_SH}    - shell script for batch download")
    print()

    # Show first 5 and last 5
    for name, url in urls[:5]:
        print(f"  {name}")
        print(f"    {url}")
    print("  ...")
    for name, url in urls[-3:]:
        print(f"  {name}")
        print(f"    {url}")


if __name__ == "__main__":
    main()
