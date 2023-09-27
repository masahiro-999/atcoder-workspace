import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
from abc215.D.main import solve

import pytest
import random
from math import gcd

def test_solve(capsys):
    N = 1000
    M = 100000
    A = [random.randint(1,100000) for _ in range(N)]
    start = time.perf_counter()
    solve(N,M,A)
    end = time.perf_counter()
    out, _ = capsys.readouterr()
    out_list = list(map(int, out.split()))
    assert out_list[0] == len(out_list)-1
    for k in out_list[1:]:
        for a in A:
            assert gcd(a,k) == 1

    # print(f"elapsed_time:{end-start}")
    # assert end-start ==0