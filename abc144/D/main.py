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


def solve(a: int, b: int, x: int):
    x1 = a*a*b/2
    if x1 < x:
        s = atan2(2*(a*a*b-x), a*a*a)*180/pi
    else:
        s = atan2(b*b*a/2, x)*180/pi
    print(s)



def main():
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    solve(a, b, x)
    return

main()
