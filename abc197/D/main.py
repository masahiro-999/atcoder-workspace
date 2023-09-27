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


def solve(N,xy0, xy2):
    x0,y0 = xy0
    x2,y2 = xy2
    c_x, c_y = (x0+x2)/2, (y0+y2)/2
    c = cos(2*pi/N)
    s = sin(2*pi/N)
    x1 = (x0-c_x)*c-(y0-c_y)*s+c_x
    y1 = (x0-c_x)*s+(y0-c_y)*c+c_y
    print(x1,y1)


def main():
    N = int(next(tokens))
    xy0 = li()
    xy2 = li()
    solve(N,xy0, xy2)
    return

main()
