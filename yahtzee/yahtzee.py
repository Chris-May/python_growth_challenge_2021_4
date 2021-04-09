from collections import Counter
from functools import partial
from typing import List


def score_roll(roll: List[int], category: str) -> int:
    return category_mapper.get(category, sum)(roll)


def count_and_multiply(amount: int, roll: List[int]) -> int:
    return roll.count(amount) * amount


def sm_straight(roll: List[int]) -> int:
    min_roll, max_roll = min(roll), max(roll)
    min_range = range(min_roll, min_roll + 4)
    max_range = range(max_roll - 4, max_roll)
    roll = set(roll)
    if roll == set(min_range) or roll == set(max_range):
        return 30
    return 0


def lg_straight(roll: List[int]) -> int:
    roll_set = set(roll)
    low_range = set(range(1, 6))
    high_range = set(range(2, 7))
    if roll_set == low_range or roll_set == high_range:
        return 40
    return 0


def full_house(roll: List[int]) -> int:
    c = Counter(roll)
    if set(c.values()) == {3, 2}:
        return 25
    return 0


def check_yahtzee(roll: List[int]) -> int:
    first = roll[0]
    if all(die == first for die in roll):
        return 50
    return 0


category_mapper = {
    'ones': partial(count_and_multiply, 1),
    'twos': partial(count_and_multiply, 2),
    'threes': partial(count_and_multiply, 3),
    'fours': partial(count_and_multiply, 4),
    'fives': partial(count_and_multiply, 5),
    'sixes': partial(count_and_multiply, 6),
    'small straight': sm_straight,
    'large straight': lg_straight,
    'full house': full_house,
    'yahtzee': check_yahtzee,
    'chance': sum
}
