# Tracetify Skills

Free workflows from [Tracetify](https://tracetify.com) for coding agents: investigate competitors with evidence, pull the ads they are running, and decide which pages to improve using your own Search Console data.

| Skill | Result | Required input |
|---|---|---|
| [competitor-research](skills/competitor-research/SKILL.md) | Cited product/growth brief and a few testable actions | A domain plus host browsing, or supplied materials |
| [gsc-seo-optimizer](skills/gsc-seo-optimizer/SKILL.md) | Search trend diagnosis, prioritized changes and justified skips | GSC CSV/ZIP exports, existing Google API access, or a suitable connector |
| [ad-angle-research](skills/ad-angle-research/SKILL.md) | A competitor's live Meta and Google ads turned into hooks, offers, landing pages and up to three tests | A domain; the Tracetify MCP for live data, or a manual Ad Library sample |

No Tracetify account is required. Your agent/model costs remain those of your host. Optional Tracetify MCP access requires authentication; some deeper research tools consume credits, with explicit authorization. The skill packages contain no telemetry or automatic account setup.

Browse the [skills page and worked examples](https://tracetify.com/skills?utm_source=github&utm_medium=referral&utm_campaign=agent_skills&utm_content=skills_readme) for a quick start.

## Install

```bash
npx skills add tracetify/skills --skill competitor-research
npx skills add tracetify/skills --skill gsc-seo-optimizer
npx skills add tracetify/skills --skill ad-angle-research
```

The [skills CLI](https://github.com/vercel-labs/skills) lets you choose the target agent. Add `--agent codex` or `--agent claude-code` to select one explicitly. Run `npx skills add tracetify/skills --list` to browse the collection.

For a local checkout or downloaded bundle, replace `tracetify/skills` with its directory path. To install manually, copy only the selected skill directory, including its references/scripts, into your agent's documented skills location.

## Optional MCP connection

The competitor-research and gsc-seo-optimizer skills work without a Tracetify account; ad-angle-research uses the MCP for live ad data and offers a manual Ad Library route without it. The [Tracetify MCP server](https://github.com/tracetify/tracetify-mcp) can add existing growth reports, deeper research data, and connected Search Console access. Free MCP reads still require authentication; paid research needs explicit authorization. See the [connection guide](https://tracetify.com/mcp).

The existing [`competitor-teardown`](https://github.com/tracetify/skills/tree/main/skills/competitor-teardown) remains available for users who specifically want the older Tracetify-report workflow. It requires MCP. Start with `competitor-research` for the free public-web or supplied-materials workflow; you do not need both for the same task.

## Try a real task

**Competitor research**

> Use competitor-research to investigate how this competitor found early users. I run a new B2B SaaS with a $100/month experiment budget. Separate observed evidence from hypotheses and suggest up to three things I can test.

**Ad angles**

> Use ad-angle-research on heavys.com. I sell wireless earbuds under $80. Give me the three longest-running angles with their landing pages and tell me which one I could test without video assets.

**Search Console**

> Use gsc-seo-optimizer on these two GSC exports. Our target market is Germany. Explain what changed, check whether branded searches are distorting the page metrics, and recommend the smallest worthwhile optimization batch. Do not edit the site yet.

See the [UIZZE public-source research brief](examples/uizze-growth-research.md) for a real product example with citations and explicit evidence gaps. The [offline competitor example](examples/competitor-offline.md) and [GSC example](examples/gsc-review.md) use synthetic data. Real private exports are not included.

## Development and release

Run `python3 -m unittest discover -s tests -v` from the directory containing this README in the source checkout. The GSC CSV importer has no third-party dependencies; the optional API fetcher documents its dependencies separately.

Run `python3 scripts/package_release.py` to generate an allowlisted ZIP in `dist/`. It contains the three skill packages, README, LICENSE and examples. Development scripts/tests and the legacy skill remain in the GitHub source checkout; the ZIP excludes private settings, credentials and validation reports.

Keep personal account/market preferences outside this release tree. Changes to the published core should originate here and be synchronized to personal installations after verification.

GitHub publication and third-party directory indexing are separate. Installation and format checks do not prove ranking improvements or production conversion.

## License

MIT. See [LICENSE](LICENSE).
