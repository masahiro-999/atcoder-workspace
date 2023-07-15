import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate, combinations
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


def solve(N,T,M,ab):
    table = {} 

    def create_comb(N,T)
    for x in product(range(T), repeat=N):
        for i,t in zip(range(N), x):
            table[i] = t

        ng = False
        for a in s:
            if len(s) == 0:
                ng = True
        if ng:
            continue

        

def main():
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    ab = [li() for _ in range(M)]
    solve(N,T,M,ab)
    return

main()
