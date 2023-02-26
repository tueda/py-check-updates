from pathlib import Path

from pytest_mock import MockerFixture

from check_updates import poetry, update

from . import conftest


def test_update_pyproject(mocker: MockerFixture) -> None:
    mocker.patch(
        "check_updates.pypi._get_latest_version_impl",
        side_effect=conftest.offline_get_latest_version_impl,
    )
    mocker.patch(
        "check_updates.pre_commit._get_pre_commit_hook_impl",
        side_effect=conftest.offline_get_pre_commit_hook_impl,
    )

    filename = str(Path(__file__).parent / "data/configs/poetry/simple/pyproject.toml")
    lines = tuple(Path(filename).read_text().splitlines())

    assert poetry.update_pyproject(filename) == (
        (
            update.Update(
                "pytest",
                "^5.2",
                "7.1.2",
                filename,
                "tool.poetry.dev-dependencies",
                None,
            ),
        ),
        update.FileContent(filename, lines),
    )


def test_analyze_pyproject() -> None:
    filename = str(Path(__file__).parent / "data/configs/poetry/simple/pyproject.toml")
    lines = tuple(Path(filename).read_text().splitlines())

    assert poetry.analyze_pyproject(filename) == (
        poetry.PoetryConfigStruct(
            filename,
            (
                poetry.PoetryConfigPackage(
                    "numpy", "^1.23.0", "tool.poetry.dependencies"
                ),
                poetry.PoetryConfigPackage(
                    "pytest", "^5.2", "tool.poetry.dev-dependencies"
                ),
            ),
        ),
        update.FileContent(filename, lines),
    )
