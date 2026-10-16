# Grader notes, iteration 1

## Eval 1: understanding-first-session (with 0.90, without 0.70)
- **Difference.** The with_skill run records the baseline word for word and holds back corrections. It returns the student's three confusions as the Checkpoint 1 task. The without_skill run corrects at once ("two parts need correcting") and answers both confusions itself.
- **Errors.** None found. Both quote the notebook's "standard of care met on both charts" (05). Case B was "met with some concerns" (R2/Summary p.5).
- **Should not encourage.** Turns 3 to 6 each go on "no scripted reply. Continuing", and turn 6 asks the student nothing. Neither run names the six text-less scans (01_Source_Map).

## Eval 2: integrated-strategy (with 1.00, without 0.82)
- **Difference.** The with_skill run gives five costed, stress-tested paths and recommends hearing-backed negotiation (P2). P2 depends on "a corrected NPDB characterization if lawful", which is unverified. The without_skill run found that only a reversal voids an NPDB report, so it leads with the hearing. That finding goes to the with_skill run's weakest premise.
- **Risky without_skill advice.** It files the NPDB statement "this week", before the client interview, and serves the notice of claim with no decision gate.
- **Unverified as verified (with_skill).** It claims it read §50-e and CPLR 217 "on the NY Senate site" and §60.12 "on Cornell LII". Nothing in the outputs confirms this, so check the tool trace.
- **Errors.** None material. "Recruited the day probation began" comes from the notebook (05). It is ambiguous: the Plan is dated 12/11 and the request 12/12.

## Eval 3: revision-after-removed-assumption (with 1.00, without 0.90)
- **Difference.** Small. The with_skill run keeps the hypothetical as a labelled branch and says "Uncertain, with a provisional modification", gated on G2. It flags that a confirming letter may concede the defect and leaves that call to the student. The without_skill run says the letter "concedes nothing", and its chronology lists 2/24 with "Prior counsel's file" as the locator.
- **Detail.** The without_skill run says the request is timely if the letter was received "on or after 1/25", but 1/25/2026 was a Sunday. The with_skill run uses Monday 1/26. Both runs' other dates are correct.

## Non-discriminating assertions (both runs passed)
- **Eval 1:** #3, #4, #5, #7, #8, #9, #10. #5 passes on [M] markers alone.
- **Eval 2:** all except #5 (opposing responses per path) and #11 (tell the student to save).
- **Eval 3:** all except #1, and that verdict is borderline.
- **Suggestions.**
  - Add assertions on the quality of the advice: no NPDB statement before the client interview, and decision gates for adversarial filings.
  - Add an assertion that "verified" law claims are backed by the trace.
  - Make eval 1 #5 require both the source-status column and the dispute column.
