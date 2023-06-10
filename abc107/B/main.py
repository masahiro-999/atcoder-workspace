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
    i = 0
    while i < len(a[0]):
        flag = True
        for j in range(H):
            if a[j][i]=="#":
                flag = False
                break
        if flag:
            for j in range(H):
                a[j] = a[j][:i]+a[j][i+1:]
        else:
            i+=1
    a = filter(lambda x: x.find("#") != -1, a)
    for i in a:
        print(i)

def main():
    H = int(next(tokens)) 
    W = int(next(tokens)) 
    a = [input() for _ in range(H)]
    solve(H,W,a)
    return

main()
