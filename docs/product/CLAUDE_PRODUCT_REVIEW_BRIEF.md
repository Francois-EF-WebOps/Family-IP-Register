# Independent Product & Delivery Review — Universal Creative Workspace

## Review request
Act as a sceptical principal product architect, staff frontend engineer, platform engineer, privacy/security reviewer, and ad-supported product operator. Provide an independent second opinion on the Universal Character Studio's evolution into a multi-source creative workspace.

Do not praise the concept. Identify contradictions, hidden costs, technical risks, missing decisions, weak assumptions, and the shortest credible path to a usable product. Distinguish verified facts, assumptions, recommendations, and questions. Do not assume paid infrastructure, paid APIs, a desktop computer, or a large engineering team.

## Product direction
The product is an open-entry creative workspace. It is not a linear wizard and must not force users to begin with a particular source or complete a prescribed sequence.

A user may enter with any supported combination of:
- a text prompt or idea;
- a selfie, photograph, drawing, reference sheet, or other image;
- a script or narrative;
- JSON or other structured project data;
- an existing 3D render or model, especially GLB/glTF;
- a combination of the above.

The platform should identify each input, preserve its provenance, allow the user to assign its role, reconcile compatible information, flag conflicts and uncertainty, then produce the best available preview as early as possible. The user adjusts, compares, transforms, continues, or exports. Users can enter at any point and leave at any point.

Character creation is the first complete application/use case. The architecture should be extensible to other creative assets without prematurely building a generic platform abstraction that delays delivery.

## User experience and commercial rules
1. Open entry: no mandatory starting point or linear workflow.
2. Multi-source session: add multiple inputs in one workspace and assign roles (identity, body, style, wardrobe, environment, story, geometry, other).
3. Preview first: show an honest preview or capability-specific fallback quickly. Never imply metadata inspection is a 3D render or that a prompt has been AI-generated if it has not.
4. Editing remains central: the user reviews and adjusts output. Identity facts, inferred properties, user decisions, and generated guesses must remain distinguishable.
5. Advertising: maximum one ad per ten minutes across the active session, not one ad per operation. It must never interrupt upload, editing, rendering, or export. The ad may appear at a safe transition or pause. If no ad is available, the user continues. Do not hold user work hostage.
6. Export: every format actually supported by the platform is exportable without mandatory signup. Be explicit about formats available today versus planned.
7. Persistence: signup is required to save an ongoing cloud workspace and resume across devices. Unsigned users can work locally and export. Do not lose unsaved work because auth or an ad fails.
8. Delegation: use user-authorised Google, Microsoft, or social identity/storage integrations where they reduce our infrastructure burden. Authentication is not equivalent to storage, compute, or blanket access. Request least-privilege scopes and keep integrations optional.
9. Platform remains core: our project model, workflow orchestration, preview/edit experience, provenance, compatibility, and export rules remain ours. Providers are replaceable adapters.
10. Mobile-first: Android browser is the primary constrained device. Consider memory, battery, touch UI, upload size, local storage quota, network, and interruption recovery.

## Current implementation baseline
Repository: https://github.com/Francois-EF-WebOps/Family-IP-Register
Application: character-studio/
Current baseline is a static HTML/CSS/JavaScript application with Fin/Nik fixture examples, identity separated from mutable appearance, deterministic procedural SVG preview, localStorage appearance and resumable workflow state, JSON and SVG export, versioned character and workflow schemas. It has no backend, accounts, AI generation, cloud sync, advertising integration, or 3D rendering.

The current code is a demonstrator, not a production-ready multi-user service. Do not assume localStorage is a suitable long-term binary asset store or that current fixtures are the final universal data model.

