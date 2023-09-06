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

MOD = 998244353

def solve(N: int, A: "List[int]"):
    # dp[i][j] = i番目までの数を使って、jにな個数
    dp = [[0] * 10 for _ in range(N)]
    def f(a,b):
        return (a + b) % 10
    def g(a,b):
        return (a * b) % 10
    dp[0][A[0]] = 1
    for i in range(1, N):
        for j in range(10):
            dp[i][f(j, A[i])] += dp[i - 1][j]
            dp[i][f(j, A[i])] %= MOD
            dp[i][g(j, A[i])] += dp[i - 1][j]
            dp[i][g(j, A[i])] %= MOD

    for i in range(10):
        print(dp[-1][i])
        

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)
    return

main()
