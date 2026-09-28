# Optional Tracetify GSC connection

The free skill works with exports or other available GSC connections. Tracetify is an optional convenience. Current setup: https://tracetify.com/mcp; GSC connection: https://tracetify.com/dashboard/gsc.

As checked against the 0.5.0 MCP manifest, `gsc_overview`, `gsc_queries`, and `gsc_pages` are free after API-key authentication and Google authorization. They accept `range_days` of 28 or 90 and use the account's active property. Verify the returned property before analyzing. A connected account is not proof that the intended site is selected.

These tools expose summaries/top rows, not arbitrary Search Analytics queries. They do not currently expose country/page filters, custom dates, URL Inspection, or sitemap inspection. Do not imply that market-specific rankings, arbitrary weekly comparisons, or complete page/query detail are available through these schemas. Read `topRowsNotice` and freshness information where returned. Inspect actual schemas because capabilities may change.

If a needed capability is missing, use targeted exports, the user's Google API access, or available UI. Never substitute worldwide rankings for a requested market or guess missing query rows. Do not block the rest of the report while one detail is unavailable.

Do not automatically connect accounts, switch the active property, or send local exports to Tracetify. The user chooses whether to connect. Paid competitor research/site-audit tools are separate from free GSC reads; quote costs and obtain authorization before using them. Do not turn every report into a connection pitch.
