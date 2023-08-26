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


def solve(N: int):
    def f(a,b):
        return a**3+a*a*b+a*b*b+b**3
    
    def find(b, mx):
        l = 0
        r = mx
        while r-l > 1:
            a = (r+l)//2
            if a**3+a*a*b+a*b*b+b**3-N <0:
                l = a
            else:
                r = a
        return r 

    mx_a = find(0, N)
    ans = inf
    for a in range(0,mx_a+1):
        b = find(a, mx_a)
        x = a**3+a*a*b+a*b*b+b**3
        ans = min(ans,x)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    solve(N)
    return

main()
