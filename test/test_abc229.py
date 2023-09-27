import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from abc229.D.main import solve

import pytest
from itertools import accumulate
from bisect import bisect_right

@pytest.mark.parametrize("S, K, expected", [
    ("X.X.X", 2, 5),
    ("X.X.X", 3, 5),
    (".X.X..X...X....X.....", 1, 3),
    (".X.X..X...X....X.....", 2, 4),
    (".X.X..X...X....X.....", 3, 6),
    (".X.X..X...X....X.....", 4, 7),
    (".X.X..X...X....X.....", 5, 8),
    (".X.X..X...X....X.....", 6, 10),
])
def test_solve(S, K, expected):
    assert solve(S, K)==expected

@pytest.mark.parametrize("S, K, expected", [
    (".X.X..X...X....X.....", 1, 3),
    (".X.X..X...XXX...X.....", 3, 7),
    (".X.X..X...XXX...XX.....", 3, 8),
    (".XXXX.X..X...XXX...XX.....", 3, 9),
])
def test_solve_XXX(S, K, expected):
    assert solve(S, K)==expected

@pytest.mark.parametrize("S, K, expected", [
    (".", 6, 1),
    ("...", 1, 1),
    ("...", 2, 2),
    ("...", 3, 3),
    ("...", 4, 3),
    ("...", 5, 3),
])
def test3_solve_only_dot(S, K, expected):
    assert solve(S, K)==expected


@pytest.mark.parametrize("S, K, expected", [
    ("X", 6, 1),
    ("XXX", 1, 3),
    ("XXX", 2, 3),
    ("XXX", 3, 3),
    ("XXX", 4, 3),
    ("XXX", 5, 3),
])
def test_solve_only_x(S, K, expected):
    assert solve(S, K)==expected
