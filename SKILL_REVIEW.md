# Skill review (step 6) and test findings

## Checked against the assignment's defect list
| Defect | Status in case-strategy-tutor | Where |
|---|---|---|
| Tasks with no explanation of how they inform one another | Each stage says what it **feeds** and when to **revisit**; there is a flow diagram | SKILL.md, each stage; "How the stages connect" |
| Long summaries without student engagement | About one screen per turn, then a question; a checkpoint ends every stage | SKILL.md "The workflow" |
| Assumes the user understands the case | Stage 0 baseline; Checkpoint 1 explain-back | SKILL.md Stage 0, 1 |
| Preferred conclusion embedded as a rule | No case facts in the skill. Evals moved out of the package. "Would this change if the facts differed?" check | SKILL.md Stage 5 |
| Vague source checks | Read / listed / scan inventory; locators; label table; scan procedure; clocks with arithmetic | references/source-protocol.md |
| No procedure for contradictory evidence | Conflicting-sources rule; revision protocol | source-protocol §3; revision-protocol.md |
| No saving or reopening directions | Versioned files and a five-step reopening check | references/working-documents.md |
| References to unavailable files or tools | Web verification is conditional ("if you can reach"); no scripts | |

## Instructions traced to the Mercer work
- Typed vs handwritten text, brace scope and insertions (source-protocol §4) ← the Nov 20 transcription error log (06 §C, E1-E10).
- Opposing-party assertions are not facts (source-protocol §3) ← the "afforded applicable rights" trap (06 §B).
- Client-only facts re-checked against each release (source-protocol §3) ← [M] rows with "R2 effect" (02).
- Source status and dispute status kept in separate columns (SKILL Stage 1) ← 02 Chronology design.
- Date conflicts are pivotal and clocks are computed both ways (source-protocol §6) ← 12/16 vs 12/19 (06 Q2; 02 Clocks).
- **Load-bearing premise check (SKILL Stage 5) ← iteration-1 test.** The with-skill strategy run rested its recommendation on an unverified NPDB premise; the baseline run had looked it up. Checking the NPDB Guidebook showed a void requires actual vacatur, so the Mercer strategy changed (strategy change log v1.1).

## Iteration-1 results (3 tests × with/without skill; graded on 31 checks)
| Test | With skill | Without |
|---|---|---|
| Understanding | 9/10 | 7/10 |
| Strategy | 11/11 | 9/11 |
| Revision | 10/10 | 9/10 |
| **Overall** | **96.7%** | **80.7%** |

What the numbers hide (grader_notes.md):
- Most checks passed in both configurations, so the margin is modest. Three runs per side illustrate a result; they don't prove one.
- The clearest differences are in **judgment**. Without the skill, the runs filed an NPDB statement "this week," before the client interview. They also called the confirming letter to Baxter "concedes nothing." With the skill, both decisions went to the student.
- Both configurations repeated the notebook's "standard met on both charts." Case B was "met with some concerns" (R2/Summary p.5). Fixed in the working docs.
- Neither run named the six text-less scans. Fixed in Stage 0.

Iteration 2: the strategy test is rerun with the revised skill (see `case-strategy-tutor-workspace/iteration-2/`).

## Iteration-2 result (strategy test rerun with the revised skill)
The fix worked. The rerun ran an explicit "Load-bearing premise check" (response.md, around line 270). It labeled the recommendation **CONDITIONAL** on two unverified premises: a timely hearing request (A1) and Mercer's H&P account. It made verifying them steps 1-2 of the sequence. It also marked as verified only the authorities it actually fetched in that session. In iteration 1, the recommendation rested on an unverified NPDB premise and said nothing about it.
