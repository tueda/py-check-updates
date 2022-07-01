"""Configuration for testing."""

import importlib
import json
import os
from pathlib import Path
from typing import Callable

url_cache: Callable[[str], Path] = importlib.import_module(
    str(
        (Path(__file__).parent.parent / "scripts/download-testdata")
        .resolve()
        .relative_to(Path(".").resolve())
    ).replace(os.sep, ".")
).url_cache


def offline_get_latest_version_impl(name: str) -> str:
    """Offline version of check_updates.pypi._get_latest_version_impl()."""
    return json.loads(  # type: ignore[no-any-return]
        (url_cache(f"https://pypi.org/pypi/{name}/json")).read_text()
    )["info"]["version"]


def offline_get_pre_commit_hook_impl(name: str, rev: str) -> str:
    """Offline version of check_updates.pre_commit._get_pre_commit_hook_impl()."""
    github_prefix = "https://github.com/"
    if name.lower().startswith(github_prefix):
        url = f"https://raw.githubusercontent.com/{name[len(github_prefix):]}/{rev}"
    else:
        return ""
    return url_cache(f"{url}/.pre-commit-hooks.yaml").read_text()
