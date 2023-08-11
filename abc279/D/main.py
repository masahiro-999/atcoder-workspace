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


def solve(A: int, B: int):
    def f(n):
        return -A*A+4*B*B*(1+n)**3
    l = 0
    r = 1
    while f(r)<0:
        r = r*2
    while r-l > 1:
        mid = (r+l)//2
        if f(mid) > 0:
            r = mid
        else:
            l = mid
    ans1 = A/sqrt(1+r)+r*B
    ans2 = A/sqrt(1+l)+l*B
    ans = min(ans1, ans2)
    print(ans)

def main():
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)
    return

main()
