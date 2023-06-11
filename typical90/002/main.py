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


def solve(N: int):
    def is_OK(s):
        c = 0
        for i in s:
            if i == "(":
                c+= 1
            else:
                c-= 1
            if c <0:
                return False
        return c==0

    for p in product(["(",")"], repeat=N):
        if is_OK(p):
            print("".join(p))


def main():
    N = int(next(tokens))  # type: int
    solve(N)
    return

main()
