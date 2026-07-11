**Curriculum Network Analysis of Quantitative Bottlenecks in**

**Hospitality Management Education (Paper #445)**

**Larissa Mae Maranan-Montano**

**Department of Hotel, Restaurant and Institution Management & Data
Science Program**

**University of the Philippines Diliman**

**Giovanni A. Tapang**

**National Institute of Physics & Data Science Program**

**University of the Philippines Diliman**

**Abstract:**

This study uses a dual-network analysis to evaluate student progression
in a rapidly growing hospitality bachelor's program. The program has
expanded by 64% since 2024, yet the 2021 curricular revision has
produced an on-time graduation rate of only 24%. To identify the
systemic drivers of this delay, the curriculum is modeled through two
distinct lenses: a structural curriculum network based on official
prerequisites and an empirical progression network derived from the
records of N=269 students. Structural analysis reveals a high-risk
prerequisite chain centered on the subjects of calculus (CALC) and
statistics (STAT), with the operations management (ORM) subject serving
as the main structural chokepoint (betweenness centrality = 0.0335).
Louvain community detection confirms strong structural partitioning
(modularity Q = 0.674) that degrades sharply in the empirical network (Q
= 0.231), where failure and retake cycles blur intended prerequisite
tiers. CALC emerges as the dominant academic bottleneck, with a 37.3%
failure rate, 295 total attempts from 194 unique students, and a
self-loop weight of 71, confirming mandatory failure-driven retakes. The
dominant empirical hub by degree is PHYSED2, a structural artifact of
its four-time enrollment requirement. These findings support targeted
early intervention in quantitative courses and curriculum revisions that
reduce reliance on a single prerequisite chain. In this program, 76% of
students did not graduate on time under the revised curriculum, even
though some may eventually complete it.

**Keywords:** hospitality education, curriculum network, curriculum
roadblocks

**1. Introduction**

In this paper, we discuss a bachelor's program in hospitality management
at a local university that has experienced unprecedented growth. Between
2023 and 2025, new cohorts have grown to represent over 60% of total
enrollment, with section counts escalating from a single section in 2021
to four sections by 2025. However, this growth has collided with the
structural rigidities of the 156-unit curriculum revised in 2021.
Preliminary data from the inaugural 2021 cohort reveal a concerning
trend: only 24% graduated on time. On-time graduation means completing
all 156 required units within eight regular semesters (four academic
years), excluding midyear terms. The remaining 76% have either withdrawn
or faced significant delays.

The primary driver of delays is the prerequisite trap centered on core
quantitative and professional courses. The progression into the culinary
management (CUL) series, a critical fifth-semester block that must be
taken in its entirety, requires successful completion of operations
management (ORM). ORM requires CALC and STAT. High failure rates in
these foundational subjects have created a massive backlog. The
department has offered ORM every semester since 2022 to accommodate
students who have been delayed by one to five semesters.

This off-season scheduling places an unsustainable strain on limited
faculty and classroom resources. With the population nearly quadrupling
in four years, the department faces a dual crisis: maintaining academic
rigor while ensuring student flow through a curriculum that currently
lacks the flexibility to absorb failure or delay. There is an urgent
need to shift from anecdotal observations to data-driven modeling to
understand how these prerequisite chains impact student momentum.

*Research Objectives*

This study seeks to provide a quantitative framework for curriculum
management by pursuing the following objectives:

1.  Map the given hospitality curriculum as an empirical progression
    network to visualize student flow.

2.  Identify specific bottleneck nodes that disproportionately hinder
    on-time graduation.

3.  Quantify the impact of failure rates on institutional resources and
    student progress.

**2. Literature Review**

*2.1. Structural Complexity and Curricular Analytics*

Network analysis is widely used across fields to study complex systems
by modeling entities as nodes and their relationships as links (Roxas,
2010). Modern curricular assessment has shifted from subjective
evaluation toward curricular analytics, which models degree programs as
directed curriculum networks. Within this framework, courses are treated
as nodes and prerequisites as directed edges. Aldrich (2015) provided an
early formal treatment by modeling the undergraduate curriculum at
Benedictine University as a Course Prerequisite Network (CPN), revealing
hidden community clusters, bridges, and hub courses not apparent from
the catalog alone. Structural complexity in CPNs is defined by three key
metrics: the blocking factor (courses blocked by a single failure), the
delay factor (the longest prerequisite chain through a course), and
centrality (Slim et al., 2014; Heileman et al., 2019). High structural
complexity often correlates with higher failure rates and elongated
time-to-degree, particularly in professional programs where foundational
quantitative sequences act as gatekeepers with high blocking factors.

Yang et al. (2024) provide the most comprehensive peer-reviewed CPN
application across public universities. They formally define the CPN as
G = (V, E) and apply centrality measures---betweenness centrality,
out-degree, reach, and transpose PageRank---to the CPNs of six American
institutions. Their reach(v) metric quantifies the total downstream
courses for which course v is a direct or indirect prerequisite. Their
findings confirm that mathematics courses achieve the highest
betweenness centrality and reach values across all institutions studied,
establishing mathematics prerequisites as a structural feature of
STEM-adjacent curricula rather than an institutional anomaly. Yang et
al. further introduce the Longest Paths Induced sub-Graph (LPIG), the
subgraph containing all courses on prerequisite chains of length ≥ k, as
a formal construct for identifying the most highly constrained degree
pathways.

Zuev & Stavrinides (2025) introduce three global CPN measures---breadth
(B), depth (D), and flux (Φ)---grounded in topological stratification,
enabling whole-curriculum diagnosis beyond node-level properties.
Basavaraj et al. (2022) combined Sankey visualizations with network
science curricular analytics to map degree mobility patterns, finding
that foundational course performance is the primary driver of
differences in progression across cohorts. This body of work establishes
that the network-analytic approach is not merely descriptive but
diagnostic: the structural position of a course in the CPN predicts its
real-world impact on student progression and time-to-degree.

*2.2. Learning Analytics and Student Progression*

Learning analytics (LA) measures and reports data on learners and their
contexts to understand and optimize learning and the environments in
which it occurs (Conijn et al., 2017). Rienties & Toetenel (2016)
studied 151 modules and 111,256 students at the UK Open University,
finding that the structural design of a course strongly predicts student
engagement, retention, and satisfaction. This parallels the rationale
for applying network-level curriculum metrics: both approaches treat
program structure as a tractable, data-measurable driver of student
outcomes rather than as a fixed condition.

Predictive modeling has extended this to identifying at-risk
individuals. Conijn et al. (2017) compared 17 blended courses at a Dutch
university and demonstrated that LMS engagement data can accurately
predict final course grades, enabling intervention before failure
becomes irreversible. For structured prerequisite programs like the
hospitality curriculum, this has significant implications: early
engagement predicts course-level outcomes, and course-level outcomes in
prerequisite-gating courses predict degree-level trajectories.
Identifying bottleneck courses through network analysis is a critical
first step in at-risk identification pipelines.

In the Philippine higher education context, these issues carry
particular urgency. The Commission on Higher Education (CHED) updates
its Policies, Standards, and Guidelines (PSGs) on average every 11 years
(EDCOM II, 2023). Structural curricular problems identified today may
persist for nearly a decade before the next revision window. This
institutional inertia makes data-driven, within-cycle evidence
especially valuable. Curriculum network analysis provides precisely this
type of evidence, allowing programs to optimize student outcomes without
waiting for a full curriculum overhaul.

*2.3. The Hospitality Curriculum*

Quantitative subjects such as calculus and statistics have long been
integrated into hospitality curricula (Cullen & Lambert, 1987). For
example, Cullen and Lambert (1987) report that leading U.S. hospitality
programs typically require at least one semester of business statistics
and one analytics-oriented course. More recently, Fei et al. (2025)
highlight modules on revenue management, demand forecasting, and
data-driven pricing as standard quantitative components in contemporary
hospitality degrees.

Regional comparisons of hospitality programs in Asia reveal that
curricula frequently struggle to balance business-theoretical
foundations with specialized practical training (Wang & Abukhalifeh,
2021). Fei et al. (2025) recommend that future curricular revisions
prioritize immersive industry-based learning, hospitality-specific
technologies such as CRM systems and online reservation platforms, and a
heightened focus on big data and analytics.

Notably, the ASEAN Common Competency Standards for Tourism Professionals
(ACCSTP) and the Common ASEAN Tourism Curriculum (CATC) do not list
quantitative analytics, statistics, or calculus as explicit competency
domains. The heavy quantitative prerequisite chain in the hospitality
curriculum under consideration (PRECALC → CALC → STAT → ORM) is
therefore a feature of CHED's academic degree framework, not a
requirement of the ACCSTP vocational competency standards. This
structural tension between academic gating logic and the industry-facing
competency framework governing regional workforce mobility is a key
contextual factor in the present analysis.

*2.4. Research Gap*

Curriculum network analysis literature is growing, but applications to
hospitality management programs remain scarce. Existing CPN studies have
focused on STEM, computing, and general undergraduate programs at North
American and European institutions (Aldrich, 2015; Yang et al., 2024).
The structural dynamics of professional service-sector curricula---which
combine quantitative requirements with practicum-heavy experiential
sequences---remain unexamined.

Philippine hospitality programs face additional complexity. The said
hospitality program is governed by CHED's PSG framework, operates under
AUN-QA accreditation standards, and has undergone rapid enrollment
expansion in the post-pandemic period. These conditions allow structural
prerequisite bottlenecks to compound quickly across large cohorts. The
present study fills this gap by applying a dual-network curriculum
analysis that combines a structural blueprint with empirical student
flow---the first network-analytic bottleneck assessment of a hospitality
management curriculum in the ASEAN region.

**3. Methodology**

This study employs a dual-network analysis approach to evaluate the
hospitality program. Both networks share the same node set of courses.
However, they encode different edge types. The structural network uses
prerequisites from the official curriculum document. The empirical
network uses observed student transitions from enrollment records. We
developed two distinct models. The Structural Curriculum Network maps
the program\'s theoretical design. The Empirical Progression Network
analyzes the actual movement of N = 269 students.

*3.1. Structural Curriculum Network*

The initial phase involved modeling the formal 156-unit hospitality
curriculum as a directed graph to quantify its inherent complexity.
Following Yang et al. (2024), the curriculum is formally encoded as a
CPN G = (V, E). Graph-theoretic centrality measures identify courses of
structural importance, including betweenness centrality and node reach.
Following Zuev & Stavrinides (2025), a transitive reduction was applied
to remove any edge i → k where a longer directed path i → ... → k
already exists, ensuring that computed centrality values reflect only
essential prerequisite structure.

Nodes represent each unique subject in the 156-unit program. Directed
edges link prerequisite subjects to their subsequent target courses.
Prerequisite edges were assigned a weight of w = 2, reflecting a hard
sequential dependency in which failure fully blocks access. Corequisite
edges were assigned w = 1, reflecting softer coupling, allowing
concurrent enrollment. To assess sensitivity, all centrality measures
reported in §4.1 were recomputed under uniform weighting (w = 1 for all
edges). The top-five betweenness and reach rankings were unchanged,
confirming that structural bottleneck identification is robust to the
weighting scheme.

Co-requisites are treated as unidirectional edges from the first-offered
term to the co-offered course. Retake loops in the empirical flow are
represented as parallel paths rather than back-edges. This preserves the
acyclicity of the directed curriculum network.

*3.2. Empirical Progression Network*

The second phase modeled students\' actual academic histories to
identify deviations from the theoretical blueprint. We extracted and
anonymized the curriculum checklists of N = 269 students currently
enrolled under the current curriculum (covering the 2021--2025 cohorts).
Unlike the static structural network, this model maps the subjects
students actually took sequentially, including retakes and off-season
enrollments. Each node was enriched with performance data, including
total attempts, failure rate (f), and counts of incomplete (INC) or
dropped (DRP) attempts. Edges were weighted by transition
frequency---the volume of student flow between subjects across all
recorded semesters.

This phase follows the analytical pipeline established by Basavaraj et
al. (2022), who extracted term-by-term institutional enrollment records
for student cohorts and overlaid them on a curricular network
representation to identify which courses generated the greatest
disruptions in student degree mobility. Their approach of coupling
historical student-flow data with network analysis to "provide
recommendations to improve student outcomes" (Basavaraj et al., 2022, p.
791) directly informs the construction of the empirical progression
network in the present study.

