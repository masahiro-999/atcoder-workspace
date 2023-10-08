import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate,permutations,combinations
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

MOD = 1000000007

def solve(S: int):
    if S < 3:
        print(0)
        return
    dp = [0]*(S+1)
    dp[0] = 1
    for i in range(3,S+1):
        for j in range(3,S+1):
            if i-j <0:
                break
            dp[i] += dp[i-j]
            dp[i] %= MOD
    ans = dp[S]
    print(ans)

def main():
    S = int(next(tokens))  # type: int
    solve(S)
    return

main()
