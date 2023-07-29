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


def solve(x: int, y: int):
    def get_ans(x,y):
        if x*y == 0:
            if x < y:
                return y-x
            else:
                return x-y+1
        elif x*y > 0:
            if x < y:
                return y-x
            else:
                return x-y+2
        else:
            return abs(x+y)+1
    ans  = get_ans(x,y)
    print(ans)

def main():
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(x, y)
    return

main()