*3.3. Visualization and Comparative Analysis*

Both networks were constructed and analyzed using the Python NetworkX
library (Hagberg et al., 2008). The structural network was rendered
using a hierarchical layout ordered by topological level---entry-point
courses with no prerequisites at the top, deeper prerequisite levels
descending---to make prerequisite flow visually explicit. The empirical
network was rendered using the ForceAtlas2 force-directed algorithm
(Jacomy et al., 2014), which positions high-degree hub nodes centrally
and clusters tightly connected courses together.

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
of student movement through high-stakes blocks like the CUL series; and
path deviation, comparing theoretical network diameter against the
actual multi-attempt paths taken by students to identify systemic
delays.

**4. Results**

*4.1.* *Structural Curriculum Network Analysis*

The visualization reveals a highly centralized network architecture with
a clear prerequisite backbone. The following are the key structural
features of the curriculum.

*4.1.1. High-risk Prerequisite Chain*

In Figure 1, the red cluster constitutes the highest-risk prerequisite
sequence in the structural network. This path is a single-file line
starting with PRECALC (pre-calculus mathematics), a non-credit bridging
course that is a prerequisite for CALC. STAT and CALC are prerequisites
for ORM, which is the gateway to the CUL (culinary) series. Failure at
any node in this sequence blocks all downstream progression. Academic
advisers encourage students to attempt CALC and STAT during their first
year to minimize cumulative delay.

