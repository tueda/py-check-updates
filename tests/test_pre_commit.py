from pathlib import Path

from pytest_mock import MockerFixture

from check_updates import pre_commit, update

from . import conftest


def test_update_pre_commit(mocker: MockerFixture) -> None:
    mocker.patch(
        "check_updates.pypi._get_latest_version_impl",
        side_effect=conftest.offline_get_latest_version_impl,
    )
    mocker.patch(
        "check_updates.pre_commit._get_pre_commit_hook_impl",
        side_effect=conftest.offline_get_pre_commit_hook_impl,
    )

    filename = str(
        Path(__file__).parent / "data/configs/pre-commit/simple/.pre-commit-config.yaml"
    )
    lines = tuple(Path(filename).read_text().splitlines())

    assert pre_commit.update_pre_commit(filename) == (
        (update.Update("flake8-bugbear", "21.9.2", "22.6.22", filename, None, 9),),
        update.FileContent(filename, lines),
    )


def test_analyze_pre_commit_config(mocker: MockerFixture) -> None:
    mocker.patch(
        "check_updates.pre_commit._get_pre_commit_hook_impl",
        side_effect=conftest.offline_get_pre_commit_hook_impl,
    )

    filename = str(
        Path(__file__).parent / "data/configs/pre-commit/simple/.pre-commit-config.yaml"
    )
    lines = tuple(Path(filename).read_text().splitlines())

    assert pre_commit.analyze_pre_commit_config(filename) == (
        pre_commit.PreCommitConfigStruct(
            filename,
            (
                pre_commit.PreCommitConfigPackage(
                    "flake8-bandit", "3.0.0", "python", filename, 8
                ),
                pre_commit.PreCommitConfigPackage(
                    "flake8-bugbear", "21.9.2", "python", filename, 9
                ),
            ),
        ),
        update.FileContent(filename, lines),
    )


def test_analyze_pre_commit_hooks(mocker: MockerFixture) -> None:
    mocker.patch(
        "check_updates.pre_commit._get_pre_commit_hook_impl",
        side_effect=conftest.offline_get_pre_commit_hook_impl,
    )

    assert pre_commit.analyze_pre_commit_hooks(
        "https://github.com/PyCQA/flake8", "4.0.1"
    ) == pre_commit.PreCommitHooksStruct(
        "https://github.com/PyCQA/flake8",
        "4.0.1",
        {
            "flake8": "python",
        },
    )
