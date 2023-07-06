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


def solve(H: int, W: int, A: "List[List[int]]"):
    def sumh(x):
        return sum([A[x][i] for i in range(W)])

    def sumv(x):
        return sum([A[i][x] for i in range(H)])

    sumh_list = [sumh(i) for i in range(H)]
    sumv_list = [sumv(j) for j in range(W)]
    for i in range(H):
        line = []
        for j in range(W):
            line.append(sumh_list[i]+sumv_list[j]-A[i][j])
        print(*line)

def main():
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, A)
    return

main()
