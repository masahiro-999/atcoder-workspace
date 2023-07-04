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


def solve(N: int, T: int, t: "List[int]"):
    sum_t = 0
    for i in range(N-1):
        d = t[i+1] - t[i]
        if d < T:
            sum_t += d
        else:
            sum_t += T

    sum_t += T
    print(sum_t)

def main():
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    t = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, t)
    return

main()