Figure 1.

*Structural Curriculum Network of the Hospitality Program (156 units)*

![](media/image3.png){width="6.267716535433071in" height="3.625in"}

*Note.* Nodes represent individual courses; directed edges point from
prerequisite to dependent course. Node color encodes Louvain community
membership (modularity Q = 0.674; red = quantitative chain community,
purple = hospitality foundational cluster, gray = general education (GE)
and other clusters). Node size is proportional to out-degree. Key
bottleneck courses (CALC, STAT, MICRO, ORM) are labeled in the figure.

*4.1.2. Hub Dominance*

Two major high-degree star subgraphs are evident: MICRO
(micro-perspectives in hospitality, generally taken during the first two
years) and CUL/RES (research, junior courses). MICRO has a massive
out-degree, serving as the prerequisite for at least seven core courses.
CUL and RES act as gatekeepers to senior courses with high betweenness
centrality. Congestion at either node constrains the entire graduation
pipeline.

*4.1.3. Structural Asymmetry*

The early clusters are broad but shallow; the later clusters are deep
with many successive prerequisites. In the framework of Zuev &
Stavrinides (2025), this asymmetry is formally captured by topological
stratification: the early strata S₁--S₂ are wide (high breadth, many
courses per stratum), while the later strata leading to the CUL and LAW
series are narrow, producing a high-depth, low-breadth terminal
structure. A curriculum with this profile has the longest path relative
to its total node count---precisely the structural condition that Zuev &
Stavrinides identify as associated with constrained degree programs and
extended time-to-graduation. The "high-risk chain of survival"
corresponds to the long-path subgraph that would dominate the
hospitality LPIG, confirming the linear quantitative prerequisite chain
as a systemic architectural feature.

