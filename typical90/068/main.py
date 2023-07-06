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


def solve(N: int, Q: int, T: "List[int]", X: "List[int]", Y: "List[int]", V: "List[int]"):

def main():
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    T = [int()] * (Q)  # type: "List[int]"
    X = [int()] * (Q)  # type: "List[int]"
    Y = [int()] * (Q)  # type: "List[int]"
    V = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, Q, T, X, Y, V)
    return

main()
