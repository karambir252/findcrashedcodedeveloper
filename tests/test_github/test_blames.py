import pytest


def test_get_blame(github_api, dummy_repository):
    blame = github_api.blames.get_blame(
        dummy_repository,
        'dummyfiles/dummyauthor.txt'
    )

    assert blame is not None

    author = blame.get_line_author(0)

    assert author.get_username() == 'karambir252'


def test_get_blame_file_not_found(github_api, dummy_repository):
    with pytest.raises(FileNotFoundError):
        github_api.blames.get_blame(
            dummy_repository,
            'dummyfiles/dummyauthor22.txt'
        )
