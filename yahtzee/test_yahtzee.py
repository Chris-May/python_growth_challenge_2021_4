import pytest

from .yahtzee import *


@pytest.mark.parametrize(
    'roll, category, expected_score', [
        ([1, 1, 1, 1, 1], 'ones', 5),
        ([2, 2, 2, 2, 2], 'twos', 10),
        ([2, 2, 2, 2, 4], 'twos', 8),
        ([1, 2, 3, 4, 5], 'threes', 3),
        ([1, 1, 2, 4, 4], 'fours', 8),
        ([1, 1, 2, 2, 3], 'fours', 0),
        ([3, 4, 5, 1, 5], 'fives', 10),
        ([1, 2, 6, 6, 6], 'sixes', 18),
        ([3, 3, 3, 4, 5], 'three of a kind', 18),
        ([2, 2, 2, 2, 5], 'four of a kind', 13),
        ([1, 1, 2, 3, 4], 'small straight', 30),
        ([1, 1, 2, 3, 6], 'small straight', 0),
        ([2, 3, 4, 5, 6], 'large straight', 40),
        ([2, 5, 4, 5, 6], 'large straight', 0),
        ([1, 1, 2, 2, 2], 'full house', 25),
        ([1, 1, 3, 2, 2], 'full house', 0),
        ([3, 3, 3, 3, 3], 'yahtzee', 50),
        ([1, 1, 3, 2, 2], 'yahtzee', 0),
        ([1, 1, 3, 2, 2], 'chance', 9),
    ])
def test_yahtzee(roll, category, expected_score):
    result = score_roll(roll, category)
    assert result == expected_score
