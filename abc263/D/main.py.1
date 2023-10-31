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


def solve(N: int, L: int, R: int, A: "List[int]"):
    b = [a-L for a in A]
    # c = sum(bi)の最大値
    c = [0]*(N+1)
    c[0] = 0
    sum_b = 0
    for i in range(0,N):
        sum_b += b[i]
        c[i+1] = max(c[i], sum_b)
    
    a = [0] + list(accumulate(A))
    x = inf
    for r in range(N+1):
        x = min(x, a[r] - c[r] + (N-r)*R)

    print(x)


def main():
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L, R, A)
    return

main()
