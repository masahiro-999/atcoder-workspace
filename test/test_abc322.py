import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
import re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush

import random

from abc322.D.main import rot,create_set,moved_ply

def test_rot(capsys):
    assert rot(0,0,1) == (0,3)
    assert rot(0,0,2) == (3,3)
    assert rot(0,0,3) == (3,0)
    assert rot(0,0,0) == (0,0)

def test_create_set():
    p = [
        "....",
        "###.",
        ".#..",
        "...."
    ]
    assert create_set(p) == {(1, 0), (1, 1), (1, 2), (2, 1)}
