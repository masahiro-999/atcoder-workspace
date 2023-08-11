import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect_left
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


def solve(H,W,rs,cs,N,rc,Q,dl):
    def limit_horizontal(r,c):
        return limit_sub(r,c,r_list,W)

    def limit_vertical(r,c):
        return limit_sub(c,r,c_list,H)

    def limit_sub(r,c,list,mx):
        if list[r] == []:
            return(1,mx)
        i = bisect_left(list[r],c)
        right = list[r][i]-1
        left = list[r][i-1]+1
        return(left, right)

    r_list = defaultdict(list)
    c_list = defaultdict(list)
    for r,c in rc:
        r_list[r].append(c)
        c_list[c].append(r)
    for k in r_list.keys():
        r_list[k].append(0)
        r_list[k].append(W+1)
        r_list[k].sort()
    for k in c_list.keys():
        c_list[k].append(0)
        c_list[k].append(H+1)
        c_list[k].sort()

    r = rs
    c = cs
    for d,l in dl:
        if d == "L":
            limit,_ = limit_horizontal(r,c)
            c = max(c-l, limit)
        elif d == "R":
            _, limit = limit_horizontal(r,c)
            c = min(c+l, limit)
        elif d == "U":
            limit,_ = limit_vertical(r,c)
            r = max(r-l, limit)
        elif d == "D":
            _, limit = limit_vertical(r,c)
            r = min(r+l, limit)
        print(r,c)


def main():
    def get_dl():
        [d,l] = input().split()
        return (d, int(l))
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    rs = int(next(tokens))  # type: int
    cs = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    rc = [li() for _ in range(N)]
    Q = int(next(tokens))  # type: int
    dl = [get_dl() for _ in range(Q)]

    solve(H,W,rs,cs,N,rc,Q,dl)
    return

main()
