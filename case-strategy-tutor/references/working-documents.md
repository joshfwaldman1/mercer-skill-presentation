# Working documents

Maintain three documents. They are working drafts that summarize the record; they are not sources. Every factual line in them carries a locator or a label (see `source-protocol.md`).

Update a document when the sources or the analysis justify a change, and record the reason in the Strategy's change log. Keep them concise: the overview should fit on one or two pages.

## 1. Case Overview

```markdown
# Case Overview: [case name]  (as of [problem date]; version [n], [session date])

## Sources
- Read: ...
- Listed only: ...
- Not machine-readable / transcription checked?: ...
- Off-limits by course rule: ...

## Baseline (student's words, Stage 0; do not edit after recording)
- Understanding:
- What the client should do:
- Confusions:
- Needed before confident:

## The dispute in five sentences
[who, what happened, what is disputed, where it stands, what is at stake], with locators

## Actors (flag multiple roles)
| Person/body | Role(s) | Key acts (locator) | Multiple-role flag |

## Chronology (short form; full version in the Map)
| Date | Event | Locator | Source status | Disputed? |

## Procedural position and clocks
| Forum/step | Who decides | Burden & standard | Deadline (rule, arithmetic) | Status |

## Client objectives
- Ultimate: ... [confirmed by student / PROVISIONAL from (locator)]
- Immediate: ...
- Constraints: ...

## What changed since the baseline
```

## 2. Evidence-and-Issues Map

```markdown
# Evidence-and-Issues Map: [case name] (version [n])

## Propositions that matter
| # | Proposition | Who must prove it, standard | Supporting evidence (locator) | Contrary evidence (locator) | Status | Pivotal? (which strategy element it moves) |

## Claims and defenses
| Claim/defense | Elements | Burden | Rule source (verified?) | Facts for | Facts against | OPEN |

## Competing theories
| Theory | One sentence | 3 facts it needs | Most dangerous fact | Answer | Distinguishing evidence |

## Gaps
| Gap | Pivotal? | Who has it / how to get it | Time-sensitive? | Next step |

## Assumptions
| ID | Assumption | Basis | What depends on it | If wrong |

## Legal research list
| Proposition | Citation | Verified how / unverified | Effect on strategy if wrong |
```

## 3. Strategy (with change log)

```markdown
# Strategy: [case name] (version [n])

## Objective
## Case theories (ours; strongest competing)
## Proof (propositions, support, contrary, gaps)
## Options
| Path | Achieves | Requires | Costs/risks (incl. other forums) | Timing | Depends on | Opposing response | Our reply |
## Recommendation and why it beats the strongest alternative
## Sequence
1. First: ... (because ...)
2. Depends on 1: ...
- Reassess when: [specific event/finding] -> [what we would do]
## Uncertainty: what would change the recommendation, how we would learn it
## Open questions (client interview / records / research)

## Change log
| Version | Date | Trigger (record fact / HYPOTHETICAL / assumption removed / objective changed) | What changed | Why | Documents affected |

## Collaboration log
- Student's question or correction that improved the analysis: ...
- Connection the tutor surfaced that the student had missed (and how it was checked against the record): ...
```

## Saving

At the end of every session, or when asked, output each document as a separate Markdown file named `[case]_overview_v[n].md`, `[case]_map_v[n].md`, `[case]_strategy_v[n].md`. If you can't create files, output three clearly separated blocks. Tell the student to save them and, next time, add them to the Project (or upload them) along with the original case files. Never save over a previous version; increment the version number so revisions stay traceable.

## Reopening check (run before relying on supplied documents)

1. Confirm the original case files are also available. The working documents do not replace them.
2. Note each document's version and date. If the versions disagree, ask which is current.
3. Spot-check: re-open at least the locators behind the recommendation's three most important premises, plus every client-only fact and every assumption the recommendation depends on. Report any that don't check out.
4. Ask the student whether anything has changed since that version: new documents, new facts from the client, changed objectives, deadlines passed. If anything has, go to Stage 6.
5. Ask the student to explain the current recommendation in two sentences before continuing. This checks their understanding, not just the documents.
