# The idea

The lead writes this once the team has agreed the idea, and no issue is created before it is
complete. If your task doesn't fit this page, open a change-request (AGENTS.md §7).

## Problem

Small teams keep receipts in a spreadsheet export and add them up by hand each month. It takes
an hour and the total is often wrong.

## The idea

`receipts`: a command that reads a CSV export of receipts and prints the total per category.

## What we build

- Parsing the CSV export into `Receipt` records (Matrix)
- Totals per category and the command line (Zeus, for the lead)

## What we don't build

- Currency conversion, OCR of paper receipts, a web page

## The demo, in one line

`python3 -m receipts samples/march.csv` prints three category totals that match the sheet.

## Areas and owners

Each person owns their area's directories outright (AGENTS.md §6). The core is the shared
contracts; only the lead changes it.

| Area | Directories | Owner | Issues |
|---|---|---|---|
| core | receipts/model.py, docs/design.md | @atiladeokegab | — |
| parse | receipts/parse/, tests/parse/ | @Atilmatrix | #1 (vertical) |
