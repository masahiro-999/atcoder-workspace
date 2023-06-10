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

def solve(N: int, Q: int, x: "List[int]", y: "List[int]", z: "List[int]", w: "List[int]"):

def main():
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    z = [int()] * (Q)  # type: "List[int]"
    w = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        z[i] = int(next(tokens))
        w[i] = int(next(tokens))
    solve(N, Q, x, y, z, w)
    return

main()
