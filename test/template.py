import time
import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush

import random

from abcxxx.D.main import solve

def test_solve(capsys):
    # a = [random.randint(1,100000) for _ in range(1000)]
    start = time.perf_counter()
    solve()
    end = time.perf_counter()

    out, _ = capsys.readouterr()
    out_list = list(map(int, out.split()))

    # print(f"elapsed_time:{end-start}")
