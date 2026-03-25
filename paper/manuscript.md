# PRISMA 2020 Compliance Checker: An Interactive Web-Based Tool for Assessing Systematic Review Reporting

[AUTHOR_PLACEHOLDER]^1, [AUTHOR_PLACEHOLDER]^2, [AUTHOR_PLACEHOLDER]^3

^1 [AFFILIATION_PLACEHOLDER]
^2 [AFFILIATION_PLACEHOLDER]
^3 [AFFILIATION_PLACEHOLDER]

**Corresponding author:** [AUTHOR_PLACEHOLDER], [EMAIL_PLACEHOLDER]

**Word count:** ~2,500

**Target journal:** Systematic Reviews (BMC) / BMJ Open

---

## Abstract

**Background:** The Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 statement is the mandatory reporting guideline for systematic reviews. Despite widespread journal endorsement, compliance remains poor, with empirical studies consistently showing that 30--60% of PRISMA items go unreported. Existing compliance assessment tools are limited to static paper checklists and spreadsheets, which offer no real-time feedback, no structured export, and no guidance during the assessment process.

**Objective:** To develop and describe an open-access, interactive web-based tool that enables authors, peer reviewers, and editors to systematically assess and document compliance with the 27-item PRISMA 2020 checklist.

**Methods:** The PRISMA 2020 Compliance Checker was implemented as a single-file HTML application requiring no installation, server infrastructure, or user accounts. It encodes all 27 PRISMA 2020 items across seven sections with four status levels (Reported, Partially reported, Not reported, Not applicable), and supports page references, free-text notes, six PRISMA extensions, real-time dashboard analytics, and multi-format export.

**Results:** The tool provides a structured, item-by-item walkthrough of the PRISMA 2020 checklist with immediate visual feedback. A dashboard displays overall compliance scores, section-level progress bars, and an auto-generated compliance statement suitable for inclusion in manuscripts. Export options include CSV, JSON, clipboard text, and print-ready summaries. Assessment state persists automatically via browser local storage.

**Conclusions:** The PRISMA 2020 Compliance Checker fills a gap in the reporting guideline ecosystem by translating the static PRISMA 2020 checklist into an interactive, self-contained assessment tool. It may support adoption of the PRISMA 2020 statement by reducing the friction of compliance assessment for authors, reviewers, and editorial offices.

**Keywords:** PRISMA 2020, systematic review, reporting guideline, compliance assessment, web application, open access

---

## Background

Systematic reviews are foundational to evidence-based medicine, clinical guideline development, and health technology assessment. The quality and utility of a systematic review depend critically on the transparency and completeness of its reporting. The Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) statement, originally published in 2009 [1], was updated in 2020 to reflect advances in systematic review methodology [2]. The PRISMA 2020 statement comprises 27 checklist items organized across seven sections --- Title, Abstract, Introduction, Methods, Results, Discussion, and Other Information --- with an accompanying explanation and elaboration document [3].

PRISMA 2020 is endorsed by hundreds of journals and is a requirement for systematic review submissions at most major biomedical publishers [2]. Despite this endorsement, empirical assessments of reporting quality consistently reveal suboptimal compliance. Studies across clinical disciplines have found that 30--60% of PRISMA items are inadequately reported, with particularly poor adherence for items related to protocol registration, search strategy transparency, risk of bias due to missing results, and certainty of evidence assessment [4,5]. A recent cross-sectional analysis of systematic reviews published in high-impact journals found that fewer than 40% fully reported all Methods items, and only 25% provided complete information on synthesis methods [5].

The persistence of incomplete reporting, despite widespread guideline endorsement, suggests that awareness alone is insufficient. Authors face practical barriers: the PRISMA 2020 checklist is a static document (typically a PDF or Word table) that provides no interactive guidance, no real-time feedback on progress, and no structured mechanism for documenting where each item is addressed in the manuscript. Peer reviewers and editors, who are responsible for enforcing compliance, must manually cross-reference the checklist against the manuscript --- a time-consuming process that is difficult to standardize. Existing digital tools in the reporting guideline space include the PRISMA Flow Diagram Generator [6] and various journal-specific submission checklists, but no freely available interactive tool exists for conducting and documenting a structured PRISMA 2020 compliance assessment.

This paper describes the PRISMA 2020 Compliance Checker, an open-access, browser-based application that translates the 27-item PRISMA 2020 checklist into an interactive assessment tool with real-time analytics, structured documentation, and multi-format export capabilities.

## Implementation

### Design principles

