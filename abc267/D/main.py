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


def solve(N: int, M: int, A: "List[int]"):
    dp = [[-inf]*(M+1) for _ in range(N+1)]

    dp[0][0] = 0
    for i in range(1,N+1):
        for j in range(0,M+1):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j > 0 and dp[i-1][j-1] != -inf:
                # 加える場合
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+A[i-1]*j)

    ans = dp[N][M]
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)
    return

main()
