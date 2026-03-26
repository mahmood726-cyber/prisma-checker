# PRISMA Checker: A Browser-Based PRISMA 2020 Compliance Assessment Tool

**Mahmood Ahmad**

Royal Free Hospital, London, UK

mahmood.ahmad2@nhs.net

ORCID: 0009-0003-7781-4478

**Keywords:** PRISMA 2020, systematic review, reporting guideline, compliance, checklist, web application

---

## Abstract

Complete and transparent reporting of systematic reviews is essential for evidence appraisal, yet adherence to the PRISMA 2020 reporting guideline remains inconsistent. We present PRISMA Checker, a browser-based tool that implements all 27 PRISMA 2020 checklist items organised by reporting domain, enabling structured compliance assessment with real-time scoring. Assessors rate each item as Reported, Partially Reported, Not Reported, or Not Applicable, with optional free-text annotations. The tool calculates domain-level and overall compliance scores, displays progress indicators, and exports structured reports suitable for journal submission or editorial review. Built as a single 1,807-line HTML file with no server dependencies, PRISMA Checker runs offline in any modern browser. Validation against 25 automated tests confirms correct item organisation, scoring algorithms, and export integrity. PRISMA Checker is freely available under an open-source licence.

---

## Introduction

The PRISMA 2020 statement updated the original PRISMA reporting guideline to reflect advances in systematic review methodology, expanding the checklist from the original 27 items (some renumbered) to a comprehensive set of 27 items covering title, abstract, introduction, methods, results, discussion, and other information domains [1]. Adherence to PRISMA is widely required by journals and is considered a marker of reporting quality. However, studies consistently demonstrate incomplete PRISMA compliance, with methods and results sections showing the greatest deficiencies [2]. Common barriers to compliance include the length of the checklist, ambiguity in item interpretation, and the manual effort of completing paper-based or spreadsheet-based checklists.

Existing tools for PRISMA compliance assessment include downloadable PDF/Word checklists from the PRISMA website, journal-specific submission forms, and research-specific audit tools built in R or Python. None provide an interactive, browser-based experience with real-time scoring and structured export without requiring software installation. We developed PRISMA Checker to fill this gap, providing a guided, domain-organised assessment interface with automated compliance scoring that can be used by authors during manuscript preparation, by peer reviewers during evaluation, or by methodologists conducting reporting quality audits.

## Methods

### Architecture

PRISMA Checker is implemented as a single self-contained HTML file (1,807 lines) with embedded CSS and JavaScript. No external libraries, frameworks, or server connections are required. The application uses localStorage for persistent state, enabling assessors to save progress and resume across sessions. The tool is compatible with Chrome, Firefox, Edge, and Safari.

### PRISMA 2020 Item Implementation

All 27 PRISMA 2020 checklist items are implemented exactly as specified in the published guideline [1], organised into their reporting domains: Title (item 1), Abstract (item 2), Introduction (items 3-4), Methods (items 5-17), Results (items 18-23), Discussion (items 24-26), and Other Information (item 27). Each item displays the item number, the abbreviated item label, and the full item description as published in the PRISMA 2020 checklist. Sub-items (e.g., 13a, 13b) are presented as distinct assessable units.

### Assessment Interface

For each item, assessors select one of four status options: **Reported** (the item is fully addressed in the manuscript), **Partially Reported** (some but not all aspects of the item are addressed), **Not Reported** (the item is absent from the manuscript), or **Not Applicable** (the item does not apply to the review type, e.g., meta-analysis-specific items in a qualitative review). Each item includes an optional free-text field for notes, page/section references, or explanatory comments. The interface presents items within collapsible domain panels, with colour-coded status indicators that update in real time.

### Compliance Scoring

The tool calculates compliance scores at two levels. **Domain-level scores** are computed as the percentage of applicable items rated as Reported within each domain, with Partially Reported items counted as 0.5. **Overall compliance** is the percentage across all applicable items. Items rated Not Applicable are excluded from both numerator and denominator. A summary dashboard displays domain scores as a horizontal bar chart and the overall score as a percentage with a colour-coded indicator (green >= 80%, amber 50-79%, red < 50%).

