#!/bin/sh
#
# Download test files from given URLs.
#
# Requirements:
#   python >= 3.7.
#
""":" .

exec python3 "$0" "$@"
"""

import re
import sys
import urllib.request
from pathlib import Path

__doc__ = "Download test files from given URLs."

DOWNLOADS_PATH = Path(__file__).parent.parent / "tests/data/offline"


def url_cache(url: str) -> Path:
    """Return the cache path for the given URL."""
    # We handle, for example,
    #   https://pypi.org/pypi/<package>/json
    #   https://pypi.org/pypi/<package>/<version>/json
    #   https://raw.githubusercontent.com/<user>/{repo}/{rev}/.pre-commit-hooks.yaml

    m = re.match(r"https://pypi.org/pypi/(.*)", url)
    if m:
        return DOWNLOADS_PATH / f"pypi/{m.group(1)}.dat"

    m = re.match(r"https://raw.githubusercontent.com/(.*)", url)
    if m:
        return DOWNLOADS_PATH / f"github/{m.group(1)}.dat"

    raise ValueError(f"unsupported URL: {url}")


def download_file(url: str) -> None:
    """Download a file from the given URL and place it into the downloads path."""
    dest = url_cache(url)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not (url.startswith("http://") or url.startswith("https://")):
        raise ValueError(f"unsupported scheme: {url}")
    data = urllib.request.urlopen(url).read()  # noqa:S310, checked in the above
    with open(dest, mode="wb") as f:
        f.write(data)
    print(f"downloaded `{url}' to `{dest}'")


def main() -> None:
    """Entry point."""
    urls = sys.argv[1:]
    for url in urls:
        download_file(url)


if __name__ == "__main__":
    main()
