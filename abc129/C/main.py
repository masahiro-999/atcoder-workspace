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

MOD = 1000000007

def solve(N: int, M: int, a: "List[int]"):
    d = [0]*(N+1)
    d[0] = 1
    ng = set(a)
    for i in range(N):
        if i+1 < (N+1) and i+1 not in ng:
            d[i+1] += d[i]
            d[i+1] %= MOD
        if i+2 < (N+1) and i+2 not in ng:
            d[i+2] += d[i]
            d[i+2] %= MOD
    ans = d[N]
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, a)
    return

main()
