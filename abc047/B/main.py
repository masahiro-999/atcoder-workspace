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


def solve(W: int, H: int, N: int, x_list: "List[int]", y_list: "List[int]", a_list: "List[int]"):
    d = [[0]*(W) for _ in range(H)]
    for x,y,a in zip(x_list, y_list, a_list):
        if a == 1:
            d[0][0] += 1
            if x < W:
                d[0][x] += -1
        elif a == 2:
            if x < W:
                d[0][x] += 1
        elif a == 3:
            d[0][0] += 1
            if y < H:
                d[y][0] -= 1
        elif a == 4:
            if y < H:
                d[y][0] += 1
    for i in range(H):
        for j in range(1,W):
            d[i][j] += d[i][j-1]

    for j in range(W):
        for i in range(1,H):
            d[i][j] += d[i-1][j]

    ans = 0
    for j in range(W):
        for i in range(H):
            if d[i][j] == 0:
                ans += 1
    print(ans)

def main():
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    a = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        a[i] = int(next(tokens))
    solve(W, H, N, x, y, a)
    return

main()