The tool was designed with three guiding principles: (1) zero-barrier access --- no installation, server, login, or internet connection required after initial page load; (2) fidelity to the PRISMA 2020 statement --- item numbers, titles, and descriptions reproduce the published checklist verbatim [2]; and (3) structured output --- all assessment data can be exported in machine-readable formats for audit trails and reproducibility.

### Technical architecture

The PRISMA 2020 Compliance Checker is implemented as a single self-contained HTML file (1,808 lines) incorporating all markup, styles, and application logic. This architecture eliminates external dependencies, simplifies distribution, and allows the tool to function entirely offline. The application uses vanilla JavaScript within an immediately-invoked function expression (IIFE), with no external libraries or frameworks. It is compatible with all modern browsers (Chrome, Firefox, Safari, Edge) on desktop and mobile devices. The interface supports both dark and light display themes and is fully responsive.

### Data model

The checklist data model encodes the 27 PRISMA 2020 items, each identified by number (1--27), title, and full description text drawn from the PRISMA 2020 statement [2]. Items are organized into seven sections: Title (item 1), Abstract (item 2), Introduction (items 3--4), Methods (items 5--16), Results (items 17--23), Discussion (items 24--26), and Other Information (item 27).

Each item supports four mutually exclusive status levels:

- **Reported**: The item is fully and adequately reported in the manuscript.
- **Partially reported**: Some elements of the item are present but the reporting is incomplete.
- **Not reported**: The item is not addressed in the manuscript.
- **Not applicable (N/A)**: The item does not apply to the review type (e.g., meta-analysis items for a qualitative synthesis).

In addition, each item includes a free-text field for recording the manuscript page number or section where the item is addressed, and a notes field for assessor comments or justifications.

### Compliance scoring

The overall compliance score is computed as:

> Compliance (%) = (Items Reported + Items N/A) / 27 x 100

This formula treats fully reported items and legitimately not-applicable items equivalently, consistent with the principle that N/A items should not penalize the compliance score. Partially reported items are not counted toward compliance, reflecting the PRISMA 2020 expectation of complete reporting for each item.

### Feature set

The application is organized into four tabbed panels accessible via a sticky navigation bar:

**Checklist panel.** The primary assessment interface presents all 27 items as interactive cards grouped by section. Each card displays the item number, title, and full PRISMA 2020 description. Assessors select one of the four status levels via radio buttons, which triggers immediate visual feedback: the card's left border changes colour to reflect the selected status (green for Reported, amber for Partially reported, red for Not reported, grey for N/A). Section headers display real-time progress counts (e.g., "8/12 assessed" for Methods).

**Dashboard panel.** A summary analytics view provides: (a) an animated circular gauge displaying the overall compliance percentage with colour coding (green above 80%, amber 50--79%, red below 50%); (b) a status breakdown showing counts for each status category; (c) section-by-section horizontal progress bars; (d) a list of items needing attention (those marked Partially reported or Not reported); and (e) an auto-generated compliance statement suitable for direct inclusion in the Methods or supplementary material of a manuscript. The compliance statement is formatted as a structured paragraph summarizing the assessment outcome and can be copied to the clipboard with a single click.

**Extensions panel.** The tool supports six PRISMA extensions, each presented as an expandable card with extension-specific checklist items:

1. **PRISMA-S** (PRISMA for Searching): 16 items covering database naming, search strategy documentation, peer review of searches, and deduplication [7].
2. **PRISMA-ScR** (PRISMA for Scoping Reviews): 6 items addressing scoping review-specific reporting requirements [8].
3. **PRISMA-NMA** (PRISMA for Network Meta-Analyses): 8 items for network geometry, transitivity, inconsistency, and treatment rankings.
4. **PRISMA-DTA** (PRISMA for Diagnostic Test Accuracy): 7 items for index tests, reference standards, thresholds, and QUADAS assessments.
5. **PRISMA-IPD** (PRISMA for Individual Patient Data): 7 items for IPD acquisition, integrity checks, and participant-level analyses.
6. **PRISMA-P** (PRISMA for Protocols): 8 items for protocol registration, planned methods, and amendments.

Extension items use binary checkboxes (completed/not completed) rather than the four-level status system, reflecting their supplementary nature.

**Export panel.** Four export mechanisms are provided: (a) CSV download, producing a spreadsheet with columns for item number, section, title, status, page reference, and notes; (b) JSON download, generating a structured data file including compliance scores, all item assessments, and active extension data; (c) clipboard copy, producing a formatted plain-text checklist with status indicators; and (d) print summary, activating browser print with a print-optimized stylesheet.

