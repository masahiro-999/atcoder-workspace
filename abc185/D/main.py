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


def solve(N,M,A):
    A.sort()
    A.append(N+1)
    prev = 0
    len_of_white = []
    for a in A:
        l = a - prev - 1
        if l > 0:
            len_of_white.append(l)
        prev = a
    if len_of_white:
        k = min(len_of_white)
        ans = 0
        for l in len_of_white:
            ans += -((-l) // k)
    else:
        ans = 0
    print(ans)

def main():
    N = int(next(tokens))
    M = int(next(tokens))
    A = li()
    solve(N,M,A)
    return

main()