*4.1.4. Community Structure*

Louvain community detection yields nine communities at Q = 0.674, well
above the threshold for meaningful community structure (Q \> 0.30;
Newman & Girvan, 2004). The largest community (C1, 12 courses) groups
PRECALC, CALC, STAT, and ORM (operations management) with their
downstream senior electives, confirming this chain as a single
structurally cohesive unit. C2 (9 courses) captures the hospitality
foundation cluster anchored by MICRO, encompassing all seven courses
directly unlocked by MICRO, as well as its two prerequisite feeders
(MACRO, or macro-perspectives in hospitality, and ACCT, or accounting
management). Smaller communities correspond to the PE series, English
composition, SERV (service training program), and foreign language
elective pairs. The high modularity reinforces structural asymmetry: the
curriculum is a set of largely separate prerequisite sub-chains
converging at two chokepoints, MICRO and ORM, before diverging again
into the senior tier.

*4.1.5. Structural Network Centrality Measures*

Table 1 reports six graph-theoretic metrics for key curriculum nodes
(Yang et al., 2024; Zuev & Stavrinides, 2025). In-degree counts
prerequisites; out-degree counts courses directly unlocked; betweenness
centrality measures the proportion of shortest paths passing through a
node; reach quantifies the total downstream courses; delay factor
measures the longest prerequisite chain from a node; and blocking factor
counts courses immediately inaccessible upon failure. The values in
Table 1 include all downstream courses in the curriculum, including both
hospitality and non-hospitality subjects, which explains why MICRO's
reach (26) exceeds CALC's (17).

Table 1.

*Structural Centrality Measures**---** Key Hospitality Curriculum Nodes*

  --------------------------------------------------------------------------------------------
  **Course**     **In-deg**   **Out-deg**   **Betweenness**   **Reach**   **Block.   **Delay
                                                                          F.**       F.**
  -------------- ------------ ------------- ----------------- ----------- ---------- ---------
  ORM            3            6             0.0335            16          6          3

  MICRO          2            8             0.0182            26          8          4

  CUL            1            2             0.0098            4           2          2

  CALC           1            1             0.0059            17          1          4

  RES            1            1             0.0028            1           1          1

  STAT           0            1             0.0000            17          1          4

  MACRO          0            1             0.0000            27          1          5

  ACCT           0            1             0.0000            27          1          5

  PRECALC        0            1             0.0000            18          1          5

  PRACTICUM      1            0             0.0000            0           0          0
  --------------------------------------------------------------------------------------------

*Note.* Betweenness centrality is normalized. Reach = total downstream
courses unlocked (Yang et al., 2024). Blocking factor = number of
courses immediately inaccessible upon failure. Delay factor = length of
longest prerequisite chain from this node.

Three findings stand out from Table 1. First, ORM has the highest
betweenness centrality (BC = 0.0335). It is the sole gateway through
which all paths from foundational quantitative courses---CALC, STAT, and
MICRO---converge and fan out into the CUL series, making it the
curriculum's structural chokepoint. Second, MICRO has the highest
out-degree and blocking factor (8), serving as the program's primary
hub; a single failure can lock out eight courses simultaneously. Third,
CALC's betweenness is comparatively lower (BC = 0.0059), but its reach
of 17 and delay factor of 4 confirm disproportionate downstream
influence. Any student who fails CALC is indirectly blocked from 17
courses and faces a prerequisite chain four levels deep before program
completion.

*4.2. Profile of Students for the Empirical Progression Network*

The sample consists of 269 students. The distribution is skewed toward
new students: 34.6% are from the 2025--2026 cohort, and 29.4% are from
the 2024--2025 cohort. The overall average weighted average grade (WAG)
is 1.81. About 72% of students have a WAG of 2.25 or better, indicating
solid overall academic performance. Thirty-six (36) students (13.4%) are
near or at completion (120+ units), while 57 students (21.2%) are in
their early stages (\<30 units), consistent with the large incoming
cohort. Almost all students have completed MACRO. Nearly 5% have yet to
pass ACCT, indicating an early bottleneck. More students have passed
STAT than CALC. Low completion rates for upper-level courses (CUL+) are
expected, given the large incoming cohorts.

*4.3. Results of Network and Bottleneck Analysis*

Table 7.

*Network Overview*

  --------------------------------------------------------------------
  **Metric**                               **Value**
  ---------------------------------------- ---------------------------
  Nodes (courses)                          56

  Total edges                              1,633

  Self-loop edges (retakes)                12

  Non-self-loop transition edges           1,621

  Core-prefix nodes                        27

  GE / other nodes                         29

  Only pure source node (no in-edges)      ENG

  Highest in-degree node                   PHYSED 2 (in = 1,541)

  Highest out-degree node                  PHYSED 2 (out = 1,679)

  Strongest convergence sink               MICRO (in = 1,106)
  --------------------------------------------------------------------

