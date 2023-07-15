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

YES = "Yes"
NO = "No"

def solve(N, M, P, C, F):
    def is_ok(i,j):
        if not P[i] >= P[j]:
            return False
        for f in F[i]:
            if f not in F[j]:
                return False
        sj = set(F[j])
        si = set(F[i])
        iandj = sj & si
        return  P[i] > P[j] or (sj - iandj) 

    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            if is_ok(i,j):
                return YES
    return NO

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int

    P = [0] * N
    C = [0] * N
    F = [0] * N

    for i in range(N):
        P[i] = int(next(tokens))
        C[i] = int(next(tokens))
        F[i] = [int(next(tokens)) for _ in range(C[i])]

    print(solve(N, M, P, C, F))

    return
    solve()
    return

main()
