---
title: "FINAL VERSION TEMPLATE (APacCHRIE 2026 Main Conference) MONTANO & TAPANG"
type: source
category: Research
date_ingested: 2026-07-11
status: draft
confidence: high
original: "[[/Users/ganni/Desktop/Media/M-binary/Research/ingested/curriculum-networks/papers/FINAL VERSION TEMPLATE (APacCHRIE 2026 Main Conference) MONTANO & TAPANG-R.docx]]"
source_url: ""
doi: ""
hash: da5cfa5685fa536e
---

Curriculum Network Analysis of Quantitative Bottlenecks in

Hospitality Management Education (Paper #445)

Larissa Mae Maranan-Montano

Department of Hotel, Restaurant and Institution Management & Data
Science Program

University of the Philippines Diliman

Giovanni A. Tapang

National Institute of Physics & Data Science Program

University of the Philippines Diliman

Abstract:

The study uses a dual-network analysis to evaluate student progression
in a rapidly growing BS in Hotel, Restaurant and Institution management
(BS HRIM) program. The program has expanded by 64% since 2024, yet the
2021 curricular revision has produced an on-time graduation rate of only
24%. To identify the systemic drivers of this delay, the curriculum is
modeled through two distinct lenses: a structural curriculum network
based on official prerequisites and an empirical progression network
derived from the records of N=269 students. Structural analysis reveals
a high-risk prerequisite chain centered on Math 21 and Stat 101, with
HRIM 131 functioning as the main structural chokepoint (betweenness
centrality = 0.3335). Louvain community detection confirms strong
structural partitioning (modularity Q = 0.674) that degrades sharply in
the empirical network (Q = 0.231), where failure and retake cycles blur
intended prerequisite tiers. Math 21 emerges as the dominant academic
bottleneck, with a 37.3% failure rate, 295 total attempts from 194
unique students, and a self-loop weight of 71, confirming mandatory
failure-driven retakes. The dominant empirical hub by degree is PE 2, a
structural artifact of its four-time enrollment requirement. These
findings support targeted early intervention in quantitative courses and
curriculum revisions that reduce reliance on a single prerequisite
chain. In this program, 76% of students did not graduate on time under
the revised curriculum, even though some may eventually complete it.

Keywords: hospitality education, curriculum network, curriculum
roadblocks

1. Introduction

The BS Hotel, Restaurant and Institution Management (BS HRIM) program
has seen a period of unprecedented growth. Between 2023 and 2025, new
cohorts have grown to represent over 60% of total enrollment, with
section counts escalating from a single section in 2021 to four sections
by 2025. However, this growth has collided with structural rigidities of
the 156-unit curriculum revised in 2021. Preliminary data from the
inaugural 2021 cohort reveal a concerning trend: only 24% graduated on
time. On-time graduation means completing all 156 required units within
eight regular semesters (four academic years), excluding midyear terms.
The remaining 76% have either withdrawn or faced significant delays.

The primary driver of delays is the prerequisite trap centered on core
quantitative and professional courses. The progression into the HRIM 150
series (culinary, beverage, managerial control, management information
systems, human resource, and marketing), a critical fifth-semester block
that must be taken in its entirety, requires successful completion of
HRIM 131 (operations management). HRIM 131 requires Math 21 (elementary
analytics) and Stat 101 (elementary statistics). High failure rates in
these foundational subjects have created a massive backlog. The
department has offered HRIM 131 every semester since 2022 to accommodate
students delayed from one to five semesters.

This off-season scheduling places an unsustainable strain on limited
faculty and classroom resources. With the population nearly quadrupling
in four years, the department faces a dual crisis: maintaining academic
rigor while ensuring student flow through a curriculum that currently
lacks the flexibility to absorb failure or delay. There is an urgent
need to shift from anecdotal observations to data-driven modeling to
understand how these prerequisite chains impact student momentum.

Research Objectives

This study seeks to provide a quantitative framework for curriculum
management by pursuing the following objectives:

1.  Map the BS HRIM curriculum as an empirical progression network to
    visualize student flow.

2.  Identify specific bottleneck nodes that disproportionately hinder
    on-time graduation.

3.  Quantify the impact of failure rates on institutional resources and
    student progress.

2. Literature Review

2.1. Structural Complexity and Curricular Analytics

Network analysis is widely used across fields to study complex systems
by modeling entities as nodes and their relationships as links (Roxas &
Tapang, 2010). Modern curricular assessment has shifted from subjective
evaluation to curricular analytics, which models degree programs as
directed-curriculum networks. Within this framework, courses are treated
as nodes and prerequisites as directed edges. Aldrich (2015) provided an
early formal treatment by modeling the undergraduate curriculum at
Benedictine University as a Course Prerequisite Network (CPN), revealing
hidden community clusters, bridges, and hub courses not apparent from
the catalogue alone. Structural complexity in CPNs is defined by three
key metrics: the blocking factor (courses blocked by a single failure),
the delay factor (the longest prerequisite chain through a course), and
centrality (Heileman et al., 2019; Slim et al., 2014). High structural
complexity often correlates with higher failure rates and elongated
time-to-degree, particularly in professional programs where foundational
quantitative sequences act as gatekeepers with high blocking factors.

Yang et al. (2024) provide the most comprehensive peer-reviewed CPN
application across public universities. They formally define the CPN as
G = (V, E) and apply centrality measures—betweenness centrality,
out-degree, reach, and transpose PageRank—to the CPNs of six American
institutions. Their reach (v) metric quantifies the total downstream
courses for which course v is a direct or indirect prerequisite. Their
findings confirm that mathematics courses achieve the highest
betweenness centrality and reach values across all institutions studied,
establishing mathematics prerequisites as a structural feature of
STEM-adjacent curricula rather than an institutional anomaly. Yang et
al. further introduce the Longest Paths Induced sub-Graph (LPIG), the
subgraph containing all courses on prerequisite chains of length ≥ k, as
a formal construct for identifying the most highly constrained degree
pathways.

Zuev & Stavrinides (2025) introduce three global CPN measures—breadth
(B), depth (D), and flux (Φ)—grounded in topological stratification,
enabling whole-curriculum diagnosis beyond node-level properties.
Basavaraj et al (2022) combined Sankey visualizations with network
science curricular analytics to map degree mobility patterns, finding
that foundational course performance is the primary driver of
differences in progression across cohorts. This body of work establishes
that the network-analytic approach is not merely descriptive but
diagnostic: the structural position of a course in the CPN predicts its
real-world impact on student progression and time-to-degree.

2.2. Learning Analytics and Student Progression

Learning analytics (LA) measures and reports data on learners and their
contexts to understand and optimize learning and the environments in
which it occurs (Conijn et al., 2017). Rienties & Toetenel (2016)
studied 151 modules and 111,256 students at the Open University UK,
finding that the structural design of a course strongly predicts student
engagement, retention, and satisfaction. This parallels the rationale
for applying network-level curriculum metrics: both approaches treat
program structure as a tractable, data-measurable driver of student
outcomes rather than as a fixed condition.

Predictive modeling has extended this to identifying at-risk
individuals. Conjin et al (2017) compared 17 blended courses at
Eindhoven University of Technology (TU/e) and demonstrated that LMS
engagement data can accurately predict final course grades, enabling
intervention before failure becomes irreversible. For structured
prerequisite programs like BS HRIM, this has significant implications:
early engagement predicts course-level outcomes, and course-level
outcomes in prerequisite-gating courses predict degree-level
trajectories. Identifying bottleneck courses through network analysis is
a critical first step in at-risk identification pipelines.

In the Philippine higher education context, these issues carry urgency.
The Commission on Higher Education (CHED) updates its Policies,
Standards, and Guidelines (PSGs) on average every 11 years (EDCOM 2,
2026). Structural curricular problems identified today may persist for
nearly a decade before the next revision window. This institutional
inertia makes data-driven, within-cycle evidence especially valuable.
Curriculum network analysis provides precisely this type of evidence,
allowing programs to optimize student outcomes without waiting for a
full curriculum overhaul.

2.3. The Hospitality Curriculum

Quantitative subjects such as calculus and statistics have long been
integrated into hospitality curricula, and leading US hospitality
programs typically require at least a semester of business statistics
and one analytics-oriented course (Cullen & Lambert, 1987). More
recently, Fei et al. (2025) highlight modules on revenue management,
demand forecasting, and data-driven pricing as standard quantitative
components in contemporary hospitality degrees.

Regional comparisons of hospitality programs in Asia reveal that
curricula frequently struggle to balance business-theoretical
foundations with specialized practical training (Wang & Abukhalifeh,
2021). Future curricular revisions should prioritize immersive
industry-based learning, hospitality-specific technologies such as CRM
systems and online reservation platforms, and big data and analytics,
rather than dwelling on calculus and statistics (Fei et al., 2025).

Notably, the ASEAN Common Competency Standards for Tourism Professionals
(ACCSTP) and the Common ASEAN Tourism Curriculum (CATC) do not list
quantitative analytics, statistics, or calculus as explicit competency
domains. The heavy quantitative prerequisite chain in the BS HRIM
curriculum (Math 20 → Math 21 → Stat 101 → HRIM 131) is therefore a
feature of CHED’s academic degree framework, not a requirement of the
ACCSTP vocational competency standards. This structural tension between
academic gating logic and the industry-facing competency framework
governing regional workforce mobility is a key contextual factor in the
present analysis.

2.4. Research Gap

Curriculum network analysis literature is growing, but applications to
hospitality management programs remain absent. Existing CPN studies have
focused on STEM, computing, and general undergraduate programs at North
American and European institutions (Aldrich, 2015; Yang et al., 2024).
The structural dynamics of professional service-sector curricula—which
combine quantitative requirements with practicum-heavy experiential
sequences—remain unexamined.

The complexity of Philippine hospitality programs is intensified by the
intersection of CHED’s PSG framework and AUN-QA (ASEAN University
Network Quality Assurance) accreditation standards. Under the pressure
of rapid post-pandemic enrolment growth, the BS HRIM program has seen
structural prerequisite bottlenecks compound across large student
cohorts. This study addresses this gap by pioneering a dual-network
curriculum analysis—a method that synthesizes formal structural
blueprints with empirical student flow. This represents the first
application of network-analytic bottleneck assessment within a
hospitality management curriculum in the ASEAN region.

3. Methodology

This study employs a dual-network analysis approach to evaluate the BS
HRIM program. Both networks share the same node set of courses. However,
they encode different edge types. The structural network uses
prerequisites from the official curriculum. The empirical network uses
observed student transitions from individual curriculum checklists from
enrollment records. We developed two distinct models. The Structural
Curriculum Network maps the program’s theoretical design. The Empirical
Progression Network analyzes the actual movement of N = 269 students.

3.1. Structural Curriculum Network

The initial phase involved modeling the formal 156-unit BS HRIM
curriculum as a directed graph to quantify its inherent complexity.
Following Yang et al. (2024), the curriculum is formally encoded as CPN
G = (V, E). Graph-theoretic centrality measures identify courses of
structural importance, including betweenness centrality and node reach.
Following Zuev & Stravrinides (2025), a transitive reduction was applied
to remove any edge i → k where a longer directed path i → … → k already
exists, ensuring that computed centrality values reflect only essential
prerequisite structure.

Nodes represent each unique subject in the 156-unit program. Directed
edges link prerequisite subjects to their subsequent target courses.
Prerequisite edges were assigned weight w = 2, reflecting a hard
sequential dependency where failure fully blocks access. Corequisite
edges were assigned w = 1, reflecting softer coupling, allowing
concurrent enrollment. To assess sensitivity, all centrality measures
reported in §4.1 were recomputed under uniform weighting (w = 1 for all
edges). The top-five betweenness and reach rankings were unchanged,
confirming that structural bottleneck identification is robust to the
weighting scheme (see Table 1).

Corequisites are treated as unidirectional edges from the first-offered
term to the co-offered course. Retake loops in the empirical flow are
represented as parallel paths rather than back-edges. This preserves the
acyclicity of the directed curriculum network.

3.2. Empirical Progression Network

The second phase modeled students’ actual academic histories to identify
deviations from the theoretical blueprint. We extracted and anonymized
the curriculum checklists of N = 269 students currently enrolled under
the 2021 curriculum (covering the 2021–2026 cohorts). Unlike the static
structural network, this model maps the subjects students actually took
sequentially, including retakes and off-season enrollments. Each node
was enriched with performance data, including total attempts, failure
rate (f), and counts of incomplete (INC) or dropped (DRP) attempts.
Edges were weighted by transition frequency—the volume of student flow
between subjects across all recorded semesters.

This phase follows the analytical pipeline established by Basavaraj et
al. (2022), who extracted term-by-term institutional enrolment records
for student cohorts and overlaid them on a curricular network
representation to identify which courses generated the greatest
disruptions in student degree mobility. Their approach of coupling
historical student-flow data with network analysis to provide
recommendations to improve student outcomes (Basavaraj et al., 2022)
directly informs the construction of the empirical progression network
in the present study.

Both networks were constructed and analyzed using the Python NetworkX
library (Hagberg et al., 2008). The structural network was rendered
using a hierarchical layout ordered by topological level—entry-point
courses with no prerequisites at the top, deeper prerequisite levels
descending—to make prerequisite flow visually explicit. The empirical
network was rendered using the ForceAtlas2 force-directed algorithm
(Jacomy et al., 2014), which positions high-degree hub nodes centrally
and clusters tightly-connected courses together.

This approach follows Yang et al. (2024), who similarly employed Gephi
alongside NetworkX to compute and visualize betweenness centrality
distributions and modularity-based clustering. Community detection was
performed using the Louvain algorithm (Blondel et al., 2008), and
modularity scores (Newman & Girvan, 2004) were computed for both
networks.

The structural integrity and friction of the program were evaluated by
comparing the two networks through three primary lenses: in-degree and
out-degree distributions, to identify gateway and bottleneck courses
where student flow stalls; transition density, to quantify the velocity
of student movement through high-stakes blocks like the HRIM 150 series;
and path deviation, comparing theoretical network diameter against the
actual multi-attempt paths taken by students to identify systemic
delays.

4. Results

4.1. Structural Curriculum Network Analysis

The visualization reveals a highly centralized network architecture with
a clear prerequisite backbone. The following are the key structural
features of the curriculum.

4.1.1. High-risk Prerequisite Chain

In Figure 1, the red cluster constitutes the highest-risk prerequisite
sequence in the structural network. This path starts with Math 20, a
non-credit bridging course that is a prerequisite for Math 21. Stat 101
and Math 21 are prerequisites for HRIM 131, which is the gateway to the
HRIM 150 series. Failure at any node in this sequence blocks all
downstream progression. Program advisers encourage students to attempt
Math 21 and Stat 101 during their first year to minimize cumulative
delay.

Figure 1.

Structural Curriculum Network of the BS HRIM Program (156 units)

[]

Note. Nodes represent individual courses; directed edges point from
prerequisite to dependent course. Node color encodes Louvain community
membership (modularity Q = 0.674; red = quantitative chain community,
purple = HRIM foundational cluster, gray = general education (GE) and
other clusters). Node size is proportional to out-degree. Key bottleneck
courses (Math 21, Stat 101, HRIM 120, HRIM 131) are labeled in the
figure.

4.1.2. Structural Asymmetry

The early clusters are broad but shallow; the later clusters are deep
with many successive prerequisites. In the framework of Zuev &
Stavrinides (2025), this asymmetry is formally captured by topological
stratification: the early strata S₁–S₂ are wide (high breadth, many
courses per stratum), while the later strata leading to HRIM 150 and
HRIM 160 series are narrow, producing a high-depth, low-breadth terminal
structure. A curriculum with this profile has a longest path relative to
its total node count—precisely the structural condition that Zuev &
Stavrinides identify as associated with constrained degree programs and
extended time-to-graduation. The “high-risk chain of survival”
corresponds to the long-path subgraph that would dominate the BS HRIM
LPIG, confirming the linear quantitative prerequisite chain as a
systemic architectural feature.

4.1.3. Community Structure

Louvain community detection yields nine communities at Q = 0.674, well
above the threshold for meaningful community structure of Q > 0.30;
(Newman & Girvan, 2004). The largest community (C1, 12 courses) groups
Math 20, Math 21, Stat 101, and HRIM 131 together with their downstream
senior electives, confirming this chain as a single structurally
cohesive unit. C2 (9 courses) captures the HRIM foundational cluster
anchored by HRIM 120, encompassing all seven courses unlocked by HRIM
120, along with its two prerequisite feeders (HRIM 110, HRIM 116).
Smaller communities correspond to the PE series, NSTP, and foreign
language elective pairs. The high modularity reinforces structural
asymmetry: the curriculum is a set of largely separate prerequisite
sub-chains converging at two chokepoints, HRIM 120 and HRIM 131, before
diverging again into the senior tier.

4.1.4. Structural Network Centrality Measures

Table 1 reports six graph-theoretic metrics for key curriculum nodes
(Yang et al., 2024; Zuev & Stavrinides, 2025), In-degree counts
prerequisites; out-degree counts courses directly unlocked; betweenness
centrality measures the proportion of shortest paths passing through a
node; reach quantifies the total downstream courses; delay factor
measures the longest prerequisite chain from a node; and blocking factor
counts courses immediately inaccessible upon failure. Reach values in
Table 1 count all downstream courses in the curriculum, including both
HRIM and non-HRIM subjects, which explains why HRIM 120’s reach (26)
exceeds Math 21’s reach (17).

Table 1.

Structural Centrality Measures— Key BS HRIM Curriculum Nodes

  ----------- -------- --------- ------------- ------- ---------- ---------
    Course     In-deg   Out-deg   Betweenness   Reach  Block. F.  Delay F.

   HRIM 131      3         6        0.0335       16        6          3

   HRIM 120      2         8        0.0182       26        8          4

   HRIM 150      1         2        0.0098        4        2          2

    Math 21      1         1        0.0059       17        1          4

   HRIM 199      1         1        0.0028        1        1          1

   Stat 101      0         1        0.0000       17        1          4

   HRIM 110      0         1        0.0000       27        1          5

   HRIM 116      0         1        0.0000       27        1          5

    Math 20      0         1        0.0000       18        1          5

   HRIM 186      1         0        0.0000        0        0          0
  ----------- -------- --------- ------------- ------- ---------- ---------

Note. Betweenness centrality is normalized. Reach = total downstream
courses unlocked (Yang et al., 2024). Blocking factor = number of
courses immediately inaccessible upon failure. Delay factor = length of
longest prerequisite chain from this node.

Three findings stand out from Table 1. First, HRIM 131 has the highest
betweenness centrality (BC = 0.0335). It is the sole gateway through
which all paths from foundational quantitative courses—Math 21, Stat
101, and HRIM 120—converge and fan out into HRIM 150 series, making it
the curriculum’s structural chokepoint. Second, HRIM 120 has the highest
out-degree and blocking factor (8), serving as the program’s primary
hub; a single failure can lock out eight courses simultaneously. Third,
Math 21’s betweenness is comparatively lower (BC = 0.0059), but its
reach of 17 and delay factor of 4 confirm disproportionate downstream
influence. Any student who fails Math 21 is indirectly blocked from 17
courses and faces a prerequisite chain four levels deep before program
completion.

4.2. Profile of Students for the Empirical Progression Network

The sample consists of 269 students. The distribution is skewed toward
new students: 34.6% are from the 2025–2026 cohort, and 29.4% are from
the 2024–2025 cohort (Table 2). The overall Weighted Average Grade (WAG)
is 1.81. Their general performance is shown in Table 3.

Table 2.

Cohort Distribution of the UP Diliman BS HRIM program

  -------------------------------- -------------- ----------------------
          Cohort (Started)             Count            % of Total

           1st Sem 21-22                 9                3.35%

           1st Sem 22-23                 42               15.61%

           1st Sem 23-24                 46               17.10%

           1st Sem 24-25                 79               29.37%

           1st Sem 25-26                 93               34.57%

               TOTAL                    269              100.00%
  -------------------------------- -------------- ----------------------

The program is growing. The two newest cohorts (2024–2025 and 2025–2026)
together make up 64% of enrolled students.

Table 3.

Performance by Cohort of the UP Diliman BS HRIM program

  -------------- ---- ----------- -------------------- -------- --------
      Cohort      n     Avg WAG    Avg Credited Units  w/ 5.00   w/ INC

  1st Sem 21-22   9      1.657           128.63           3        1

  1st Sem 22-23   42     1.796           122.22           5        12

  1st Sem 23-24   46     1.864           88.62            7        16

  1st Sem 24-25   79     1.815           61.84            7        14

  1st Sem 25-26   93     1.824           30.54            1        22
  -------------- ---- ----------- -------------------- -------- --------

The oldest cohort (21-22) has the best WAG (1.657) and is near
completion (Table 4). The high rate of 5.00 grades across middle cohorts
(59%) is primarily driven by Math 21.

Table 4.

  ------------------------------ ---------------- ---------------------
            WAG Range                 Count                 %

            1.00–1.25                   10                3.72%

            1.26–1.50                   48               17.84%

            1.51–1.75                   71               26.39%

            1.76–2.00                   62               23.05%

            2.01–2.25                   46               17.10%

            2.26–2.50                   22                8.18%

            2.51–2.75                   6                 2.23%

            2.76–3.00                   3                 1.12%

              3.01+                     1                 0.37%

              Total                    269               100.00%
  ------------------------------ ---------------- ---------------------

Academic Performance: WAG Range

About 72% of students have a WAG of 2.25 or better, indicating a solid
overall performance.

Table 5.

Academic Progress of students in the UP Diliman BS HRIM program—
Credited Units (Total: 156 units required)

  --------------------------------- -------------- ------------------
           Units Completed              Count              %

                0–29                      57             21.19%

                30–59                     71             26.39%

                60–89                     69             25.65%

               90–119                     36             13.38%

               120–156                    36             13.38%

                Total                    269            100.00%
  --------------------------------- -------------- ------------------

Table 5 shows 36 students (13.4%) are near or at completion (120+ units)
while 57 students (21.2%) are in their early stages (<30 units),
consistent with the large incoming cohort.

Table 6.

Course Completion Rates of the UP Diliman BS HRIM program. N = 269.

  ---------------------------------------- -------------- ------------
              Core HRIM Course               Satisfied         %

                  HRIM 110                      267          99.26%

                  HRIM 116                      256          95.17%

                  Stat 101                      203          75.46%

                  HRIM 120                      182          67.66%

                  Math 21                       171          63.57%

                   FS 105                       170          63.20%

                   HE 102                       164          60.97%

                   FN 102                       159          59.11%

                   HE 100                       157          58.36%

                  HRIM 132                      148          55.02%

                  HRIM 131                      138          51.30%

                   HE 101                       132          49.07%

                  HRIM 140                       87          32.34%

                  HRIM 144                       86          31.97%

                  HRIM 143                       84          31.23%

                  HRIM 142                       83          30.86%

            HRIM 150–156 (group)                 65          24.16%

                   PI 100                        59          21.93%

            HRIM 160–163 (group)                 35          13.01%

         HRIM 176–179, 200 (group)               25          9.29%
  ---------------------------------------- -------------- ------------

Almost all students have completed HRIM 110. Nearly 5% have yet to pass
HRIM 116, indicating an early bottleneck. More students have passed Stat
101 than Math 21. Low completion rates for upper-level courses (HRIM
150+) are expected, given the large incoming cohorts. These completion
rates are shown in Table 6.

4.3. Results of Network and Bottleneck Analysis

Table 7.

Network Overview of students taking the UP Diliman BS HRIM curriculum

  ---------------------------------------- ---------------------------
                   Metric                             Value

              Nodes (courses)                          56

                Total edges                           1,633

         Self-loop edges (retakes)                     12

       Non-self-loop transition edges                 1,621

             HRIM-prefix nodes                         27

              GE / other nodes                         29

    Only pure source node (no in-edges)               Eng 1

           Highest in-degree node               PE 2 (in = 1,541)

          Highest out-degree node              PE 2 (out = 1,679)

         Strongest convergence sink           HRIM 120 (in = 1,106)
  ---------------------------------------- ---------------------------

Table 7 presents the network parameters of student progression through
the curriculum network. With 269 students moving through the curriculum,
the high edge count shows that students are not following a linear path.
They are distributed across available courses, likely due to failing
prerequisites and course offerings. HRIM 120 serves as the primary
convergence sink, demonstrating its role as a high-friction gatekeeper.

Louvain community detection on the empirical network yields three
communities at Q = 0.231. While lower than the structural network’s Q =
0.674—which is expected given that students physically traverse all
tiers and create cross-community edges—the value remains above the Q >
0.10 threshold for detectable mesoscale structure (Newman & Girvan,
2004). The three communities correspond to curriculum tiers: Community 3
(red, n = 16) groups foundation and entry-level courses; Community 2
(blue, n = 20) captures the gateway and mid-tier courses including the
quantitative bottleneck (Math 21, Stat 101) and the HRIM 131 convergence
node; and Community 1 (green, n = 20) encompasses upper-division and
senior specialization courses. The lower modularity quantifies a key
finding: failing students recycle through foundation courses across
semesters, blurring the clean tier boundaries visible in the official
curriculum.

Figure 2.

Empirical Progression Network of BS HRIM Students (N = 269, 2021-2026
Cohorts)[]

Note. Nodes represent courses as actually enrolled in by students;
directed edges connect sequentially enrolled courses across semesters,
with only transitions of five or more student instances shown. Edge
thickness is proportional to transition frequency. Node color encodes
Louvain community membership (Q = 0.231). Node size proportional to
weighted in-degree. Red rings indicate a failure rate above 5%.
Self-loops on Math 21, Stat 101, and PE 2 indicate reenrollment.

The network is organized into three structural layers, as shown in
Figure 2. The color corresponds to these structural layers.

4.3.1. Layer 1: Foundational and General Education (Red)

These courses have a large out-degree relative to their in-degree,
serving as launch pads that propel students into many subsequent
courses. The dominant first-semester entries are HRIM 110 (268 attempts,
out-degree 1,069) and HRIM 116 (273 attempts, out-degree 1,022). Other
high-out-degree Layer 1 nodes include Arts 1 (out 1,012), Kas 1 (out
957), Philo 1 (out 907), and Speech 30 (out 904). Math 20 (115 attempts)
is a non-credit bridge course; all recorded grades are P/F, INC, or DRP.
Eng 1 is the only pure source node (in-degree = 0, out-degree = 7).

4.3.2. Layer 2: Quantitative Bottleneck (Blue)

Math 21 is the most consequential bottleneck node. It recorded 295
attempts from 194 unique students, a 37.3% failure rate, an average
grade of 3.56, and a self-loop weight of 71 with avg_grade_from = 4.94,
confirming that nearly all retakers had failed previously. Math 21 holds
the second-highest in-degree (1,181) and a very high out-degree (928).
It is simultaneously a major destination and a major source of
transitions.

Stat 101 shows a parallel but less extreme pattern: 249 attempts from
212 students, a 13.2% failure rate, an average grade of 2.80, and a
self-loop weight of 21 with avg_grade_from = 4.85. Econ 11 (Markets and
the State) is a GE subject with a moderate 4.9% failure rate across 185
attempts. HRIM 116 is the only HRIM course with a non-trivial failure
rate: 4.0% from 273 attempts, average grade 2.09, self-loop weight 11.

4.3.3. Layer 3: HRIM Majors Convergence Sink (Green)

Once students clear the quantitative bottleneck, the network converges
toward a dense cluster of HRIM subjects. HRIM 120 receives the highest
in-degree of any non-PE node at 1,106. Its 0.0% failure rate and average
grade of 1.35 indicate that students who reach HRIM 120 perform
exceptionally well. Downstream, the network fans out into core HRIM
courses, all with 0.0% failure rates and grades clustering between 1.0
and 1.7: HRIM 131 (138 students, avg 1.69), HRIM 132 (148, avg 1.25),
HRIM 140–144 (84–87 students, avg 1.36–1.52), and HE/FN/FS courses
(0.0–0.6% failure). HRIM 186 (Practicum) is the terminal course; 15
students are currently enrolled.

Figure 3.

Sankey diagram of the Student Progression Flow of the UP Diliman BS HRIM
program. N = 269.

[]

Note. Three-tier curriculum funnel from enrollment through the
quantitative gate to upper-division HRIM coursework and near-completion.
Grey = not yet at quantitative gate (n ≈ 75); Red = retaking Math 21 or
Stat 101 (n ≈ 23); Orange = pending next milestone; Green/Teal =
milestone cleared.

The Sankey diagram in Figure 3 visualizes how 269 BS HRIM students
progress through a three-tier funnel: from all enrolled students,
through the quantitative gate (Math 21 and Stat 101), to HRIM 131, then
to the HRIM 150 series, and near completion. It highlights three key
flows: students not yet at the quantitative gate; students stuck in
quantitative retakes (Math 21 and Stat 101); and students who have
cleared HRIM 131 and are either pending HRIM 150 series or already near
or at completion. The width of each stream makes clear that the largest
losses and delays occur at the quantitative gate and just before HRIM
150, not in the upper-division HRIM core itself.

4.4. Comparative Network Parameters

Table 8 presents computed graph-theoretic parameters for both networks
side by side. The contrast between the two columns is the quantitative
signature of the gap between curriculum design and actual student
navigation.

Table 8.

Comparative Network Parameters—Structural vs. Empirical Networks

  --------------------------------------- -------------- --------------
                 Parameter                  Structural     Empirical

                 Nodes (N)                      49             56

         Edges (excl. self-loops)               36           1,621

              Self-loop edges                   0              12

               Graph density                  0.015          0.526

         Average degree (in = out)             0.74          28.95

               Max in-degree                    3              55

              Max out-degree                    8              53

        Weakly connected components             13             1

       Strongly connected components            49             2

          Largest WCC node count                31             56

      Avg shortest path (largest WCC)         3.135          1.358

      Network diameter (largest WCC)            6              2

        Avg clustering coefficient            0.000          0.807

                Reciprocity                   0.000          0.780

                  Is DAG?                      Yes             No

        Longest prereq path (edges)             4              —

         Source nodes (in-deg = 0)              16             1

         Sink nodes (out-deg = 0)               28             0

            Louvain communities                 9              3

               Modularity Q                   0.674          0.231
  --------------------------------------- -------------- --------------

Note. Density = E / [N(N−1)]. Shortest path and diameter computed on
undirected projection of largest weakly connected component. Node-count
difference (49 vs. 56) arises because the empirical network includes
elective variants and alternative-slot choices appearing in student
records but not in the prerequisite graph. Weighted parameters: avg.
weighted degree = 408.4; max weighted in-degree = 1,541 (PE 2); max
weighted out-degree = 1,679 (PE 2).

Density exhibits the starkest contrast: the structural network’s 0.015
indicates only 1.5% of potential directed links are official
prerequisites, whereas the empirical network’s 0.526 shows over half of
possible transitions observed, a 35-fold difference reflecting students’
behaviors like enrolling in multiple courses simultaneously, repeating
failed ones, and taking optional courses in flexible
sequences—connections not prescribed by the curriculum.

Degree statistics reinforce this: the structural network’s average
degree of 0.74 suggests most courses have fewer than one prerequisite or
dependent, consistent with a sparse prerequisite tree, while the
empirical network’s average degree of 28.95 shows each course connected
to nearly every other through observed transitions, with a maximum
in-degree of 3 (HRIM 131) versus 55 (PE 2). Shortest path length
decreases from 3.14 to 1.36, and diameter from 6 to 2, reflecting that
nearly any two courses are directly connected or separated by one course
in the empirical network. Clustering coefficient and reciprocity are
zero in the structural network but high (0.807 and 0.780) in the
empirical network, indicating co-enrollment and students moving back and
forth across semesters. Modularity drops from 0.674 to 0.231, indicating
blurred community boundaries and suggesting increased curriculum
friction, in which students cycle through lower-level courses rather
than progressing.

4.5. Self-Loops (Retake Patterns)

Twelve courses generated self-loop edges, meaning students returned to
take the same course in a later semester. Self-loops for other subjects
are shown in Table 9.

Table 9.

Self-Loop Analysis of the UP Diliman BS HRIM program.

  ----------- ---------- -------------- --------------------------------
    Course      Retake    Avg Grade at           Interpretation
                Count        Entry      

     PE 2        182          1.27      Structural: required to take PE
                                                   four times

     NSTP         89          1.4        Structural: NSTP modules span
                                                 two semesters

    Math 21       71          4.94      Failure-driven: avg grade ≈ 5.0,
                                                mandatory retake

     PE 4         42          1.1         Structural: student-athletes
                                              take PE 4 four times

   Stat 101       21          4.85      Failure-driven: avg grade ≈ 5.0,
                                                required retake

   HRIM 116       11          3.82        Mixed: near-failing students
                                                   repeating

     Kas 1        3            4          Failure-driven: small number

   HRIM 110       1            5        Failure-driven: single instance

    Philo 1       1            5        Failure-driven: single instance

     Eng 1        1            5        Failure-driven: single instance

    FN 102        1            4        Failure-driven: single instance

  FL Elective     1            5        Failure-driven: single instance
       1                                
  ----------- ---------- -------------- --------------------------------

The pattern is clear: Math 21 and Stat 101 generate mandatory
failure-retake loops (average entry grade near 5.0), while PE 2
generates self-loops because it must be taken 4 times.

4.6. Curriculum Flexibility

The checklist includes several slash-alternative slots in which students
satisfy a requirement by choosing one of two or more designated courses.
Zuev & Stavrinides (2025) distinguish between conjunctive prerequisites
(all required) and disjunctive prerequisites (one of several
alternatives). The BS HRIM slash-alternatives are disjunctive; each was
parsed separately and treated as a distinct node reflecting actual
enrollment.

Among the observed choices, Soc Sci 1 attracted 100 students, compared
with 77 for Soc Sci 2. STS 1 was the overwhelming choice (191 students),
compared with DRMAPS (7 students), reflecting disparities in section
availability. HRIM electives follow a strict sequential pattern
(Elective 1 → 2 → 3). A cohort of off-season students took an elective
ahead of schedule but could not progress to the HRIM 150 series due to
prerequisite restrictions—specifically, failure to pass Math 21 on time.
PI 100 (Life and Works of Jose Rizal), mandated by Republic Act No.
1425, has been completed by 59 students with a 0.0% failure rate.
Overall, the limited flexibility of alternatives offers few options for
students stuck at quantitative bottlenecks.

5. Discussion and Implications

5.1. Discussion

The weighted dual-network analysis reveals a three-tier curriculum
funnel: a broad general education and introductory HRIM foundation layer
that co-enrolls with dozens of courses and generates dense
early-semester transitions; a quantitative bottleneck (Math 21 and Stat
101) that acts as a filter before HRIM 131; and a tightly convergent
upper-division HRIM core anchored by HRIM 120 (in-degree 1,106, 0.0%
failure rate), flowing into specialization courses and the terminal
practicum cluster.

This three-tier structure maps onto the flux profile of Zuev &
Stavrinides (2025). Layer 1 corresponds to positive-flux strata that
emit more prerequisite links downstream than they receive—the
curriculum’s knowledge-injection layer. Layer 2 represents the peak-flux
stratum where the prerequisite concentration is highest, and failure has
maximum downstream consequences. Layer 3 corresponds to negative-flux
strata that consume many prerequisites while producing few—the terminal
knowledge-absorption phase. This flux interpretation elevates the
three-tier model from descriptive observation to theoretical
characterization.

Math 21’s downstream impact is best understood through the reach metric
(Yang et al., 2024). Math 21 is an indirect prerequisite to the entire
HRIM 150 series and all subsequent major courses. Any student who fails
faces two consequences: a delay in that single course and an effective
lockout from a large portion of their degree for at least one additional
semester. Yang et al. found introductory mathematics bottlenecks most
severe at the largest institutions. UP Diliman, as the flagship state
university of the Philippines, fits this pattern precisely,
strengthening the generalizability of the BS HRIM findings across
different national and institutional contexts.

The most actionable signal is the Math 21 bottleneck. Targeted early
intervention—tutoring support and curricular scaffolding with Math 20—is
the highest-leverage action. Another option is to allow students who
failed Math 21 to take HRIM 131 concurrently, requiring both courses to
be passed before progressing to the HRIM 150 series. Without this
change, the Math 21 self-loop continues indefinitely. All HRIM courses
above HRIM 120 have zero failures, suggesting that once students clear
the quantitative prerequisites, they are well prepared to complete their
major requirements.

Comparative network analysis (Table 8) provides macro-level
quantification of curriculum friction. The modularity gap (0.674 vs.
0.231) reveals a design-reality gap: the curriculum is designed as
well-partitioned communities, but student progression blurs these
boundaries as failing students cycle back through lower-tier courses.
The 35-fold density contrast (0.015 vs. 0.526) confirms students are not
following the prescribed linear path, driven largely by the Math 21/Stat
101 bottleneck forcing schedule reorganization.

We emphasize that network positions and failure rates identify
structurally high‑risk locations rather than prove causality; structural
risk (high reach, blocking factor) and performance risk (high failure
rates) should be read together, and any causal claims would require
additional qualitative work and predictive modeling using prior grades
or entry scores.

5.2. Institutional Resource Impact of Math 21

The third research objective was to quantify failure rate impacts on
institutional resources and student progress. Of the 194 students who
have attempted Math 21, only 171 have passed, leaving 23 students
(11.9%) caught in mandatory retake cycles. The self-loop weight of 71
means Math 21 has consumed approximately 71 additional student-semester
enrollment slots beyond its expected first-attempt load.

The downstream cascade is severe. Each failed attempt at Math 21 delays
access to 16 downstream courses (reach = 17, including HRIM 131 itself)
by at least one semester. HRIM 131 has been offered every semester since
2022—twice per year rather than once—specifically to accommodate
students delayed by failures in Math 21 and Stat 101. This constitutes
at least three additional off-schedule section offerings over four
academic years, each requiring faculty allocation, classroom assignment,
and administrative scheduling outside the standard calendar.

With enrollment nearly quadrupling between 2021 and 2025, this
structural pressure is not temporary but a recurring cost embedded in
the current prerequisite architecture. The network analysis confirms
that no alternative pathway exists: Math 21 has a blocking factor of 1
and a reach of 17, with no redundant route bypassing this chokepoint.

The universality of this pattern is supported by Yang et al. (2024), who
found that introductory mathematics courses achieved the highest
betweenness centrality and reach values across all six institutional
CPNs studied, from CalTech’s 771-node network to UIUC’s 5,126-node
network. The BS HRIM finding extends this structural regularity to a
non-STEM, service-sector professional program in the ASEAN region. In
Zuev & Stavrinides’s (2025) flux framework, the stratum containing Math
21 would exhibit anomalously high positive flux—it emits far more
prerequisite links downstream than it receives—making it the most
consequential leverage point for curricular intervention.

5.3. Academic and Practical Implications

The study will inform curriculum review and future revisions. It aligns
with ASEAN University Network Quality Assurance (AUN-QA) standards,
under which the program was certified in 2023. These findings are
actionable and consistent with Basavaraj et al. (2022), who demonstrated
that network-based curricular analytics inform academic advising
strategies by identifying which courses require additional support and
which student sub-populations need targeted intervention.

For BS HRIM, this translates to actionable advising protocols. Flag
students who have not cleared Math 21 or Stat 101 by the end of their
second semester. These students are at elevated risk of multi-semester
delays. Early and proactive advising prevents the prerequisite trap from
compounding.

5.4. Limitations and Suggestions for Future Research

This study has important limitations. It is limited to a single
institution and includes only currently enrolled students. Graduates and
students who have left the program were excluded, introducing
survivorship bias. Students who attempted Math 21 multiple times and
ultimately withdrew are not represented in the N = 269 dataset. All
reported course-level failure rates are therefore conservative
lower-bound estimates; the actual proportion unable to clear the
quantitative bottleneck is likely higher.

Future research should incorporate full cohort records, including
withdrawn students, for unbiased attrition estimates. Qualitative
interviews with students who dropped or failed would illuminate root
causes—academic difficulty, scheduling conflicts, or both. Comparative
studies with other BS HRIM or hospitality management programs in the
Philippines and broader ASEAN region would help determine whether this
bottleneck is institution-specific or reflects systemic patterns in
hospitality education.

6. Conclusion

This dual-network analysis reveals a substantial design–reality gap
between the sparse, hierarchical prerequisite structure of the BS HRIM
curriculum and the dense, highly clustered empirical progression network
generated by actual student trajectories. In particular, Math 21 and
HRIM 131 form a quantitative gate that concentrates structural and
performance risk and amplifies delays for large cohorts.

For practitioners and policy-makers, the main implications are to (1)
prioritize early support and capacity planning for quantitative
gatekeeping courses, (2) review the reliance on a single, linear
quantitative chain in light of hospitality competency and accreditation
frameworks, and (3) adopt curriculum network analytics as a routine tool
for monitoring progression and evaluating proposed reforms before
full-scale implementation.

References

Aldrich, P. R. (2015). The curriculum prerequisite network: Modeling the
curriculum as a complex system. Biochemistry and Molecular Biology
Education, 43(3), 168–180. https://doi.org/10.1002/bmb.20861

Basavaraj, P., Garibay, I., & Ozmen Garibay, O. (2022). Pathway patterns
mobility study of first time vs. Transfer students in computer science
and information technology programs at a public university. Journal of
Applied Research in Higher Education, 14(2), 784–807.
https://doi.org/10.1108/JARHE-12-2020-0429

Blondel, V. D., Guillaume, J.-L., Lambiotte, R., & Lefebvre, E. (2008).
Fast unfolding of communities in large networks. Journal of Statistical
Mechanics: Theory and Experiment, 2008(10), P10008.
https://doi.org/10.1088/1742-5468/2008/10/P10008

Conijn, R., Snijders, C., Kleingeld, A., & Matzat, U. (2017). Predicting
Student Performance from LMS Data: A Comparison of 17 Blended Courses
Using Moodle LMS. IEEE Transactions on Learning Technologies, 10(1),
17–29. https://doi.org/10.1109/TLT.2016.2616312

Cullen, T. P., & Lambert, C. U. (1987). Teaching Quantitative Decision
Skills in a Hospitality Curriculum. Cornell Hotel and Restaurant
Administration Quarterly, 28(2), 42–45.
https://doi.org/10.1177/001088048702800215

EDCOM 2. (2026, February 14). CHED curriculum updates take 11 years on
average. EDCOM 2.
https://edcom2.gov.ph/ched-curriculum-updates-take-11-years-on-average/

Fei, A., Chen, J., Lee, W., Xin, K., Behnke, C., & Gordon, S. (2025).
Designing Hospitality Curriculum for the Future: A Comprehensive
Assessment of an Undergraduate Program in the United States. Journal of
Hospitality & Tourism Education, 37(2), 138–153.
https://doi.org/10.1080/10963758.2025.2453736

Hagberg, A. A., Schult, D. A., & Swart, P. J. (2008). Exploring Network
Structure, Dynamics, and Function using NetworkX. 11–15.
https://doi.org/10.25080/TCWV9851

Heileman, G. L., Thompson-Arjona, W. G., Abar, O., & Free, H. W. (2019,
June 15). Does Curricular Complexity Imply Program Quality? 2019 ASEE
Annual Conference & Exposition.
https://peer.asee.org/does-curricular-complexity-imply-program-quality

Jacomy, M., Venturini, T., Heymann, S., & Bastian, M. (2014).
ForceAtlas2, a Continuous Graph Layout Algorithm for Handy Network
Visualization Designed for the Gephi Software. PLoS ONE, 9(6), e98679.
https://doi.org/10.1371/journal.pone.0098679

Newman, M. E. J., & Girvan, M. (2004). Finding and evaluating community
structure in networks. Physical Review E, 69(2), 026113.
https://doi.org/10.1103/PhysRevE.69.026113

Rienties, B., & Toetenel, L. (2016). The impact of learning design on
student behaviour, satisfaction and performance: A cross-institutional
comparison across 151 modules. Computers in Human Behavior, 60, 333–341.
https://doi.org/10.1016/j.chb.2016.02.074

Roxas, R. M., & Tapang, G. (2010). Prose and poetry classification and
boundary detection using word adjacency network analysis. International
Journal of Modern Physics C, 21(04), 503–512.

Slim, A., Heileman, G. L., Kozlick, J., & Abdallah, C. T. (2014).
Predicting student success based on prior performance. 2014 IEEE
Symposium on Computational Intelligence and Data Mining (CIDM), 410–415.
https://doi.org/10.1109/CIDM.2014.7008697

Wang, J., & Abukhalifeh, A. N. M. (2021). Evaluating Undergraduate
Curriculum in Hospitality Management: A Comparison between China and
South Korea. Journal of China Tourism Research, 17(4), 613–633.
https://doi.org/10.1080/19388160.2020.1788684

Yang, B., Gharebhaygloo, M., Rondi, H. R., Hortis, E., Lostalo, E. Z.,
Huang, X., & Ercal, G. (2024). Comparative analysis of course
prerequisite networks for five Midwestern public institutions. Applied
Network Science, 9(1), 25. https://doi.org/10.1007/s41109-024-00637-z

Zuev, K. M., & Stavrinides, P. (2025). Breadth, depth, and flux of
course-prerequisite networks. Network Science, 13, e17.
https://doi.org/10.1017/nws.2025.10013