With 269 students moving through the curriculum, the high edge count
shows that students are not following a linear path. They are
distributing across available courses, likely due to failing
prerequisites. MICRO serves as the primary convergence sink,
demonstrating its role as a high-friction gatekeeper.

Louvain community detection on the empirical network yields three
communities at Q = 0.231. While lower than the structural network's Q =
0.674---which is expected given that students physically traverse all
tiers and create cross-community edges---the value remains above the Q
\> 0.10 threshold for detectable mesoscale structure (Newman & Girvan,
2004). The three communities correspond to curriculum tiers: Community 3
(red, n = 16) groups foundation and entry-level courses; Community 2
(blue, n = 20) captures the gateway and mid-tier courses including the
quantitative bottleneck (CALC, STAT) and the ORM convergence node; and
Community 1 (green, n = 20) encompasses upper-division and senior
specialisation courses. The lower modularity quantifies a key finding:
failing students recycle through foundation courses across semesters,
blurring the clean tier boundaries visible in the official curriculum.

Figure 2.

*Empirical Progression Network of Hospitality Students (N = 269)*

![](media/image2.png){width="6.267716535433071in" height="5.0in"}

*Note.* Nodes represent courses as actually enrolled in by students;
directed edges connect sequentially enrolled courses across semesters,
with only transitions of five or more student instances shown. Edge
thickness proportional to transition frequency. Node color encodes
Louvain community membership (Q = 0.231). Node size proportional to
weighted in-degree. Red rings indicate a failure rate above 5%.
Self-loops on CALC, STAT, and PHYSED2 indicate re-enrollment.

The network is organized into three structural layers, as shown in
Figure 2. The color corresponds to these structural layers.

*4.3.1. Layer 1: Foundational and General Education (Red)*

These courses have a large out-degree relative to their in-degree,
serving as launch pads that propel students into many subsequent
courses. The dominant first-semester entries are MACRO (268 attempts,
out-degree 1,069) and ACCT (273 attempts, out-degree 1,022). Other
high-out-degree Layer 1 nodes include ARTS (out 1,012), HIST (out 957),
PHILO (out 907), and SPEECH (out 904). PRECALC (115 attempts) is a
non-credit bridge course; all recorded grades are P/F, INC, or DRP. ENG
is the only pure source node (in-degree = 0, out-degree = 7).

*4.3.2. Layer 2: Quantitative Bottleneck (Blue)*

CALC is the most consequential bottleneck node. It recorded 295 attempts
from 194 unique students, a 37.3% failure rate, an average grade of
3.56, and a self-loop weight of 71 with avg_grade_from = 4.94,
confirming that nearly all retakers had failed previously. CALC holds
the second-highest in-degree (1,181) and a very high out-degree (928).
It is simultaneously a major destination and a major source of
transitions.

STAT shows a parallel but less extreme pattern: 249 attempts from 212
students, a 13.2% failure rate, an average grade of 2.80, and a
self-loop weight of 21 with avg_grade_from = 4.85. ECON is a general
education subject with a moderate 4.9% failure rate across 185 attempts.
ACCT is the only hospitality course with a non-trivial failure rate:
4.0% from 273 attempts, average grade 2.09, self-loop weight 11.

*4.3.3. Layer 3: Hospitality Majors Convergence Sink (Green)*

Once students clear the quantitative bottleneck, the network converges
toward a dense cluster of hospitality subjects. MICRO receives the
highest in-degree of any non-PHYSED node at 1,106. Its 0.0% failure rate
and average grade of 1.35 indicate that students who reach MICRO perform
exceptionally well. Downstream, the network fans out into core
hospitality courses, all with 0.0% failure rates and grades clustering
between 1.0 and 1.7: ORM (138 students, avg 1.69), SERVQUAL (148, avg
1.25), NUTR, FCULT, PROC, ROOMS (84--87 students, avg 1.36--1.52), and
other courses (0.0--0.6% failure). PRACTICUM is the terminal course; 15
students are currently enrolled.

Figure 3.

*Hospitality Student Progression Flow (N = 269)*

![](media/image1.png){width="6.352744969378827in"
height="3.0474912510936134in"}

*Note.* The three-tier curriculum funnel from enrollment, through the
quantitative gate, to upper-division hospitality coursework and near
completion. Grey = not yet at quantitative gate (n ≈ 75); Red = retaking
CALC or STAT (n ≈ 23); Orange = pending next milestone; Green/Teal =
milestone cleared.

The Sankey diagram in Figure 3 visualizes how 269 hospitality students
progress through a three-tier funnel: from all enrolled students,
through the quantitative gate (CALC + STAT), to OR, then to the CUL+
series, and finally to near completion. It highlights three key flows:
students not yet at the quantitative gate; students stuck in
quantitative retakes (CALC/STAT); and students who have cleared ORM and
are either pending CUL+ or already near/at completion. The width of each
stream makes clear that the largest losses and delays occur at the
quantitative gate and just before CUL+, not in the upper-division core
itself.

*4.4. Comparative Network Parameters*

Table 8 presents computed graph-theoretic parameters for both networks
side by side. The contrast between the two columns is the quantitative
signature of the gap between curriculum design and actual student
navigation.

