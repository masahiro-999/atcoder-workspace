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


def solve(N: int, X: int, Y: int, A: "List[int]", B: "List[int]"):
    # dp[i][x][y] = i番目までの弁当を買って、たこ焼きの数がｘタイ焼きの数がyの時のお弁当の数
    dp = [[[inf] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(1,N+1):
        for x in range(X+1):
            for y in range(Y+1):
                # i番目のお弁当を買わない場合
                dp[i][x][y] = min(dp[i][x][y], dp[i-1][x][y])
                # i番目のお弁当を買う場合
                dp[i][min(x+A[i-1],X)][min(y+B[i-1],Y)] = min(dp[i][min(x+A[i-1],X)][min(y+B[i-1],Y)], dp[i-1][x][y]+1)

    ans = dp[N][X][Y]
    if ans == inf:
        ans = -1
    print(ans)
    return


def main():
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, X, Y, A, B)
    return

main()
