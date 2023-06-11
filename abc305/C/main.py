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


def solve(H,W,a):
    dh = [False]*H
    dw = [False]*W
    for i in range(H):
        if "#" in a[i]:
            dh[i] = True 

    for j in range(W):
        for i in range(H):
            if a[i][j] == "#":
                dw[j] = True
    
    for i in range(H):
        if not dh[i]:
            continue
        for j in range(W):
            if not dw[j]:
                continue
            if a[i][j] == ".":
                return(i+1,j+1)

def main():
    H = int(next(tokens)) 
    W = int(next(tokens)) 
    s = [input() for _ in range(H)]
    i,j = solve(H,W,s)
    print(i,j)
    return

main()
