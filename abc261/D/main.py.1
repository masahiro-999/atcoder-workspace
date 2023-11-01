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


def solve(N: int, M: int, X: "List[int]", C: "List[int]", Y: "List[int]"):
    bonus = defaultdict(int)
    for c,y in zip(C,Y):
        bonus[c] = y

    dp = [[-1]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1,N+1):
        # j = コイントスする前のカウンター値
        for j in range(N+1):
            if dp[i-1][j] != -1:
                # 表が出た時
                dp[i][j+1] = max(dp[i][j+1], dp[i-1][j] + X[i-1] + bonus[j+1])
                # 裏が出た時
                dp[i][0] = max(dp[i][0], dp[i-1][j])

    ans = max(dp[N])
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        C[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, X, C, Y)
    return

main()
