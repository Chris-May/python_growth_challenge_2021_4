import pytest

from .tennis import *


@pytest.mark.parametrize('points_scored, expected', [
    ((0,0), 'love love'),
    ((1, 0), 'fifteen love'),
    ((1, 1), 'fifteen fifteen'),
    ((2, 1), 'thirty fifteen'),
    ((3, 1), 'forty fifteen'),
    ((4, 1), 'Player one won'),
    ((4, 1), 'Player one won'),
    ((4, 4), 'deuce'),
    ((4, 5), 'advantage player two'),
    ((6, 7), 'advantage player two'),
    ((7, 7), 'deuce'),
    ((9, 7), 'Player one won'),
])
def test_score(points_scored, expected):
    result = tennis_score(*points_scored)
    assert result == expected
