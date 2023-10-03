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

def find(N):
    n = 1
    ret = 0
    while True:
        x = N-(n*(n-1)//2)
        if x < 0:
            break
        if x == 0:
            pass
        elif x % n == 0:
            ret += 2
            # print(n)
        n+=1
    return ret

def solve(N: int):
    if N < 0:
        N = -N
    if N == 0:
        ans = 1
    elif N==1:
        ans = 2
    elif N==2:
        ans = 2
    else:
        ans = find(N)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    solve(N)
    return

main()
