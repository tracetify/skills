# UIZZE: a free skill as a product entry point

Reviewed September 28, 2026. Public-source research using `competitor-research`; no paid data or private analytics. Question: what can Tracetify learn from UIZZE's agent distribution? Context: a small team distributing free competitor-research and Search Console workflows.

## Finding

UIZZE offers a useful pattern to test: an installable free workflow, a specific first task, and an optional connection to paid product data. The public evidence establishes that path. It does not establish how many customers followed it or whether it caused revenue growth.

## Product and free-to-paid boundary

The official README positions UIZZE around interface work inside coding agents. It offers a free skill installation command followed by a billing-page task and says the skills can work without an account or MCP connection. Its optional paid MCP supplies interface references and design materials. These are company-described capabilities, not a measured product-quality assessment. [Official README, pinned snapshot](https://github.com/uizze/uizze/blob/56f965dbd377dd73af256e0d3ded757d8747ed9d/README.md).

The `ui-design` instructions start from the user's brief, existing components and constraints. Paid reference retrieval is conditional on a concrete question needing additional evidence; an empty result should not block the work. This is visible in the published instructions, although this review did not execute the paid tools. [Skill instructions](https://github.com/uizze/uizze/blob/56f965dbd377dd73af256e0d3ded757d8747ed9d/skills/ui-design/SKILL.md).

## Dated observations

These are observation dates, not claimed launch dates. The pinned repository revision was committed September 26, 2026; that timestamp does not establish when each feature first appeared.

| Observed on | Evidence | What it establishes |
|---|---|---|
| September 28, 2026 | [Production skill index](https://uizze.com/.well-known/agent-skills/index.json) | Three entries: `anti-ui-slop`, `ui-design`, and `ui-radar`, with download or skill-file URLs. This is a distribution surface, not an installation count. |
| September 28, 2026 | [UIZZE distribution document](https://github.com/uizze/uizze/blob/56f965dbd377dd73af256e0d3ded757d8747ed9d/DISTRIBUTION.md) | The publisher maintains separate skill and MCP discovery routes and a list of catalog entries. A publisher's list alone does not independently verify every entry. |
| September 28, 2026 | [UIZZE plugin in GitHub Awesome Copilot](https://github.com/github/awesome-copilot/tree/main/plugins/uizze) | A plugin entry is publicly present in another repository. It does not prove referral traffic, installations or purchases. |

## Interpretation

Our hypothesis: users may be more willing to try a paid data connection after a free workflow completes a useful task. A concrete first prompt could help them reach that result. Neither hypothesis is a measured UIZZE conversion result.

The useful distribution asset is more than a catalog description: users can inspect the workflow before installing it and understand what the optional product adds. For Tracetify, that suggests keeping public-web research and supplied GSC exports useful on their own, with paid data offered only when it addresses an actual evidence gap.

## Three small experiments for Tracetify

| Experiment | Evidence → hypothesis | Test, effort and dependencies | Success and review rule |
|---|---|---|---|
| First useful research brief | UIZZE pairs an install command with a specific task → a worked task may improve completion. | Invite five willing users to research one public competitor each. One day of preparation; requires a working agent and public browsing. Ask for explicit feedback rather than collecting their prompts. | At least three finish a cited brief without setup help; at least two voluntarily report a second use within 14 days. Otherwise fix the first-task workflow before expanding distribution. |
| One relevant catalog | The Awesome Copilot entry is observable → a relevant agent catalog may bring qualified users. | Prepare one contribution following the catalog's rules, validate its package and check for duplicates. Budget one day, no paid placement; acceptance depends on maintainers. | Review 14 days after acceptance. Record identifiable referral visits and user-reported completed tasks; missing referrers are unknown, not zero installs. Continue only if the channel produces a useful trial or actionable feedback. |
| Optional data handoff | UIZZE makes paid retrieval conditional → an explained evidence gap may create demand for additional data. | In a research brief, explain when public evidence is insufficient and what an optional data source could add. Keep the free result complete. Half a day of copy review; paid calls still need authorization. | Review the first ten completed briefs: do users understand the extra value? Track MCP-guide clicks as interest only. Do not treat a click as a connection, purchase or successful research run. |

These thresholds are proposed decision rules for a small test, not industry benchmarks.

## What remains unknown

The earlier claims of 620K installs, 74 referring domains, subscriber counts and MRR were not independently verified here. This review has no install-to-activation, retention or revenue attribution data. Verifying those claims would require dated original metric sources and matching definitions; attributing revenue to a channel would additionally require referral/cohort or conversion evidence. A current listing cannot reconstruct an early growth timeline.

This example intentionally stops at the evidence boundary rather than inventing a launch story or projecting revenue from installation totals.