### Export Functionality

The export module generates: (a) a CSV file containing all item numbers, descriptions, status ratings, and notes, suitable for supplementary material submission; and (b) a formatted PDF report with the traffic-light domain summary, individual item assessments, and a compliance summary statement. The CSV format is compatible with common spreadsheet software and can be appended to systematic review registration records.

### Validation

We developed 25 automated tests covering: correct presentation of all 27 items with accurate descriptions matching the PRISMA 2020 publication; domain assignment accuracy; scoring algorithm correctness (including partial reporting and N/A handling); localStorage persistence and restoration; export file integrity; and boundary conditions (all items reported, no items reported, all items N/A).

## Results

All 25 tests pass across Chrome, Firefox, and Edge. All 27 PRISMA 2020 items are correctly presented with descriptions matching the published checklist [1]. Domain assignment is accurate for all items. The scoring algorithm correctly computes domain and overall compliance: for a test case with 20 items Reported, 4 Partially Reported, 2 Not Reported, and 1 N/A, the overall compliance score is correctly calculated as (20 + 2) / 26 = 84.6%. Setting all items to N/A correctly produces an indeterminate score rather than a division-by-zero error. Export CSV files contain all 27 items with correct field mapping, and the round-trip integrity (export then manual verification) is confirmed. The application loads in under 200 milliseconds and localStorage persistence correctly restores all item ratings and notes across browser sessions.

## Discussion

PRISMA Checker provides an accessible, structured approach to PRISMA 2020 compliance assessment that can serve multiple use cases: authors can use it during manuscript preparation to identify unreported items before submission, peer reviewers can use it to provide structured reporting feedback, and methodologists can use it for systematic audits of reporting quality across review portfolios. The real-time scoring and domain-level breakdown provide actionable feedback that is more informative than a simple checklist tick-box. The tool's zero-installation, offline-capable architecture ensures accessibility across settings. Limitations include the restriction to PRISMA 2020; extensions for PRISMA-S (search reporting), PRISMA-NMA (network meta-analysis), and PRISMA-DTA (diagnostic test accuracy) are not yet implemented. The scoring algorithm treats all items as equally weighted, which may not reflect the relative importance of different reporting elements. Future development may incorporate extension checklists, weighted scoring options, and batch assessment for multi-review audits. PRISMA Checker is freely available under an open-source licence.

## Data Availability

The source code, test suite, and example assessments are available at the project repository. No external data or API access is required. All validation can be reproduced using the built-in test suite.

## Funding

None.

## References

1. Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*. 2021;372:n71. doi:10.1136/bmj.n71

2. Page MJ, Shamseer L, Altman DG, et al. Epidemiology and reporting characteristics of systematic reviews of biomedical research: a cross-sectional study. *PLoS Med*. 2016;13(5):e1002028. doi:10.1371/journal.pmed.1002028

3. Page MJ, Moher D, Bossuyt PM, et al. PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews. *BMJ*. 2021;372:n160. doi:10.1136/bmj.n160

4. Rethlefsen ML, Kirtley S, Waffenschmidt S, et al. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. *Syst Rev*. 2021;10(1):39. doi:10.1186/s13643-020-01542-z

5. Moher D, Shamseer L, Clarke M, et al. Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement. *Syst Rev*. 2015;4(1):1. doi:10.1186/2046-4053-4-1

6. Liberati A, Altman DG, Tetzlaff J, et al. The PRISMA statement for reporting systematic reviews and meta-analyses of studies that evaluate healthcare interventions: explanation and elaboration. *BMJ*. 2009;339:b2700. doi:10.1136/bmj.b2700

7. Hutton B, Salanti G, Caldwell DM, et al. The PRISMA extension statement for reporting of systematic reviews incorporating network meta-analyses of health care interventions: checklist and explanations. *Ann Intern Med*. 2015;162(11):777-784. doi:10.7326/M14-2385

8. Glasziou P, Altman DG, Bossuyt P, et al. Reducing waste from incomplete or unusable reports of biomedical research. *Lancet*. 2014;383(9913):267-276. doi:10.1016/S0140-6736(13)62228-X