## Core architecture questions
Evaluate and recommend:
- A minimal versioned project envelope that can contain heterogeneous source records without forcing every input into a character schema.
- How to represent original source assets, extracted observations, inferred attributes, conflicts, user-approved decisions, transformations, renderer outputs, licensing/provenance, and revision history.
- Whether the universal project model should be distinct from a character-specific Universal Character Reference (UCR), and exactly where the boundary belongs.
- Input adapters for prompt/script, image, JSON, GLB and glTF.
- Renderer adapters for SVG/2D and browser 3D.
- How to render the same project across different engines without making any renderer output the source of truth.
- How to support incomplete records and partial workflows without fabricated data.
- How to version schemas and migrate old projects safely.
- What should run locally, what needs a backend, and what may be delegated to third parties.
- Whether a provider-neutral interface is worthwhile at MVP stage or premature abstraction.

## Advertising and unit economics
Assess the proposed policy: one ad maximum per ten minutes of active session, session-wide, not per operation. It is a frequency cap, not a requirement that each user watch an ad to advance.

Analyse:
- whether rewarded ads, interstitials, or another format best fit this policy;
- whether a ten-minute interval is commercially viable and acceptable UX;
- provider eligibility and fill uncertainty in Thailand and other target geographies;
- verification, consent, privacy, ad blockers, no-fill, and offline behavior;
- whether web rewarded ads are technically available under realistic publisher/account constraints;
- the cost of AI/image/3D operations compared with plausible net ad revenue;
- which operations can run locally at near-zero marginal cost;
- which operations must be quota-limited, asynchronous, optional, or deferred;
- whether advertising can ever reliably fund advanced generation without a paid tier or other revenue source.

Do not invent CPM, fill rate, eCPM, or provider eligibility. Give formulas and scenario ranges with assumptions labelled. The product must continue when ads are unavailable.

## Identity, rights, safety and privacy
Review consent and rights for uploaded faces, children, third-party likenesses, and user-generated scripts; source licensing and attribution; provenance preservation and user confirmation; retention and deletion; local-first handling of private reference images; OAuth least-privilege scopes and token storage; account deletion and export; safety controls for adult/sexualised transformations, minors, impersonation, and deceptive media; and whether face analysis or biometric processing creates additional legal/privacy obligations in target markets. Flag issues requiring qualified legal review. Do not present general product advice as legal advice.

## Delivery and acceptance criteria
Propose a staged delivery plan with explicit scope, dependencies, risks, test strategy, mobile performance targets, security/privacy acceptance criteria, deployment and rollback, measurable product metrics, and a realistic solo-developer schedule.

Assess these journeys:
1. prompt-only entry → preview → edit → export;
2. selfie/image entry → preview → user correction → export;
3. multiple images plus script → role assignment → conflict review → preview;
4. JSON import → validation → preview or clear unsupported-field report;
5. GLB import → actual browser 3D preview → inspect/rotate → export or preserve source;
6. unsigned session → local continuity → export without signup;
7. signup → cloud save/resume, with provider integration optional;
8. ad due during active work → no interruption; ad no-fill → continue normally.

For every journey, specify what is genuinely functional versus simulated.

## Required reviewer output
Return:
1. Executive verdict: build / narrow / redesign, with reasons.
2. Product boundary: what the product is and is not.
3. Proposed project/UCR data model, with an example JSON record.
4. Architecture diagram and component responsibilities.
5. Input/output format compatibility matrix.
6. Advertising feasibility and cost model with explicit assumptions.
7. Authentication, storage and external-service strategy.
8. Privacy, rights and safety threat model.
9. Prioritised risk register (severity, likelihood, mitigation, owner).
10. Delivery roadmap broken into independently testable increments.
11. Concrete acceptance tests for the first public beta.
12. What to delete, postpone, or simplify.
13. Ten hard questions the product owner must answer.
14. Unsupported or overconfident claims in the current product brief.

## Review standard
Be adversarial but constructive. Prefer existing standards and proven components over custom engines. Minimise dependencies, recurring costs, operational burden, and user friction. Optimise for a real product that one constrained developer can ship, test and maintain. If the proposed economics do not work, say so plainly and offer a viable alternative.