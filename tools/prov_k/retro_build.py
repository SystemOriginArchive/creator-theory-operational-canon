#!/usr/bin/env python3
"""Deterministically regenerate retroactive reconstruction manifests."""

from __future__ import annotations

import argparse
from pathlib import Path

from .manifest import build_manifest, dump_manifest_file, sha256_file

RETRO_NOTICE = "Retro manifests are reconstruction scaffolds only. They are NOT historical proof unless tied to exact historical commits/tags and user signatures."

RELEASE_GROUPS = (
    {
        "label": "releases-lineage-current-state",
        "output": "provenance/manifests/releases-retro-reconstruction.json",
        "prefixes": ("releases",),
    },
    {
        "label": "v0.3.0-current-state",
        "output": "provenance/manifests/v0.3.0-retro-reconstruction.json",
        "prefixes": ("v0.3.0",),
    },
    {
        "label": "v0.3.1-current-state",
        "output": "provenance/manifests/v0.3.1-retro-reconstruction.json",
        "prefixes": ("v0.3.1",),
    },
)


def select_paths(root: Path, prefixes: tuple[str, ...]) -> list[Path]:
    paths: list[Path] = []
    for prefix in prefixes:
        start = root / prefix
        if start.is_file():
            paths.append(start)
        elif start.is_dir():
            paths.extend(path for path in start.rglob("*") if path.is_file())
    return sorted(paths, key=lambda item: item.resolve().relative_to(root.resolve()).as_posix())


def build_retro_manifests(repo_root: Path, origin_attribution: str) -> list[Path]:
    repo_root = repo_root.resolve()
    previous_sha: str | None = None
    outputs: list[Path] = []
    for group in RELEASE_GROUPS:
        output_path = repo_root / group["output"]
        data = build_manifest(
            repo_root,
            group["label"],
            file_paths=select_paths(repo_root, group["prefixes"]),
            prev_manifest_sha256=previous_sha,
            status="UNSIGNED_DRAFT",
            provenance_class="retroactive_reconstruction",
            origin_attribution=origin_attribution,
            created_utc="2026-06-10T00:00:00Z",
            awaiting_user_signature=True,
            historical_proof=False,
        )
        data = {"_notice": RETRO_NOTICE, **data}
        output_path.parent.mkdir(parents=True, exist_ok=True)
        dump_manifest_file(output_path, data)
        previous_sha = sha256_file(output_path)
        outputs.append(output_path)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate PROV-K retroactive reconstruction manifests")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--origin-attribution", required=True)
    args = parser.parse_args()
    for output in build_retro_manifests(Path(args.repo_root), args.origin_attribution):
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
