# Portfolio Ticketing Standard

GitHub Issues are the execution system of record for all repositories owned by Francois-EF-WebOps. Family-IP-Register maintains the canonical schema, conventions, and portfolio index; work remains in the repository where its code or evidence belongs.

## Core rules

1. Inventory existing issues, pull requests, commits, project boards, and documented work before creating a ticket. Update or link an existing record instead of duplicating it.
2. One issue represents one independently verifiable outcome. Split unrelated outcomes; use checklists and linked issues for coordinated work.
3. Preserve existing issue numbers, titles, discussion, labels, milestones, and PR history. Do not close or rewrite historical records merely to fit this standard.
4. Use GitHub Issues for actionable work. Pull requests remain implementation/review records and should link to the issue with `Closes #N` only when they fully satisfy it.
5. Do not create speculative tasks from ideas alone. Record a concrete outcome, an owner or explicit unassigned state, and acceptance criteria.
6. For system-affecting work, record the affected system/repository, data classification, trust boundary, security/privacy impact, and recovery implications. Mark each item not applicable with a reason where appropriate.
7. Use the SECURITY type only for non-sensitive security work. Do not publish exploitable vulnerability details, attack instructions, secrets, or personal data in public issues; use private vulnerability reporting or a private channel for sensitive findings.
8. Never place credentials, private family information, children's information, personal identifiers, confidential correspondence, or sensitive evidence in public issues. Link to a safe private reference instead.
9. A ticket is Done only when acceptance criteria are met and evidence is linked. Close as completed; use not planned only with an explicit rationale.
10. A Blocked ticket must name the blocking dependency, responsible external party where known, and next review trigger.
11. Record dependencies with GitHub issue links. Cross-repository dependencies must use fully qualified issue URLs.
12. Keep the original work intact. Migration is additive: inventory first, then classify and link; do not bulk-recreate backlogs.

## System and security work

For a task that changes a system's architecture, data flow, permissions, deployment, persistence, public interface, or external integrations, include these fields in the issue body or linked design record:

- **Affected system/repository:** canonical repository and component.
- **Data classification:** PUBLIC, INTERNAL, SENSITIVE, or RESTRICTED. Record the classification, never the sensitive data itself.
- **Trust boundary:** inputs, outputs, external services, devices, users, and automation that cross the boundary.
- **Security/privacy impact:** authentication, authorization, input validation, secrets, personal data, logging, retention, deletion, and exposure risks.
- **Recovery impact:** backup, restore, integrity, rollback, and failure behaviour.
- **Verification:** tests or manual checks that demonstrate the control works.

For a low-risk documentation-only task, a short `Not applicable — documentation-only; no system/data-flow change` statement is sufficient. Do not turn every issue into a security questionnaire.

Use `SECURITY` as a work type for remediation and control implementation. Public issues should describe the risk at a level safe for disclosure. Sensitive vulnerability reports must remain private.

## Cross-system ticketing

- Create the execution ticket in the repository that owns the affected system or artifact.
- Create a portfolio-level EPIC in Family-IP-Register only when coordination across multiple repositories is itself a deliverable.
- Link dependent tickets with full issue URLs; do not copy their descriptions or status into a second backlog.
- A shared architecture decision defines interfaces and principles; each consuming system still owns its own threat model, tests, data classification, and release evidence.
- Track the same stable issue URL in reports and dashboards. Exported snapshots are read-only and never override GitHub state.

## Canonical identity

The canonical ticket identifier is the GitHub issue URL, represented compactly as `owner/repository#number`. Do not invent a second global numeric sequence. An optional `ticket_id` field in exported records must equal that stable identifier.

## Issue structure

Use the templates in `.github/ISSUE_TEMPLATE/`. Each issue should include:

- Type: EPIC, TASK, BUG, RESEARCH, DECISION, RELEASE, or BLOCKER
- Outcome / problem statement
- Context and scope
- Acceptance criteria (observable, testable checklist)
- Priority: P0 urgent, P1 high, P2 normal, P3 low
- Status label: `status:backlog`, `status:ready`, `status:in-progress`, `status:blocked`, or `status:review`
- Dependencies and external counterparties, when applicable
- Evidence: commits, PRs, tests, documents, or source records
- Target date only when externally committed or operationally necessary

## Lifecycle

| Status | Meaning | GitHub state |
|---|---|---|
| Backlog | Captured, not yet prepared | Open |
| Ready | Scope and acceptance criteria are actionable | Open |
| In Progress | Work is actively underway | Open |
| Blocked | Cannot proceed until a named dependency changes | Open |
| Review | Implementation complete; verification remains | Open |
| Done | Acceptance criteria verified with evidence | Closed as completed |

Do not use a status label for Done: close the issue with a completion reason and evidence. Reopen if verification fails or new required work is discovered.

## Labels

Use these namespaces consistently:

- Type: `type:epic`, `type:task`, `type:bug`, `type:research`, `type:decision`, `type:release`, `type:blocker`
- Priority: `priority:p0`, `priority:p1`, `priority:p2`, `priority:p3`
- Status: `status:backlog`, `status:ready`, `status:in-progress`, `status:blocked`, `status:review`
- Optional domain labels: repository-specific and additive; do not replace the canonical namespaces.

If a repository lacks a canonical label, create it before applying it. Do not rename or delete unrelated existing labels.

## Portfolio operation

- Each repository owns its own issues and execution state.
- Family-IP-Register is the portfolio control plane: it documents the standard and tracks rollout/inventory links, not a duplicate copy of every task.
- Use cross-repository links rather than cloning tickets.
- Weekly review: shipped/closed, active, blocked, stale, and next concrete action.
- A repository is not considered migrated until its existing work has been inventoried and its maintainers can use the standard.

## Migration checklist

- [ ] Enumerate repositories in scope, including private repositories.
- [ ] Inventory open issues and pull requests before creating anything.
- [ ] Inspect README, project boards, TODO/FIXME records, release plans, and active branches for untracked commitments.
- [ ] Map existing work to existing issue/PR URLs; create only genuinely missing tickets.
- [ ] Add canonical labels and issue templates without removing local conventions.
- [ ] Link active PRs to their issue when the relationship is clear.
- [ ] Record repositories with no actionable work as inventoried; do not manufacture backlog items.
- [ ] Verify the inventory and publish the portfolio index.

## Data and automation contract

`schemas/ticket.schema.json` defines the normalized export shape. GitHub remains authoritative for issue state, comments, labels, assignees, milestones, and timestamps. Exported JSON/JSONL is a derived snapshot and must retain the source URL and retrieval timestamp. No automation may close, reassign, or rewrite tickets without an explicit approved workflow.
