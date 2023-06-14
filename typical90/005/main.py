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

MOD = 1000000007

def solve(N: int, B: int, K: int, c: "List[int]"):
    dp = [[0]*B for _ in range(N)]
    for c1 in c:
        dp[0][c1%B] += 1 
    for i in range(1,N):
        for j in range(B):
            for c1 in c:
                next = (j*10+c1)%B
                dp[i][next] += dp[i-1][j]
                dp[i][next] %= MOD
    count = dp[N-1][0]
    print(count)

def main():
    N = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    c = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, B, K, c)
    return

main()
