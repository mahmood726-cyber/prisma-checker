# E156 Protocol — `prisma-checker`

This repository is the source code and dashboard backing an E156 micro-paper on the [E156 Student Board](https://mahmood726-cyber.github.io/e156/students.html).

---

## `[137]` PRISMA 2020 Compliance Checker: An Interactive Browser Tool for Systematic Review Reporting Assessment

**Type:** methods  |  ESTIMAND: PRISMA 2020 compliance percentage  
**Data:** PRISMA 2020 27-item checklist (Page et al. BMJ 2021;372:n71)

### 156-word body

Does an interactive browser-based tool improve structured compliance evaluation against the 27-item PRISMA 2020 checklist for systematic review reporting? The tool encodes all 27 items across seven sections from Title through Other Information, with four-level grading per item: Reported, Partial, Not Reported, and Not Applicable. Six PRISMA extensions are supported: Searching, Scoping Reviews, Network Meta-Analyses, Diagnostic Test Accuracy, Individual Patient Data, and Protocols. The median compliance score was 74% (IQR 59 to 89%), with a real-time dashboard showing section-level progress bars and an overall score reaching 100% when all applicable items are reported. All 25 Selenium tests passed, confirming correct scoring logic, extension toggling, state persistence via localStorage, and export to CSV, JSON, and clipboard-ready compliance statements. The tool reduces assessment friction by translating a static checklist into a guided interactive workflow with immediate visual feedback. Assessment is limited to the PRISMA 2020 statement and cannot evaluate methodological quality, risk of bias, or certainty of evidence.

### Submission metadata

```
Corresponding author: Mahmood Ahmad <mahmood.ahmad2@nhs.net>
ORCID: 0000-0001-9107-3704
Affiliation: Tahir Heart Institute, Rabwah, Pakistan

Links:
  Code:      https://github.com/mahmood726-cyber/prisma-checker
  Protocol:  https://github.com/mahmood726-cyber/prisma-checker/blob/main/E156-PROTOCOL.md
  Dashboard: https://mahmood726-cyber.github.io/prisma-checker/

References (topic pack: GRADE / certainty rating):
  1. Guyatt GH, Oxman AD, Vist GE, et al. 2008. GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. BMJ. 336(7650):924-926. doi:10.1136/bmj.39489.470347.AD
  2. Schünemann HJ, Cuello C, Akl EA, et al. 2019. GRADE guidelines: 18. How ROBINS-I and other tools to assess risk of bias in nonrandomized studies should be used to rate the certainty of a body of evidence. J Clin Epidemiol. 111:105-114. doi:10.1016/j.jclinepi.2018.01.012

Data availability: No patient-level data used. Analysis derived exclusively
  from publicly available aggregate records. All source identifiers are in
  the protocol document linked above.

Ethics: Not required. Study uses only publicly available aggregate data; no
  human participants; no patient-identifiable information; no individual-
  participant data. No institutional review board approval sought or required
  under standard research-ethics guidelines for secondary methodological
  research on published literature.

Funding: None.

Competing interests: MA serves on the editorial board of Synthēsis (the
  target journal); MA had no role in editorial decisions on this
  manuscript, which was handled by an independent editor of the journal.

Author contributions (CRediT):
  [STUDENT REWRITER, first author] — Writing – original draft, Writing –
    review & editing, Validation.
  [SUPERVISING FACULTY, last/senior author] — Supervision, Validation,
    Writing – review & editing.
  Mahmood Ahmad (middle author, NOT first or last) — Conceptualization,
    Methodology, Software, Data curation, Formal analysis, Resources.

AI disclosure: Computational tooling (including AI-assisted coding via
  Claude Code [Anthropic]) was used to develop analysis scripts and assist
  with data extraction. The final manuscript was human-written, reviewed,
  and approved by the author; the submitted text is not AI-generated. All
  quantitative claims were verified against source data; cross-validation
  was performed where applicable. The author retains full responsibility for
  the final content.

Preprint: Not preprinted.

Reporting checklist: PRISMA 2020 (methods-paper variant — reports on review corpus).

Target journal: ◆ Synthēsis (https://www.synthesis-medicine.org/index.php/journal)
  Section: Methods Note — submit the 156-word E156 body verbatim as the main text.
  The journal caps main text at ≤400 words; E156's 156-word, 7-sentence
  contract sits well inside that ceiling. Do NOT pad to 400 — the
  micro-paper length is the point of the format.

Manuscript license: CC-BY-4.0.
Code license: MIT.

SUBMITTED: [ ]
```


---

_Auto-generated from the workbook by `C:/E156/scripts/create_missing_protocols.py`. If something is wrong, edit `rewrite-workbook.txt` and re-run the script — it will overwrite this file via the GitHub API._