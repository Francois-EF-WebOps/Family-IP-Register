# Family Operations Runtime

**Status:** Architecture proposal and first implementation slice  
**Design goal:** Keep portfolio operations useful without paid AI, a hosted model, or a continuously running service.

## What this is

A portable, local-first operations layer: shared project records, deterministic discovery and validation, task handovers, evidence, and human approval gates. It is not an agent swarm framework and does not require an AI provider.

## Operating principles

1. **Offline-capable core:** inventory, reporting, validation, and task records work without network access or model calls.
2. **AI is an adapter:** agents may consume bounded task packets and return structured findings. The runtime remains useful if every model quota is exhausted.
3. **Files are the source of truth:** human-readable Markdown/YAML/JSON and Git history; no proprietary database required.
4. **Independent projects:** shared conventions, not a forced monorepo or uniform technology stack.
5. **Least privilege:** discovery agents read-only by default. Changes, publishing, payments, merges, deletion, and external communication require explicit human approval.
6. **Deterministic before intelligent:** scripts handle repeatable checks; agents interpret ambiguity and exceptions.
7. **Portable execution:** Python standard library and Git are the initial baseline. GitHub, Codespaces, Actions, Copilot, and local models are replaceable adapters.

## Layers

- **Control plane:** portfolio index, priorities, project passports, policies, task queue, decision log.
- **Runtime:** local CLI for discovery, validation, report generation, and task packet creation.
- **Workers:** deterministic scripts first; optional AI agents and human contributors second.
- **Adapters:** local filesystem and Git first; GitHub API/CLI, CI, model providers and local inference optional.
- **Deliverables:** independently maintained project repositories and released assets.

## Team / squad model

A coordinator owns the queue and assigns small, non-overlapping tasks. Squads are role-based, not permanently running processes:

- **Discovery squad:** repository inventory, structure, status and stale work.
- **Engineering squad:** build, tests, dependencies and maintainability.
- **Security squad:** secrets, privacy, threat boundaries and unsafe operations.
- **Evidence squad:** source quality, provenance, claims and reproducibility.
- **Rights squad:** licences, authorship, third-party assets and commercial restrictions.
- **Delivery squad:** user journey, release evidence, support and buyer validation.

Start with deterministic tools. Activate only the specialist needed by a finding. A coordinator must not launch every worker against every repository by default. Keep concurrency low to avoid duplicated context, rate limits and review overload.

## Task lifecycle

1. Discover a candidate task without AI.
2. Create a bounded task packet with repository, commit SHA, objective, scope, constraints and expected output.
3. Assign one worker; provide only relevant files and prior evidence.
4. Worker returns facts, evidence, inferences, unknowns, risks and one next action.
5. Coordinator checks evidence and deduplicates.
6. Human approves any consequential change.
7. Record outcome and commit/reference; update project passport.

## Offline-first guarantees

The first runtime command must:
- scan local Git repositories;
- report branch, commit, dirty state and common project markers;
- write JSON or Markdown;
- make no network calls;
- make no AI calls;
- never read or print environment variables, credential files or secret values.

## Resource and quota policy

- One Codespace at a time; stop it when idle.
- Use shell, Git, Python standard library and CI for routine checks.
- Batch repository metadata collection.
- No polling loops or always-on agents.
- Model calls require a bounded task and explicit value; prefer one coordinator call over repeated broad prompts.
- Do not assume any provider's free tier is permanent or unlimited.
- Never send private repository contents, family data, secrets or client material to an external model without an explicit data review.

## Safety and approval boundaries

Read-only by default. Require human approval for:
- modifying or deleting project files;
- changing licences or ownership statements;
- publishing or deploying;
- merging pull requests;
- spending money, moving funds, signing transactions;
- contacting customers, employers, partners or public audiences;
- disclosing personal, confidential or patent-sensitive information.

## First milestone

Run `python3 scripts/portfolio.py scan . --format markdown` in a workspace containing cloned repositories. Verify that it reports local repository metadata only and works with network disabled. This is the proof that the core does not depend on paid AI.

## Explicit non-goals for v0

No autonomous financial activity, no unattended public publishing, no cloud database, no mandatory web UI, no model orchestration dependency, no claim of unlimited free compute, and no forced migration of existing project structures.
