# Search Console example (synthetic)

Scope: `sc-domain:example.test`, Germany, Web, all devices; 2026-08-28–2026-09-24 versus the preceding 28 days. Export filters have been checked. Files in `gsc-current/` are an intentionally tiny demonstration, not real site data or a complete previous-period dataset.

The Pages and Queries tables are separate views. The sample does not establish which query belongs to each page. It supports a preliminary page shortlist, not query-specific rewriting.

| Page | Clicks | Impressions | CTR | Position | Initial decision |
|---|---:|---:|---:|---:|---|
| /pricing | 0 | 100 | 0% | 1 | Check page-filtered queries for brand sitelinks; do not assume title failure |
| /tool | 2 | 120 | 1.67% | 12 | Candidate if relevant non-brand queries are confirmed |

The site-level query export includes a brand term, but cannot prove it explains /pricing. Request a /pricing-filtered Queries export before diagnosing it. Check recent edits for /tool; a change made three days ago needs an observation window before another overlapping rewrite.

No independent overall totals are supplied. Do not calculate a property CTR by summing these tables, or infer that omitted queries had zero clicks. If the user supplies no further detail, deliver these limited findings and defer the edit batch.

Import the sample from the repository root:

```bash
python3 skills/gsc-seo-optimizer/scripts/import_gsc.py \
  skills/examples/gsc-current/Pages.csv --property sc-domain:example.test \
  --start 2026-08-28 --end 2026-09-24 --country deu
```
