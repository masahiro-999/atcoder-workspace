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
ti = lambda: tuple(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())


def solve(N,M,Q,wv,x_list,lr):
    def get_max_v_less_x(x,used):
        max_v = 0
        max_i = 0
        for i,(w,v) in enumerate(wv):
            if i in used:
                continue
            if w > x:
                break
            if max_v < v:
                max_v = v
                max_i = i
        if max_v != 0:
            used.add(max_i)
        return max_v
    
    def f(l,r):
        sum_v = 0
        used = set()
        for x,i in sort_x:
            if l<=i<=r:
                continue
            sum_v += get_max_v_less_x(x,used)
        return sum_v
    sort_x = [(v,i) for i,v in enumerate(x_list)]
    sort_x.sort()
    wv.sort()
    for l,r in lr:
        print(f(l-1,r-1))


def main():
    N = int(next(tokens))
    M = int(next(tokens))
    Q = int(next(tokens))
    wv = [ti() for _ in range(N)]
    x_list = li()
    lr = [ti() for _ in range(Q)]
    solve(N,M,Q,wv,x_list,lr)
    return

main()
