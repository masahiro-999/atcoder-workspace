import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())


def solve(N: int, dcs):
    dcs.sort(key=lambda x:x[0])
    max_d = dcs[-1][0]
    dp = [[0]*(max_d+1) for _ in range(N+1)]
    # dp[i][j] 仕事iまで　jは仕事の合計日数
    for i in range(1,N+1):
        d,c,s = dcs[i-1]
        for j in range(1,max_d+1):
            if c > j or j > d:
                # 仕事がはいらない
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-c]+s)
    ans = max(dp[N])
    print(ans)
  
def main():
    N = int(next(tokens))  # type: int
    dcs = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        dcs[i] = (int(next(tokens)), int(next(tokens)), int(next(tokens)))
    solve(N, dcs)
    return

main()
