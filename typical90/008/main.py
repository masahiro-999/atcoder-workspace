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

MOD = 1000000007

def solve(N: int, S: str):
    str="atcoder"
    d = [[0]*7 for _ in range(N)]
    s = [x for x in S if x in str]
    for i in range(len(s)-1,-1,-1):
        if i != len(s)-1:
            d[i] = d[i+1][:]
        x = str.find(s[i])
        if x == 6:
            d[i][x] += 1

        else:
            d[i][x] += d[i][x+1]
        d[i][x] %= MOD
    print(d[0][0])

def main():
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)
    return

main()
