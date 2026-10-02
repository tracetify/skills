#!/usr/bin/env python3
"""Build a release from an explicit public-file allowlist; never package the app."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "README.md", "LICENSE",
    "competitor-research/SKILL.md", "competitor-research/LICENSE",
    "competitor-research/agents/openai.yaml",
    "competitor-research/references/evidence.md",
    "competitor-research/references/report-template.md",
    "competitor-research/references/tracetify.md",
    "ad-angle-research/SKILL.md", "ad-angle-research/LICENSE",
    "ad-angle-research/agents/openai.yaml",
    "ad-angle-research/references/angle-extraction.md",
    "ad-angle-research/references/manual-ad-library.md",
    "ad-angle-research/references/brief-template.md",
    "gsc-seo-optimizer/SKILL.md", "gsc-seo-optimizer/LICENSE",
    "gsc-seo-optimizer/agents/openai.yaml",
    "gsc-seo-optimizer/references/data-access.md",
    "gsc-seo-optimizer/references/data-quality.md",
    "gsc-seo-optimizer/references/report-template.md",
    "gsc-seo-optimizer/references/roi-rubric.md",
    "gsc-seo-optimizer/references/tracetify.md",
    "gsc-seo-optimizer/scripts/gsc_fetch.py",
    "gsc-seo-optimizer/scripts/import_gsc.py",
    "gsc-seo-optimizer/scripts/requirements-api.txt",
    "examples/competitor-offline.md", "examples/gsc-review.md",
    "examples/uizze-growth-research.md",
    "examples/gsc-current/Pages.csv", "examples/gsc-current/Queries.csv",
    "examples/gsc-current/Filters.csv",
]


def source_path(relative):
    direct = ROOT / relative
    if direct.exists():
        return direct
    return ROOT / "skills" / relative


def archive_path(relative):
    if relative.startswith(("competitor-research/", "gsc-seo-optimizer/")):
        return "skills/" + relative
    return relative


def public_readme(content):
    return content.replace(b"](competitor-research/", b"](skills/competitor-research/").replace(
        b"](gsc-seo-optimizer/", b"](skills/gsc-seo-optimizer/")


def build(destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Validate every input before replacing any prior package.
    payloads = []
    for relative in FILES:
        path = source_path(relative)
        if not path.is_file() or path.is_symlink() or ROOT not in path.resolve().parents:
            raise ValueError(f"Not a regular public release file: {relative}")
        content = path.read_bytes()
        if relative == "README.md":
            content = public_readme(content)
        payloads.append((archive_path(relative), content))
    temporary = destination.with_suffix(".tmp")
    with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, content in sorted(payloads):
            item = zipfile.ZipInfo("tracetify-skills/" + relative, date_time=(2026, 9, 28, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.external_attr = 0o100644 << 16
            archive.writestr(item, content)
    temporary.replace(destination)
    return destination


if __name__ == "__main__":
    print(build(ROOT / "dist/tracetify-skills-0.1.0.zip"))
