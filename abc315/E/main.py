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


def solve(N,P):
    def f(n):
        for x in P[n-1]:
            if x not in has_read:
                has_read.add(x)
                f(x)
        ans.append(n)

    has_read = set()
    ans = []
    f(1)
    ans = ans[:-1]
    print(*ans)

def main():
    N = int(next(tokens))  # type: int
    P = []
    for i in range(N):
        c = int(next(tokens))
        p = [int(next(tokens)) for _ in range(c)]
        P.append(p)
    
    solve(N,P)
    return

main()
