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

def solve(S: str):
    l = len(S)
    if l == 1:
        ans = 0
    else:
        d = [[0]*(l+1) for _ in range(l)]
        # d[i][j] i文字目の(の数
        if S[0] == "(" or S[0] == "?":
            d[0][1] = 1
        for i in range(l-1):
            for j in range(l):
                if S[i+1] == "(" or S[i+1] == "?":
                    d[i+1][j+1] += d[i][j]
                    d[i+1][j+1] %= MOD
                if (S[i+1] == ")" or S[i+1] == "?") and j >= 1:
                    d[i+1][j-1] += d[i][j]
                    d[i+1][j-1] %= MOD
        ans = d[l-1][0]
    print(ans)

def main():
    S = next(tokens)  # type: str
    solve(S)
    return

main()
