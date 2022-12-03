from pathlib import Path

import pytest

from script import (
    get_score_for_round,
    get_score_for_round_part2,
    get_total_score_for_all_rounds,
)

BASE_DIR = Path(__file__).parent


@pytest.fixture
def guide():
    return (BASE_DIR / "input.txt").read_text()


@pytest.mark.parametrize(
    "line, expected",
    [
        ("A Y", 8),
        ("B X", 1),
        ("C Z", 6),
    ],
)
def test_scores(line, expected):
    assert get_score_for_round(line) == expected


def test_total_score():
    lines = "A Y\nB X\nC Z".splitlines()
    assert get_total_score_for_all_rounds(lines) == 15


def test_total_score_from_input_file(guide):
    lines = guide.splitlines()
    assert get_total_score_for_all_rounds(lines) == 10310


@pytest.mark.parametrize(
    "line, expected",
    [
        ("A Y", 4),
        ("B X", 1),
        ("C Z", 7),
    ],
)
def test_scores_part2(line, expected):
    assert get_score_for_round_part2(line) == expected


def test_total_score_part2():
    lines = "A Y\nB X\nC Z".splitlines()
    assert get_total_score_for_all_rounds(lines, func=get_score_for_round_part2) == 12


def test_total_score_from_input_file_part2(guide):
    lines = guide.splitlines()
    assert (
        get_total_score_for_all_rounds(lines, func=get_score_for_round_part2) == 14859
    )