Table 8.

*Comparative Network Parameters---Structural vs. Empirical Networks*

  ------------------------------------------------------------------------
  **Parameter**                           **Structural**   **Empirical**
  --------------------------------------- ---------------- ---------------
  Nodes (N)                               49               56

  Edges (excl. self-loops)                36               1,621

  Self-loop edges                         0                12

  Graph density                           0.015            0.526

  Average degree (in = out)               0.74             28.95

  Max in-degree                           3                55

  Max out-degree                          8                53

  Weakly connected components             13               1

  Strongly connected components           49               2

  Largest WCC node count                  31               56

  Avg shortest path (largest WCC)         3.135            1.358

  Network diameter (largest WCC)          6                2

  Avg clustering coefficient              0.000            0.807

  Reciprocity                             0.000            0.780

  Is DAG?                                 Yes              No

  Longest prereq path (edges)             4                ---

  Source nodes (in-deg = 0)               16               1

  Sink nodes (out-deg = 0)                28               0

  Louvain communities                     9                3

  Modularity Q                            0.674            0.231
  ------------------------------------------------------------------------

*Note.* Density = E / \[N(N−1)\]. Shortest path and diameter are
computed on the undirected projection of the largest weakly connected
component. The node-count difference (49 vs. 56) arises because the
empirical network includes elective variants and alternative-slot
choices that appear in student records but not in the prerequisite
graph. Weighted parameters: avg. weighted degree = 408.4; max weighted
in-degree = 1,541 (PHYSED 2); max weighted out-degree = 1,679 (PHYSED
2).

Density exhibits the starkest contrast: the structural network's 0.015
indicates only 1.5% of potential directed links are official
prerequisites, whereas the empirical network's 0.526 shows over half of
possible transitions are observed, a 35-fold difference reflecting
students' behaviors like enrolling in multiple courses simultaneously,
repeating failed ones, and taking optional courses in flexible
sequences---connections not prescribed by the curriculum.

Degree statistics reinforce this: the structural network's average
degree of 0.74 suggests most courses have fewer than one prerequisite or
dependent, consistent with a sparse prerequisite tree, while the
empirical network's average degree of 28.95 shows each course connected
to nearly every other through observed transitions, with a maximum
in-degree of 3 (ORM) versus 55 (PHYSED 2). Shortest path length
decreases from 3.14 to 1.36, and diameter from 6 to 2, reflecting that
nearly any two courses are directly connected or separated by one course
in the empirical network. Clustering coefficient and reciprocity are
zero in the structural network but high (0.807 and 0.780) in the
empirical network, indicating co-enrollment and students moving back and
forth across semesters. Modularity drops from 0.674 to 0.231, indicating
blurred community boundaries and suggesting increased curriculum
friction, in which students cycle through lower-level courses rather
than progressing.

*4.5. Self-Loops (Retake Patterns)*

Twelve courses generated self-loop edges, meaning students returned to
take the same course in a later semester. The pattern is clear: CALC and
STAT generate mandatory failure-retake loops (average entry grade near
5.0), while PHYSED2 generates self-loops because it must be taken 4
times.

*4.6. Curriculum Flexibility*

The checklist includes several slash-alternative slots in which students
satisfy a requirement by choosing one of two or more designated courses.
Zuev & Stavrinides (2025) distinguish between conjunctive prerequisites
(all required) and disjunctive prerequisites (one of several
alternatives). The hospitality slash alternatives are disjunctive; each
was parsed separately and treated as a distinct node reflecting actual
enrollment.

Among the observed choices, SOCS attracted 100 students, compared with
77 for POLS. SCI was the overwhelming choice (191 students), compared
with RISK (7 students), reflecting disparities in section availability.
Hospitality electives follow a strict sequential pattern (Elective 1 → 2
→ 3). A cohort of off-season students took an elective ahead of schedule
but could not progress to the CUL series due to prerequisite
restrictions---specifically, failure to pass Math 21 on time. RIZAL
(Life and Works of Jose Rizal), mandated by Republic Act No. 1425, has
been completed by 59 students with a 0.0% failure rate. Overall, the
limited flexibility of alternatives offers few options for students
stuck at quantitative bottlenecks.

**5. Discussion and Implications**

*5.1. Discussion*

The weighted dual-network analysis reveals a three-tier curriculum
funnel: a broad general education and introductory hospitality
foundation layer that co-enrolls with dozens of courses and generates
dense early-semester transitions; a quantitative bottleneck (CALC and
STAT) that acts as a filter before OR; and a tightly convergent
upper-division core anchored by MICRO (in-degree 1,106, 0.0% failure
rate), flowing into specialization courses and the terminal practicum
cluster.

This three-tier structure maps onto the flux profile of Zuev &
Stavrinides (2025). Layer 1 corresponds to positive-flux strata that
emit more prerequisite links downstream than they receive---the
curriculum's knowledge-injection layer. Layer 2 represents the peak-flux
stratum, where the prerequisite concentration is highest, and failure
has the most downstream consequences. Layer 3 corresponds to
negative-flux strata that consume many prerequisites while producing
few---the terminal knowledge-absorption phase. This flux interpretation
elevates the three-tier model from descriptive observation to
theoretical characterization.

