from findcrashedcodedeveloper.utilities.filepath import (
    get_all_possible_repository_paths
)


def test_get_all_possible_repository_paths():
    absolute_filepath = '/a/b/c/d/a/a/b/a.txt'
    possible_paths = get_all_possible_repository_paths(absolute_filepath, 'a')
    assert possible_paths == ['b/c/d/a/a/b/a.txt', 'a/b/a.txt', 'b/a.txt']
