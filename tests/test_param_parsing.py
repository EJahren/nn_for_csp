from io import StringIO

import pytest

from neural_networks_for_csp._parse_param_input import (
    _read_header,
    _skip_comments,
    parse_param_file,
)


def test_read_header():
    _read_header(StringIO("language Essence 1.3\n"))
    with pytest.raises(ValueError, match="Unexpected header"):
        _read_header(StringIO("\n"))


def test_skip_comments():
    assert (
        _skip_comments(StringIO("$ comment\nletting n_cars be 100\n"))
        == "letting n_cars be 100\n"
    )


def test_that_each_problem_can_be_parsed(param_files):
    for file in param_files:
        parsed = parse_param_file(file)
        assert len(parsed[1]) > 0


def test_that_parsing_is_correct_for_small_example():
    inp = StringIO(
        """language Essence 1.3
$ This is instance 0 from Regin & Puget
$ It is *not* included in the data.txt file.
letting n_cars be 100
letting n_classes be 18
letting n_options be 5
letting maxcars be function (1 --> 1, 2 --> 2, 3 --> 1, 4 --> 2, 5 --> 1)
letting blksize be function (1 --> 2, 2 --> 3, 3 --> 3, 4 --> 5, 5 --> 5)
letting quantity be function (1 --> 5, 2 --> 3, 3 --> 7, 4 --> 1, 5 --> 10, 6 --> 2, 7 --> 11, 8 --> 5, 9 --> 4, 10 --> 6, 11 --> 12, 12 --> 1, 13 --> 1, 14 --> 5, 15 --> 9, 16 --> 5, 17 --> 12, 18 --> 1)
letting usage be relation ((1,1),(1,2),(1,5),(2,1),(2,2),(2,4),(3,1),(3,2),(3,3),(4,2),(4,3),(4,4),(5,1),(5,2),(6,1),(6,5),(7,1),(7,4),(8,1),(8,3),(9,2),(9,5),(10,2),(10,4),(11,2),(11,3),(12,3),(12,5),(13,3),(13,4),(14,1),(15,2),(16,5),(17,4),(18,3))
"""
    )
    assert parse_param_file(inp) == (
        [(1, 2), (2, 3), (1, 3), (2, 5), (1, 5)],
        [
            (5, [True, True, False, False, True]),
            (3, [True, True, False, True, False]),
            (7, [True, True, True, False, False]),
            (1, [False, True, True, True, False]),
            (10, [True, True, False, False, False]),
            (2, [True, False, False, False, True]),
            (11, [True, False, False, True, False]),
            (5, [True, False, True, False, False]),
            (4, [False, True, False, False, True]),
            (6, [False, True, False, True, False]),
            (12, [False, True, True, False, False]),
            (1, [False, False, True, False, True]),
            (1, [False, False, True, True, False]),
            (5, [True, False, False, False, False]),
            (9, [False, True, False, False, False]),
            (5, [False, False, False, False, True]),
            (12, [False, False, False, True, False]),
            (1, [False, False, True, False, False]),
        ],
    )
