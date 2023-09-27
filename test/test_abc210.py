import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush

import random

from abc210.D.main import solve

def test_solve(capsys):
    # a = [random.randint(1,100000) for _ in range(1000)]
    H = 10
    W = 10
    C = 100
    A = [[random.randint(1,1000000000) for _ in range(W)] for _ in range(H)]    
    # A = [[1,2,3,4,5,6,7,8,9,10]]   
    start = time.perf_counter()
    ret = solve(H, W, C, A)
    end = time.perf_counter()

    out, _ = capsys.readouterr()
    out_list = list(map(int, out.split()))

    ans = 2<<63-1
    for i in range(H):
        for j in range(W):
            for k in range(i, H):
                for l in range(j, W):
                    if i == k and j == l:
                        continue
                    ans = min(ans, C*(abs(k-i)+abs(l-j))+A[i][j]+A[k][l])
    assert ret == ans
    # print(f"elapsed_time:{end-start}")
