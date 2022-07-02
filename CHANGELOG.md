# Changelog

<a name="0.1.1"></a>
## [0.1.1] (2022-07-02)

### Fixed
- Missing support for pre-commit hooks hosted on GitLab.com.
  ([d54ff71](https://github.com/tueda/py-check-updates/commit/d54ff7153e821f73f8f13e1813360b7e9799ece1))
- `KeyError` raised for pre-commit hooks when `.pre-commit-hooks.yaml` was missing.
  ([f073f9e](https://github.com/tueda/py-check-updates/commit/f073f9e4dc8e97ba3b327ef8e340b4fac6a4f33a))
- Partially broken (hard-coded) list of excluded directories in the configuration file search.
  ([03195a9](https://github.com/tueda/py-check-updates/commit/03195a9d18834d954d069a4d29ac1736449aa8c2))

<a name="0.1.0"></a>
## 0.1.0 (2022-07-01)
- First release.
  Limited support for top-level dependencies in `pyproject.toml` ([Poetry](https://python-poetry.org/))
  and additional dependencies in `.pre-commit-config.yaml` ([pre-commit](https://pre-commit.com/)).

[0.1.1]: https://github.com/tueda/py-check-updates/compare/0.1.0...0.1.1
