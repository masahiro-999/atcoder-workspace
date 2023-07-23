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


def solve(N: int, C: int, K: int, T: "List[int]"):
    T.sort()
    ans = 0
    start_bus = None
    num_bus = 0
    for t in T:
        num_bus += 1
        if start_bus is None:
            start_bus = t
        if num_bus > C or t > start_bus + K:
            ans += 1
            start_bus = t
            num_bus = 1
    if num_bus >0:
        ans += 1
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, C, K, T)
    return

main()


2

6
6
7
8

10