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


def solve(N: int, M: int, C: "List[str]", D: "List[str]", P: "List[int]"):
    def price(str):
        try:
            i = D.index(str)
            return P[i+1]
        except:
            return P[0]

    s = 0
    for c in C:
        s += price(c)
    print(s)
    
def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    C = [next(tokens) for _ in range(N)]  # type: "List[str]"
    D = [next(tokens) for _ in range(M)]  # type: "List[str]"
    P = [int(next(tokens)) for _ in range(M + 1)]  # type: "List[int]"
    solve(N, M, C, D, P)
    return

main()
