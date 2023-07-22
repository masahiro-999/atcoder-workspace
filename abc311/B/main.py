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


def solve(N: int, D: int, S: "List[str]"):
    s = [0] * D
    for i in range(N):
        for j in range(D):
            if S[i][j] == "x":
                s[j] = 1

    n = 0
    ans = 0
    for i in range(D):
        if s[i] == 0:
            n += 1
        else:
            ans = max(ans, n)
            n = 0
    ans = max(ans, n)
    print(ans)


def main():
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, D, S)
    return

main()
