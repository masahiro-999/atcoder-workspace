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


def solve(N: int, X: "List[int]", Y: "List[int]"):
    # d[i][m] i番目まできた。m==0 正常　m==1 毒状態
    d = [[0]*2 for _ in range(N)]

    if X[0] == 0:
        d[0][0] = max(0,Y[0])
        d[0][1] = -inf
    else:
        d[0][0] = 0
        d[0][1] = Y[0]

    for i in range(1,N):
        x = X[i]
        y = Y[i]
        if x == 0:
            d[i][0] = max(d[i-1][0], d[i-1][1]+y, d[i-1][0]+y)
            d[i][1] = d[i-1][1]

        else:
            d[i][0] = d[i-1][0]
            d[i][1] = max(d[i-1][1], d[i-1][0]+y)

    ans = max(d[N-1])
    print(ans)


def main():
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, X, Y)
    return

main()
