# assets/compliance — provenance and boundary

These three CSV files are the machine-readable reference data the skill's `lint_claims()` runs
against, and they are the only compliance material published in this repository:

| File | Used for |
|---|---|
| `Never-Say-Prohibitions.csv` | the prohibited-claim list: each row carries the wording, why it is prohibited, and the approved alternative. The lint's BLOCKING rules map onto these rows |
| `Approved-Surface-Claims-16-Sentences.csv` | the approved surface-claim sentences (Annex A Section 6 wording) a Tier 2 or Tier 3 claim must be rewritten into |
| `TURI-Results-Reference-v1.0.csv` | the TURI test cells the comparative claims have to match (what was tested, on which surface, with which benchmark, and which cells are empty) |

## What is deliberately NOT here

- the Claims Filter review pack itself (`.docx`) — the governing document for every rule above;
- the Surface Claims Guide / Annex A (`.pdf`) and the extracted plain-text copy of either;
- any internal correspondence, contact list or legal note.

The Claims Filter is owned by compliance (Dutch Harbor Brands) and is not editable by this team:
rule changes go to compliance and come back as a new version. The skill summarises the rules it
operates under in `references/03-compliance-claims-filter.md`; that summary is not a substitute for
the governing document and must be re-checked against it when compliance publishes a revision.

A product's claim permissions come from Part 4 of the Filter, per SKU. These CSVs do not replace
Part 4: they exist so the automation can catch prohibited wording before a human reviews it, and so
the approved rewrites are one lookup away.