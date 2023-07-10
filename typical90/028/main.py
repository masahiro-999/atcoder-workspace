import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())


def solve(N: int, lx_list: "List[int]", ly_list: "List[int]", rx_list: "List[int]", ry_list: "List[int]"):
    def get_v(d,i):
        return [d[x][i] for x in range(1001)]

    d = [[0]*1001 for _ in range(1001)]
    for lx,ly,rx,ry in zip(lx_list, ly_list, rx_list, ry_list):
        d[ly][lx] += 1
        d[ly][rx] += -1
        d[ry][lx] += -1
        d[ry][rx] += 1

    d1 = [list(accumulate(d[i])) for i in range(1001)]
    d2 = [list(accumulate(get_v(d1,i))) for i in range(1001)]

    c = Counter()
    for i in range(1001):        
        for j in range(1001):
            c[d2[i][j]] += 1
    for i in range(1, N+1):
        print(c[i])        
    

def main():
    N = int(next(tokens))  # type: int
    lx = [int()] * (N)  # type: "List[int]"
    ly = [int()] * (N)  # type: "List[int]"
    rx = [int()] * (N)  # type: "List[int]"
    ry = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        lx[i] = int(next(tokens))
        ly[i] = int(next(tokens))
        rx[i] = int(next(tokens))
        ry[i] = int(next(tokens))
    solve(N, lx, ly, rx, ry)
    return

main()
