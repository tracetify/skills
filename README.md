# Tracetify Skills

Skills that answer **what winners actually did** — powered by
[Tracetify](https://tracetify.com)'s growth-trace data.

Most competitive analysis tells you where a product stands today. These
skills work from its reconstructed history instead: the first mention, the
quiet weeks, the directory wave, the launch spike — twelve sources per trace,
every claim dated and linked to the page it came from.

## Install

```
npx skills add tracetify/skills
```

Or copy a skill folder from `skills/` into `~/.claude/skills/` (Claude Code)
or your agent's skills directory.

Live data comes through the [`tracetify-mcp`](https://github.com/tracetify/tracetify-mcp)
server — each skill guides you through the one-line setup if it isn't
connected yet. Reading the public report library is free; fresh traces draw
from your Tracetify credit balance.

## Skills

| Skill | What it does |
| --- | --- |
| [`competitor-teardown`](skills/competitor-teardown/SKILL.md) | Turn a competitor's real growth timeline into a dated, source-linked playbook — and apply it to your own project |

More are on the way; the bar for inclusion is that a skill's core step
cannot be answered without trace data.

## License

MIT
