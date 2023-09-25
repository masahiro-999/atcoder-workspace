import time
import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush

import random

from abc200.D.main import solve

def test_solve(capsys):
    N = 100
    a = [random.randint(1,200) for _ in range(N)]
    start = time.perf_counter()
    solve(N,a)
    end = time.perf_counter()

    out, _ = capsys.readouterr()
    ret  = out.split("\n")
    assert ret[0] == "Yes"
    b_list = ret[1]
    c_list = ret[2]
    b_list = list(map(int, b_list.split()))
    c_list = list(map(int, c_list.split()))

    b = b_list[1:]
    c = c_list[1:]
    sum_b = sum([a[x-1] for x in b])
    sum_c = sum([a[x-1] for x in c])
    assert sum_b % 200 == sum_c % 200
    assert b != c


def test_solve_lot_of_samevalue(capsys):
    N = 100
    a = [random.randint(1,2) for _ in range(N)]
    start = time.perf_counter()
    solve(N,a)
    end = time.perf_counter()

    out, _ = capsys.readouterr()
    ret  = out.split("\n")
    assert ret[0] == "Yes"
    b_list = ret[1]
    c_list = ret[2]
    b_list = list(map(int, b_list.split()))
    c_list = list(map(int, c_list.split()))

    b = b_list[1:]
    c = c_list[1:]
    sum_b = sum([a[x-1] for x in b])
    sum_c = sum([a[x-1] for x in c])
    assert sum_b % 200 == sum_c % 200
    assert b != c

def test_solve_large_value(capsys):
    N = 100
    a = [random.randint(1,1000000000) for _ in range(N)]
    start = time.perf_counter()
    solve(N,a)
    end = time.perf_counter()

    out, _ = capsys.readouterr()
    ret  = out.split("\n")
    assert ret[0] == "Yes"
    b_list = ret[1]
    c_list = ret[2]
    b_list = list(map(int, b_list.split()))
    c_list = list(map(int, c_list.split()))

    b = b_list[1:]
    c = c_list[1:]
    sum_b = sum([a[x-1] for x in b])
    sum_c = sum([a[x-1] for x in c])
    assert sum_b % 200 == sum_c % 200
    assert b != c

def test_N_2(capsys):
    N = 2
    a = [2,2]
    start = time.perf_counter()
    solve(N,a)
    end = time.perf_counter()

    out, _ = capsys.readouterr()
    ret  = out.split("\n")
    assert ret[0] == "Yes"
    b_list = ret[1]
    c_list = ret[2]
    b_list = list(map(int, b_list.split()))
    c_list = list(map(int, c_list.split()))

    b = b_list[1:]
    c = c_list[1:]
    sum_b = sum([a[x-1] for x in b])
    sum_c = sum([a[x-1] for x in c])
    assert sum_b % 200 == sum_c % 200
    assert b != c


def test_N_2_No(capsys):
    N = 2
    a = [1,2]
    start = time.perf_counter()
    solve(N,a)
    end = time.perf_counter()

    out, _ = capsys.readouterr()
    ret  = out.split("\n")
    assert ret[0] == "No"

def test_testcase13(capsys):
    a = [
        594881561,
        676552199,
        623563589,
        67350035,
        491719004,
        930740354,
        49510901,
        365531333
        ]
    N = len(a)
    start = time.perf_counter()
    solve(N,a)
    end = time.perf_counter()

    out, _ = capsys.readouterr()
    ret  = out.split("\n")
    assert ret[0] == "Yes"
    b_list = ret[1]
    c_list = ret[2]
    b_list = list(map(int, b_list.split()))
    c_list = list(map(int, c_list.split()))

    b = b_list[1:]
    c = c_list[1:]
    sum_b = sum([a[x-1] for x in b])
    sum_c = sum([a[x-1] for x in c])
    assert b_list[0] > 0
    assert c_list[0] > 0
    assert sum_b % 200 == sum_c % 200
    assert b != c


