import pytest


def test_get_blame(github_api, dummy_repository):
    blame = github_api.blames.get_blame(
        dummy_repository,
        'dummyfiles/dummyauthor.txt'
    )

    assert blame is not None, 'blame is None'

    author = blame.get_line_author_info(1)

    assert author is not None, 'author is None'

    assert author.get_username() == 'karambir-sentieo'


def test_get_blame_file_not_found(github_api, dummy_repository):
    with pytest.raises(FileNotFoundError):
        github_api.blames.get_blame(
            dummy_repository,
            'dummyfiles/dummyauthor22.txt'
        )
