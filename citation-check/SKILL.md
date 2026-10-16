---
name: citation-check
description: Audit a legal case notebook (Markdown) so every factual assertion carries a source locator (release/file/page, Bylaws section, statute) or an explicit VERIFIED / INFERRED / OPEN label. Use when asked to "check citations", "make sure everything is cited", or before submitting case-file work product.
---

# Citation check

## The rule

Every factual sentence says where it comes from.

It does that in one of three ways:

1. **A record cite.** Give the file and the page, for example `R2/Summary p.5` or `R1/05 NPDB p.2`.
2. **A legal cite.** Give the rule itself, for example `Bylaws VIII §5.i p.31`, `CPLR 217(1)` or `45 C.F.R. §60.12`.
3. **A status label**, when there is no cite to give:
   - **VERIFIED**: I checked it at the cite given.
   - **INFERRED**: my own reasoning. The line states the reasoning.
   - **OPEN**: the file doesn't establish it. The line says what would.
   - **[M]**: it rests on the client's word alone. The line says whether later releases support it, contradict it, or say nothing.

Two more rules:
- **Never invent a page number.** If you can't find the source, the line is OPEN.
- **The other side's documents are their claims.** When the NPDB report says Mercer was "afforded applicable rights," cite it as the hospital's assertion. Don't write it as a fact in your own voice.

## What the script checks and what it doesn't

- It checks that each line has a cite or a label.
- It does **not** check that the cite is right. Open the source for every fact the strategy depends on.
- An entry (a bold title followed by `- *Field:*` bullets) passes if any one of its lines has a cite.
- It skips headings, label definitions, short field values, and **every table row**. Check tables by hand until the script covers them.

## Steps
1. Run the script bundled in this skill folder: `python3 -I <this skill folder>/scripts/check_citations.py <notebook_dir>/*.md`. If you can't run code, apply the rule above by hand, line by line.
2. For each flagged line, add the cite from the source, or label it INFERRED (with the reasoning) or OPEN (with what would establish it).
3. Re-run until it reports 0 flagged lines.
4. Read the tables and spot-check the cites behind the recommendation. The script can't do either.
5. Rebuild any derived PDF or zip.
