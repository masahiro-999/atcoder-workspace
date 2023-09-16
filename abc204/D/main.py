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


def solve(N: int, T: "List[int]"):
    total = sum(T)
    half = total // 2
    dp = [False] * (half + 1)
    dp[0] = True
    for t in T:
        for i in range(half, t - 1, -1):
            dp[i] |= dp[i - t]
    for i in range(half, -1, -1):
        if dp[i]:
            print(total - i)
            return  
def main():
    N = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T)
    return

main()
