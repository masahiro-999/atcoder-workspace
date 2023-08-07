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

MOD = 4

def solve(queue):
    for [n, d, k] in queue:
        d = d % n
        w = (n-1)//d+1
        if w == 0:
            w = 1
        a = (k-1) // w
        b = (k-1) % w
        ans = a + d*b
        print(ans)

def main():
    Q = int(next(tokens))  # type: int
    q = [li() for _ in range(Q)]
    solve(q)
    return

main()
