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

    

def solve(H,W,ab):
    dp = [[-inf] * W for _ in range(H)]
    dp[-1][-1] = 0
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if i == H-1 and j == W-1:
                continue
            if j != W-1:
                dp[i][j] = max(dp[i][j], ab[i][j+1] - dp[i][j+1])
            if i != H-1:
                dp[i][j] = max(dp[i][j], ab[i+1][j] - dp[i+1][j])

    # @lru_cache(None)
    # def f(i,j):
    #     if i == H-1 and j == W-1:
    #         ret = 0
    #     else:
    #         ret = -inf
    #         if j != W-1:
    #             ret = max(ret, ab[i][j+1] - f(i,j+1))
    #         if i != H-1:
    #             ret = max(ret, ab[i+1][j] - f(i+1,j))
    #     return ret

    ans = dp[0][0]
    if ans == 0:
        print("Draw")
    elif ans > 0:
        print("Takahashi")
    else:
        print("Aoki")

def main():
    H = int(next(tokens))
    W = int(next(tokens))
    ab = [[1 if a=="+" else -1 for a in next(tokens)] for _ in range(H)]
    solve(H,W,ab)
    return

main()
