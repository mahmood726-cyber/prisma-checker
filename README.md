# PRISMA Checker

Browser-based PRISMA 2020 compliance checker for systematic review manuscripts.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

PRISMA Checker provides a structured self-assessment workflow for evaluating systematic review reporting against the 27-item PRISMA 2020 statement (Page et al. BMJ 2021;372:n71). It covers all 7 sections from Title through Other Information, with support for 6 PRISMA extensions. A real-time compliance dashboard tracks progress with section-level bar charts and an overall score ring, and generates publication-ready compliance statements.

## Features

- Full 27-item PRISMA 2020 checklist organized across 7 sections (Title, Abstract, Introduction, Methods, Results, Discussion, Other Information)
- Four-level assessment per item: Reported, Partial, Not Reported, Not Applicable
- Page/section reference and free-text notes for each item
- 6 PRISMA extensions: PRISMA-S (Searching), PRISMA-ScR (Scoping Reviews), PRISMA-NMA (Network Meta-Analyses), PRISMA-DTA (Diagnostic Test Accuracy), PRISMA-IPD (Individual Patient Data), PRISMA-P (Protocols)
- Real-time compliance dashboard with overall score ring and section-level progress bars
- Attention panel highlighting items marked Partial or Not Reported
- Auto-generated compliance statement text for manuscripts
- Expand/collapse all items for efficient review
- CSV export (item-level compliance data)
- JSON export/import (full assessment state, restorable)
- Print-optimized checklist and dashboard
- Dark/light theme toggle
- localStorage persistence (assessment survives browser refresh)

## Quick Start

1. Download `prisma-checker.html`
2. Open in any modern browser
3. No installation, no dependencies, works offline

## Built-in Examples

No built-in datasets. Begin assessing by marking each of the 27 checklist items as Reported, Partial, Not Reported, or N/A. Enable relevant extensions in the Extensions tab.

## Methods

- Based on: Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ 2021;372:n71.
- Compliance score: percentage of applicable items marked as Reported (items marked N/A are excluded from the denominator)
- Section-level scoring follows the same logic within each of the 7 PRISMA sections

## Screenshots

> Screenshots can be added by opening the tool and using browser screenshot.

## Validation

- 25/25 Selenium tests pass
- Checklist items verified against the official PRISMA 2020 statement and Explanation and Elaboration document

## Export

- CSV (item-level compliance status, page references, notes)
- JSON (full assessment state, restorable across sessions)
- Compliance statement (clipboard, manuscript-ready)
- Print-optimized report

## Citation

If you use this tool, please cite:

> Ahmad M. PRISMA Checker: A browser-based PRISMA 2020 compliance assessment tool. 2026. Available at: https://github.com/mahmood726-cyber/prisma-checker

## Author

**Mahmood Ahmad**
Royal Free Hospital, London, United Kingdom
ORCID: [0009-0003-7781-4478](https://orcid.org/0009-0003-7781-4478)

## License

MIT
