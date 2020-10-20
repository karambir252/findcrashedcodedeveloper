import pytest
from findcrashedcodedeveloper.githubapi.models.exceptions import InvalidLineNumberException


def test_get_file_content(github_api, dummy_repository):
    file = github_api.files.get_file_content(
        dummy_repository,
        'dummyfiles/dummyauthor.txt'
    )

    assert file.get_number_of_lines() == 2
    assert file.get_line_code(0) == 'Please ignore this file.'
    assert file.get_line_code(0) == 'This file is used in tests.'
    assert file.get_line_range_code(0, 1) == [
        'Please ignore this file.',
        'This file is used in tests.'
    ]

    with pytest.raises(InvalidLineNumberException):
        file.get_line_code(100)

    with pytest.raises(InvalidLineNumberException):
        # startline not in range
        file.get_line_range_code(100, 102)

    with pytest.raises(InvalidLineNumberException):
        # endline not in range
        file.get_line_range_code(0, 102)

    with pytest.raises(InvalidLineNumberException):
        # endline is smaller then startline
        file.get_line_range_code(100, 88)


def test_get_file_content_filenotfound(github_api, dummy_repository):
    with pytest.raises(FileNotFoundError):
        github_api.files.get_file_content(
            dummy_repository,
            'dummyfiles/dummyauthor_not_exists.txt'
        )


def test_get_files(github_api, dummy_repository):
    files_info = github_api.files.get_files(
        dummy_repository,
        'dummyfiles'
    )

    files_found = set(f.get_name() for f in files_info)

    assert 'dummyauthor.txt' in files_found
    assert 'dummycrash.py' in files_found
