from pathlib import Path

import pytest

from neural_networks_for_csp._parse_txt_input import parse_txt_input, show_problem


def test_that_each_problem_can_be_parsed(big_data_set_files):
    for file in big_data_set_files:
        parsed = parse_txt_input(Path(file).read_text())
        assert len(parsed[1]) > 0


def test_that_parsing_and_writing_are_inverse(big_data_set_files):
    for file in big_data_set_files:
        print(file)
        content = Path(file).read_text()
        # Remove trailing space and add
        # eof endline from file
        normalized = content.replace(" \n", "\n")
        if normalized[-1] != "\n":
            normalized += "\n"
        assert show_problem(parse_txt_input(content)) == normalized


def test_that_parsing_produces_good_result_for_simple_example():
    assert parse_txt_input("20 2 2\n1 2\n3 4\n0 11 0 1\n1 9 1 0\n") == (
        [(1, 3), (2, 4)],
        [(11, [False, True]), (9, [True, False])],
    )


def test_that_missing_header_gives_error():
    with pytest.raises(ValueError, match="Missing header"):
        parse_txt_input("")


def test_that_short_header_gives_error():
    with pytest.raises(ValueError, match="Header line"):
        parse_txt_input("1 2")


def test_that_too_few_options_give_error():
    with pytest.raises(ValueError, match="number of options"):
        parse_txt_input("10 2 2\n1\n2 2\n")


def test_that_too_few_classes_give_error():
    with pytest.raises(ValueError, match="number of classes"):
        parse_txt_input("10 2 2\n1 1\n2 2\n0 10 1 1\n")


def test_that_too_few_cars_give_error():
    with pytest.raises(ValueError, match="number of cars"):
        parse_txt_input("10 2 2\n1 1\n2 2\n0 1 1 1\n1 0 0\n")
