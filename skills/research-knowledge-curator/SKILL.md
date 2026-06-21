---
name: research-knowledge-curator
description: Use when the user wants to organize research notes, evidence cards, paper cards, Zotero/Obsidian materials, experiment logs, claims, citations, or project knowledge into a maintainable knowledge base without dumping unverified summaries.
---

# Research Knowledge Curator

## Trigger

Use this skill when the user asks to organize, merge, clean, deduplicate, migrate, or maintain research notes, paper cards, evidence cards, experiment logs, Zotero exports, Obsidian vaults, literature matrices, or project knowledge bases.

## Inputs

- Notes, PDFs, Zotero metadata, BibTeX, evidence cards, paper cards, screenshots, comments, experiment logs, project conversation/thread archives, or existing vault folders.
- Target knowledge-base structure, if any: folders, tags, templates, naming rules, backlinks, indexes, or frontmatter schema.
- Project research questions, inclusion rules, source quality rules, and what should not be written.
- Existing duplicate notes, outdated notes, unresolved claims, and review queues if available.

## Procedure

1. Define curation scope:
   - Identify the target vault/folder, topic, time range, source types, and whether the task is ingest, cleanup, migration, or review.
   - Stop before writing if source boundaries or destination rules are unclear enough to create clutter.
2. Audit source quality:
   - Classify each source as full evidence, abstract-only, metadata-only, experiment log, weak signal, duplicate, conflict, or drop.
   - Do not promote abstract-only or unverified notes into strong evidence.
3. Curate project conversations when present:
   - Inventory sessions by project, date, title, source archive, and final artifact.
   - Extract decisions, evidence, assumptions, open questions, failed attempts, and user corrections.
   - Cluster repeated questions by root cause; preserve one evidence-backed answer instead of replaying the dialogue.
   - Separate verified facts, model assumptions, assistant claims not yet verified, and decisions that need user confirmation.
   - Exclude tool chatter, duplicate prompts, and injected continuation text unless they contain the user's final decision.
4. Choose note types:
   - Use separate paper cards, evidence cards, method cards, variable cards, experiment cards, claim records, and synthesis/index notes.
   - Keep summaries separate from reusable evidence.
5. Normalize metadata:
   - Capture title, authors, year, DOI/URL, source path, status, tags, research question, evidence level, and review state.
   - Preserve links to PDF pages, tables, figures, logs, commands, and outputs.
6. Deduplicate and reconcile:
   - Merge duplicate paper records by DOI/title/path.
   - Keep conflicting claims as conflicts with conditions, not averaged conclusions.
   - Mark stale notes and unresolved claims for review rather than silently deleting them.
7. Plan writes:
   - Produce a write plan before editing: paths, note type, operation, source evidence, and risk.
   - Prefer small batches that can be reviewed.
8. Output handoff:
   - Record what was added, updated, skipped, dropped, and left for human review.

## Output Format

```markdown
# Research Knowledge Curation Report

## Scope
| Item | Value |

## Source Audit
| Source | Type | Quality | Decision | Reason |

## Note Plan
| Path | Note Type | Operation | Source | Required Fields |

## Claim Registry
| Claim | Source | Evidence Location | Status | Links |

## Dedupe and Conflict Log
| Item | Issue | Decision | Follow-up |

## Write Queue
| Priority | Action | Path | Acceptance Check |

## Do Not Ingest
| Source | Reason |

## Next Review
```

For conversation archives, additionally return:

```markdown
## Conversation Inventory
| Session | Date | Scope | Durable Artifact | Status |

## Decision and Assumption Log
| Item | Type | Evidence | Status | Reversal Condition |

## Repeated-Question Clusters
| Cluster | Canonical Answer | Evidence Needed | Do Not Repeat |

## Context Capsule
- Goal:
- Verified state:
- Open decisions:
- Current blocker:
- Next executable action:
```

## Quality Standards

- Knowledge-base writes are evidence-first, not summary dumps.
- Every reusable claim links to a source, page/table/figure/log, DOI/URL, or experiment output.
- Abstract-only, screenshot-only, or comment-only materials are marked as weak until verified.
- Duplicate notes are merged or linked deliberately; conflicts are preserved with conditions.
- Folder paths, tags, note types, and required fields are explicit before writing.
- The output names skipped and dropped material, not only kept material.
- The next session can continue from the write queue without reading the full chat.
- A conversation claim is not retained as fact unless it points to code, data, a command, a primary source, or a user decision.
- Any conflict between an earlier and later assistant answer is retained as an unresolved decision until the underlying artifact is checked.

## Failure Repair

- If the target structure is missing, propose a minimal schema and wait before bulk writes.
- If sources are too many, sample and triage first; do not auto-ingest the whole pile.
- If evidence locations are missing, create review tasks instead of strong claims.
- If duplicates conflict, preserve both claims with source conditions until resolved.
- If the vault already has user conventions, follow them rather than imposing a new taxonomy.
- If the result becomes a long summary, rewrite into source audit, note plan, claim registry, and review queue.
- If a conversation contains repeated questions, create a canonical answer with its evidence and a single next diagnostic rather than compressing the repetition into false certainty.
