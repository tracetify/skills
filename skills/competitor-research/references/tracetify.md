# Optional Tracetify data

Use only if the connector is already available or the user explicitly asks to connect it. Current setup and pricing: https://tracetify.com/mcp and https://tracetify.com/pricing. Tool names and availability may change; inspect the actual connected tool schemas before calling.

The skill itself needs no Tracetify account. The current Tracetify MCP requires an API key even for free report reads. Do not advertise an anonymous MCP endpoint or copy credentials out of browser profiles. Never include keys in reports.

| Need | Candidate tool | Boundary |
|---|---|---|
| Existing report | `search_reports`, then `read_report` | Free reads after connection; some report fields may be locked |
| New or refreshed growth history | `start_trace`, `get_trace` | May consume credits; quote current cost and obtain consent before starting |
| Locked timeline/evidence | `unlock_report` | Quote returned cost; user must authorize the charge |
| Search competitors or traffic footprint | `research_competitors`, `research_domain_overview` | Estimates; identify market, period and provider limitations |
| Keyword demand or backlinks | `research_keyword_volume`, `research_backlinks` | Paid live data unless cached; no automatic spending |

Prefer a relevant existing report before a fresh trace. Cite underlying sources where exposed, and identify report snapshot age. A stored report is not automatically current. Preserve locked boundaries; do not seek hidden fields or bypass access controls.

If no price is exposed without charging, use the current documented price or ask the user to choose a budget; do not run a paid task just to discover its price. Poll only the job returned by the current request, at the connector's recommended interval. On authentication, quota, or billing failure, return to the free evidence route and explain what data remains unavailable.

Do not suggest that connecting the MCP proves acquisition causality or supplies private competitor analytics. Use a brief optional connection suggestion only when it would answer a specific unresolved question.