CALC's downstream impact is best understood through the reach metric
(Yang et al., 2024). CALC is an indirect prerequisite to the entire CUL
series and all subsequent major courses. Any student who fails faces two
consequences: delay in that single course and effective lockout from a
large portion of their degree for at least one additional semester. Yang
et al. found introductory mathematics bottlenecks most severe at the
largest institutions. The data we find fit this pattern precisely,
strengthening the generalizability of the hospitality findings across
different national and institutional contexts.

The most actionable signal is the CALC bottleneck. Targeted early
intervention---tutoring support and curricular scaffolding with Math
20---is the highest-leverage action. Another option is to allow students
who failed CALC to take ORM concurrently, with both courses required
before they can progress to the CUL series. Without this change, the
CALC self-loop continues indefinitely. All courses above MICRO have zero
failures, suggesting that once students clear the quantitative
prerequisites, they are well prepared to complete their major
requirements.

The comparative network analysis (Table 8) provides macro-level
quantification of curriculum friction. The modularity gap (0.674 vs.
0.231) reveals a design-reality gap: the curriculum is designed as
well-partitioned communities, but student progression blurs these
boundaries as failing students cycle back through lower-tier courses.
The 35-fold density contrast (0.015 vs. 0.526) confirms that students
are not following the prescribed linear path, largely due to the
CALC/STAT bottleneck, which is forcing a reorganization of the schedule.

We emphasize that network positions and failure rates identify
structurally high‑risk locations rather than prove causality; structural
risk (high reach, blocking factor) and performance risk (high failure
rates) should be read together, and any causal claims would require
additional qualitative work and predictive modeling using prior grades
or entry scores.

*5.2. Institutional Resource Impact of the CALC Bottleneck*

The third research objective was to quantify the impacts of failure
rates on institutional resources and student progress. Of the 194
students who have attempted CALC, only 171 have passed, leaving 23
students (11.9%) caught in mandatory retake cycles. The self-loop weight
of 71 means CALC has consumed approximately 71 additional
student-semester enrollment slots beyond its expected first-attempt
load.

The downstream cascade is severe. Each failed attempt at CALC delays
access to 16 downstream courses (reach = 17, including ORM itself) by at
least one semester. ORM has been offered every semester since
2022---twice per year rather than once---specifically to accommodate
students delayed by failures in CALC and STAT. This constitutes at least
three additional off-schedule section offerings over four academic
years, each requiring faculty allocation, classroom assignment, and
administrative scheduling outside the standard calendar.

With enrollment nearly quadrupling between 2021 and 2025, this
structural pressure is not temporary but a recurring cost embedded in
the current prerequisite architecture. The network analysis confirms
that no alternative pathway exists: CALC has a blocking factor of 1 and
a reach of 17, with no redundant route bypassing this chokepoint.

The universality of this pattern is supported by Yang et al. (2024), who
found introductory mathematics courses achieved the highest betweenness
centrality and reach values across all six institutional CPNs studied,
from CalTech's 771-node network to UIUC's 5,126-node network. The
hospitality finding extends this structural regularity to a non-STEM,
service-sector professional program in the ASEAN region. In Zuev &
Stavrinides's (2025) flux framework, the stratum containing CALC would
exhibit anomalously high positive flux---it emits far more prerequisite
links downstream than it receives---making it the most consequential
leverage point for curricular intervention.

*5.3. Academic and Practical Implications*

This study will inform curriculum review and future revisions. It aligns
with ASEAN University Network Quality Assurance (AUN-QA) standards,
under which the program was certified in 2023. These findings are
actionable and consistent with Basavaraj et al. (2022), who demonstrated
that network-based curricular analytics inform academic advising
strategies by identifying which courses require additional support and
which student sub-populations need targeted intervention.

For the said hospitality program, this translates to actionable advising
protocols. Flag students who have not cleared CALC or STAT by the end of
their second semester. These students are at elevated risk of
multi-semester delays. Early and proactive advising prevents the
prerequisite trap from compounding.

*5.4. Limitations and Suggestions for Future Research*

This study has important limitations. It is limited to a single
institution and includes only currently enrolled students. Graduates and
students who have left the program were excluded, introducing
survivorship bias. Students who attempted CALC multiple times and
ultimately withdrew are not represented in the N = 269 dataset. All
reported course-level failure rates are therefore conservative
lower-bound estimates; the actual proportion unable to clear the
quantitative bottleneck is likely higher.

Future research should incorporate full cohort records, including
withdrawn students, to obtain unbiased estimates of attrition.
Qualitative interviews with students who dropped or failed would
illuminate root causes---academic difficulty, scheduling conflicts, or
both. Comparative studies with other hospitality curricula or
hospitality management programs in the Philippines and broader ASEAN
region would help determine whether this bottleneck is
institution-specific or reflects systemic patterns in hospitality
education.

**6. Conclusion**

This dual-network analysis reveals a substantial design--reality gap
between the sparse, hierarchical prerequisite structure of the
hospitality curriculum and the dense, highly clustered empirical
progression network generated by actual student trajectories. In
particular, CALC and ORM form a quantitative gate that concentrates
structural and performance risk and amplifies delays for large cohorts.