### Data persistence

All assessment data are automatically saved to the browser's localStorage after each user interaction, keyed under `prismachecker-data`. This allows assessors to close and reopen the tool without data loss, resume assessments across sessions, and work without any network connectivity. The Reset All function clears all saved data after user confirmation.

## Use case example

To illustrate the tool's workflow, consider an author preparing to submit a systematic review of randomised controlled trials. The author opens the PRISMA 2020 Compliance Checker in their browser and proceeds item by item through the checklist panel. For Item 1 (Title), the author verifies that the manuscript title identifies the report as a systematic review and selects "Reported," entering "p. 1" in the page reference field. For Item 7 (Search strategy), the author finds that only two of three database search strategies are included in the appendix and selects "Partially reported," adding a note: "CINAHL strategy missing from Appendix 1." For Item 15 (Certainty assessment), the author realizes that no GRADE assessment was performed and selects "Not reported."

After assessing all 27 items, the author navigates to the Dashboard panel. The compliance gauge displays 78%, with 21 items reported, 2 not applicable, 3 partially reported, and 1 not reported. The attention list highlights the three partially reported and one not-reported items. The author uses the auto-generated compliance statement to draft the PRISMA reporting section of the manuscript and copies it to the clipboard. The author also enables the PRISMA-S extension, as the review includes a comprehensive search methodology section, and documents compliance with the 16 search-specific items.

Before submission, the author exports the complete assessment as a JSON file to include as supplementary material, providing the editorial office with a machine-readable compliance record.

## Discussion

### Contribution to reporting quality improvement

The PRISMA 2020 Compliance Checker addresses a recognized gap in the reporting guideline implementation ecosystem. The EQUATOR (Enhancing the QUAlity and Transparency Of health Research) Network has long advocated for tools that facilitate guideline adoption rather than merely disseminating guideline documents [9]. The present tool operationalizes this principle by converting the passive act of reading a checklist into an active, structured assessment process with immediate feedback.

Several features of the tool directly address known barriers to compliance. First, the item-by-item walkthrough with full descriptions reduces the cognitive burden of remembering what each item requires. Second, the real-time compliance score creates a quantifiable target that may motivate more thorough reporting. Third, the auto-generated compliance statement reduces the effort required to document adherence, which journals increasingly request. Fourth, the export capabilities create an audit trail that supports editorial verification.

### Integration with editorial workflows

The tool's structured export formats (particularly JSON) make it suitable for integration into journal submission workflows. Editorial offices could request that authors submit a PRISMA 2020 Compliance Checker export alongside their manuscript, analogous to the PRISMA flow diagram that many journals already require. The JSON format is machine-parseable, enabling automated screening of compliance levels prior to peer review. For peer reviewers, the tool provides a systematic framework for evaluating reporting completeness that is more efficient than ad hoc checklist review.

### Comparison with existing tools

Several related tools exist in the reporting guideline space, though none directly replicate the functionality described here. The PRISMA Flow Diagram Generator [6] focuses exclusively on producing the PRISMA flow diagram and does not assess checklist compliance. The EQUATOR Network's Reporting Guideline Selector helps authors identify applicable guidelines but does not provide interactive assessment [9]. Journal-specific submission checklists (e.g., those used by The BMJ and The Lancet) are proprietary, non-interactive, and limited to a single journal's requirements. Spreadsheet-based checklists circulated informally in the community offer basic tracking but lack real-time analytics, structured export, and persistent state management.

The PRISMA 2020 Compliance Checker is, to our knowledge, the first freely available, zero-dependency web tool that combines the complete 27-item checklist with interactive status tracking, quantitative compliance scoring, extension support, auto-generated compliance statements, and multi-format export.

### Limitations

Several limitations should be acknowledged. First, the tool is a self-assessment instrument: it facilitates and documents the compliance evaluation process but does not verify the accuracy or quality of reported information. An author can mark an item as "Reported" without the tool verifying that the corresponding manuscript text is adequate. Automated content verification using natural language processing remains a direction for future development. Second, the compliance score treats all 27 items equally, whereas some items (e.g., synthesis methods, risk of bias) may carry greater importance for interpretive validity. Weighted scoring schemes could be explored in future versions. Third, the tool currently operates as a standalone application; integration with manuscript preparation systems (e.g., Overleaf, institutional repositories) or submission platforms would enhance adoption. Fourth, while the tool includes six PRISMA extensions, additional extensions may be published as the PRISMA family grows. The single-file architecture simplifies updates but requires manual redistribution.

