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


def solve(N, a, X):
    b = [(len(a[i]),i) for i in range(N) if X in a[i]]
    b.sort()
    c = [i+1 for (l,i) in b if l == b[0][0]]
    print(len(c))
    if c:
        print(*c)


def main():
    N = int(next(tokens))  # type: int
    a = [0]*N
    for i in range(N):
        C = int(next(tokens))
        a[i] = li()
    X = int(next(tokens))  # type: int

    solve(N,a,X)
    return

main()
