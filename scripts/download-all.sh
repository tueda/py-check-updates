#!/bin/bash
set -eu
set -o pipefail

download() {
  "./$(dirname "$0")/download-testdata.py" "$1"
}

download https://pypi.org/pypi/flake8-bandit/json
download https://pypi.org/pypi/flake8-bugbear/json
download https://pypi.org/pypi/numpy/json
download https://pypi.org/pypi/pytest/json
download https://raw.githubusercontent.com/PyCQA/flake8/4.0.1/.pre-commit-hooks.yaml