For practitioners and policymakers, the main implications are to (1)
prioritize early support and capacity planning for quantitative
gatekeeping courses, (2) review the reliance on a single, linear
quantitative chain in light of hospitality competency and accreditation
frameworks, and (3) adopt curriculum network analytics as a routine tool
for monitoring progression and evaluating proposed reforms before
full-scale implementation.

**References**

Aldrich, P. R. (2015). The curriculum prerequisite network: Modeling the
curriculum as a complex system. *Biochemistry and Molecular Biology
Education*, *43*(3), 168--180. https://doi.org/10.1002/bmb.20861

Basavaraj, P., Garibay, I., & Ozmen Garibay, O. (2022). Pathway patterns
mobility study of first time vs. Transfer students in computer science
and information technology programs at a public university. *Journal of
Applied Research in Higher Education*, *14*(2), 784--807.
https://doi.org/10.1108/JARHE-12-2020-0429

Blondel, V. D., Guillaume, J.-L., Lambiotte, R., & Lefebvre, E. (2008).
Fast unfolding of communities in large networks. *Journal of Statistical
Mechanics: Theory and Experiment*, *2008*(10), P10008.
https://doi.org/10.1088/1742-5468/2008/10/P10008

Conijn, R., Snijders, C., Kleingeld, A., & Matzat, U. (2017). Predicting
Student Performance from LMS Data: A Comparison of 17 Blended Courses
Using Moodle LMS. *IEEE Transactions on Learning Technologies*, *10*(1),
17--29. https://doi.org/10.1109/TLT.2016.2616312

Cullen, T. P., & Lambert, C. U. (1987). Teaching Quantitative Decision
Skills in a Hospitality Curriculum. *Cornell Hotel and Restaurant
Administration Quarterly*, *28*(2), 42--45.
https://doi.org/10.1177/001088048702800215

EDCOM 2. (2026, February 14). CHED curriculum updates take 11 years on
average. *EDCOM 2*.
https://edcom2.gov.ph/ched-curriculum-updates-take-11-years-on-average/

Fei, A., Chen, J., Lee, W., Xin, K., Behnke, C., & Gordon, S. (2025).
Designing Hospitality Curriculum for the Future: A Comprehensive
Assessment of an Undergraduate Program in the United States. *Journal of
Hospitality & Tourism Education*, *37*(2), 138--153.
https://doi.org/10.1080/10963758.2025.2453736

Hagberg, A. A., Schult, D. A., & Swart, P. J. (2008). *Exploring Network
Structure, Dynamics, and Function using NetworkX*. 11--15.
https://doi.org/10.25080/TCWV9851

Heileman, G. L., Thompson-Arjona, W. G., Abar, O., & Free, H. W. (2019,
June 15). *Does Curricular Complexity Imply Program Quality?* 2019 ASEE
Annual Conference & Exposition.
https://peer.asee.org/does-curricular-complexity-imply-program-quality

Jacomy, M., Venturini, T., Heymann, S., & Bastian, M. (2014).
ForceAtlas2, a Continuous Graph Layout Algorithm for Handy Network
Visualization Designed for the Gephi Software. *PLoS ONE*, *9*(6),
e98679. https://doi.org/10.1371/journal.pone.0098679

Newman, M. E. J., & Girvan, M. (2004). Finding and evaluating community
structure in networks. *Physical Review E*, *69*(2), 026113.
https://doi.org/10.1103/PhysRevE.69.026113

Rienties, B., & Toetenel, L. (2016). The impact of learning design on
student behaviour, satisfaction and performance: A cross-institutional
comparison across 151 modules. *Computers in Human Behavior*, *60*,
333--341. https://doi.org/10.1016/j.chb.2016.02.074

Roxas, R. M., & Tapang, G. (2010). Prose and poetry classification and
boundary detection using word adjacency network analysis. *International
Journal of Modern Physics C*, *21*(04), 503--512.

Slim, A., Heileman, G. L., Kozlick, J., & Abdallah, C. T. (2014).
Predicting student success based on prior performance. *2014 IEEE
Symposium on Computational Intelligence and Data Mining (CIDM)*,
410--415. https://doi.org/10.1109/CIDM.2014.7008697

Wang, J., & Abukhalifeh, A. N. M. (2021). Evaluating Undergraduate
Curriculum in Hospitality Management: A Comparison between China and
South Korea. *Journal of China Tourism Research*, *17*(4), 613--633.
https://doi.org/10.1080/19388160.2020.1788684

Yang, B., Gharebhaygloo, M., Rondi, H. R., Hortis, E., Lostalo, E. Z.,
Huang, X., & Ercal, G. (2024). Comparative analysis of course
prerequisite networks for five Midwestern public institutions. *Applied
Network Science*, *9*(1), 25. https://doi.org/10.1007/s41109-024-00637-z

Zuev, K. M., & Stavrinides, P. (2025). Breadth, depth, and flux of
course-prerequisite networks. *Network Science*, *13*, e17.
https://doi.org/10.1017/nws.2025.10013
