from pathlib import Path

import pytest
from pytest_mock import MockerFixture

import check_updates

from . import conftest


def test_main(capsys: pytest.CaptureFixture[str], mocker: MockerFixture) -> None:
    mocker.patch(
        "check_updates.pypi._get_latest_version_impl",
        side_effect=conftest.offline_get_latest_version_impl,
    )
    mocker.patch(
        "check_updates.pre_commit._get_pre_commit_hook_impl",
        side_effect=conftest.offline_get_pre_commit_hook_impl,
    )

    path = (
        (Path(__file__).parent / "data/configs")
        .resolve()
        .relative_to(Path(".").resolve())
    )
    check_updates.main([path])

    captured = capsys.readouterr()

    assert (
        captured.out
        == """\
tests/data/configs/poetry/simple/pyproject.toml:

    [tool.poetry.dev-dependencies]  pytest  ^5.2  7.1.2

tests/data/configs/pre-commit/simple/.pre-commit-config.yaml:

    line:9  flake8-bugbear  21.9.2  22.6.22
"""
    )


def test_version(capsys: pytest.CaptureFixture[str]) -> None:
    check_updates.main(["--version"])
    captured = capsys.readouterr()
    assert captured.out.strip() == f"py-check-updates {check_updates.__version__}"
