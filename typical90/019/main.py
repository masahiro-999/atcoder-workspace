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


def solve(N: int, A: "List[int]"):

    a = A[:]
    sum_d = 0
    while a:
        d = [abs(a[i]-a[i+1]) for i in range(len(a)-1)]
        min_d = min(d)
        sum_d += min_d
        min_i = d.index(min_d)
        a = a[:min_i] + a[min_i+2:]

    print(sum_d)

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    solve(N, A)
    return

main()