### Future directions

Planned enhancements include: (a) integration of the PRISMA 2020 flow diagram as an interactive companion module; (b) multi-reviewer mode allowing two or more assessors to independently evaluate the same manuscript and compare results; (c) longitudinal tracking to compare compliance across successive revisions; and (d) exploration of large language model-assisted pre-screening, where manuscript text is analyzed to suggest probable status levels for each item, subject to human confirmation.

## Conclusions

The PRISMA 2020 Compliance Checker is an open-access, self-contained web application that translates the 27-item PRISMA 2020 checklist into an interactive assessment tool. By providing structured item-by-item evaluation, real-time compliance analytics, extension support for six PRISMA derivatives, and multi-format export, the tool reduces the friction of compliance assessment for systematic review authors, peer reviewers, and editorial offices. It is freely available, requires no installation or registration, and operates entirely within the browser. We believe this tool can contribute to improving the completeness and transparency of systematic review reporting.

## Availability and requirements

- **Project name:** PRISMA 2020 Compliance Checker
- **Operating system(s):** Platform independent (browser-based)
- **Programming language:** HTML5, CSS3, JavaScript (ES5+)
- **Other requirements:** Any modern web browser (Chrome, Firefox, Safari, Edge)
- **License:** [LICENSE_PLACEHOLDER]
- **Source code:** [URL_PLACEHOLDER]

## Abbreviations

EQUATOR, Enhancing the QUAlity and Transparency Of health Research; GRADE, Grading of Recommendations Assessment, Development and Evaluation; IPD, individual patient data; NMA, network meta-analysis; DTA, diagnostic test accuracy; PRISMA, Preferred Reporting Items for Systematic Reviews and Meta-Analyses; QUADAS, Quality Assessment of Diagnostic Accuracy Studies; ScR, scoping review.

## Declarations

**Ethics approval and consent to participate:** Not applicable. This study describes a software tool and involves no human participants.

**Consent for publication:** Not applicable.

**Availability of data and materials:** The PRISMA 2020 Compliance Checker is a single HTML file available at [URL_PLACEHOLDER]. No external data are required.

**Competing interests:** [COMPETING_INTERESTS_PLACEHOLDER]

**Funding:** [FUNDING_PLACEHOLDER]

**Authors' contributions:** [CONTRIBUTIONS_PLACEHOLDER]

**Acknowledgements:** [ACKNOWLEDGEMENTS_PLACEHOLDER]

## References

1. Moher D, Liberati A, Tetzlaff J, Altman DG; PRISMA Group. Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statement. BMJ. 2009;339:b2535. doi:10.1136/bmj.b2535

2. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71. doi:10.1136/bmj.n71

3. Page MJ, Moher D, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews. BMJ. 2021;372:n160. doi:10.1136/bmj.n160

4. Page MJ, Shamseer L, Altman DG, Tetzlaff J, Sampson M, Tricco AC, et al. Epidemiology and reporting characteristics of systematic reviews of biomedical research: a cross-sectional study. PLoS Med. 2016;13(5):e1002028. doi:10.1371/journal.pmed.1002028

5. Gates M, Gates A, Pieper D, Fernandes RM, Tricco AC, Moher D, et al. Reporting guideline compliance in systematic reviews of clinical interventions published in high-impact journals. Res Synth Methods. 2022;13(2):155--167. doi:10.1002/jrsm.1537

6. Haddaway NR, Page MJ, Pritchard CC, McGuinness LA. PRISMA2020: an R package and Shiny app for producing PRISMA 2020-compliant flow diagrams, with interactivity for optimised digital transparency and open synthesis. Campbell Syst Rev. 2022;18(2):e1230. doi:10.1002/cl2.1230

7. Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, et al. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. Syst Rev. 2021;10(1):39. doi:10.1186/s13643-020-01542-z

8. Tricco AC, Lillie E, Zarin W, O'Brien KK, Colquhoun H, Levac D, et al. PRISMA Extension for Scoping Reviews (PRISMA-ScR): checklist and explanation. Ann Intern Med. 2018;169(7):467--473. doi:10.7326/M18-0850

9. Simera I, Moher D, Hirst A, Hoey J, Schulz KF, Altman DG. Transparent and accurate reporting increases reliability, utility, and impact of your research: reporting guidelines and the EQUATOR Network. BMC Med. 2010;8:24. doi:10.1186/1741-7015-8-24
