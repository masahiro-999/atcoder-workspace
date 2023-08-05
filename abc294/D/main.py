import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
try:
    from pypyjit import set_param
    set_param('max_unroll_recursion=-1')
except ModuleNotFoundError:
    pass
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())


def solve(N,Q,e_list):
    not_called = [i for i in range(1,N+1)]
    heapify(not_called)
    called = []
    done = set()
    for e in e_list:
        if e[0] == 1:
            a = heappop(not_called)
            heappush(called, a)
        elif e[0] == 2:
            done.add(e[1])
        else:
            # e[0] == 3:
            while called[0] in done:
                heappop(called)
            print(called[0])



def main():
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    e = [0] * Q
    for i in range(Q):
        e[i] = li()
    solve(N,Q,e)
    return

main()
