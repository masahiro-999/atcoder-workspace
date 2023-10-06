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

from abc181.D.main import solve

def test_solve(capsys):
    # a = [random.randint(1,100000) for _ in range(1000)]
    start = time.perf_counter()
    N = "33333221"
    solve(N)
    end = time.perf_counter()

    out, _ = capsys.readouterr()

    out_list = out.split()

    assert out_list[0] == "Yes"
