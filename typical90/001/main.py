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


def solve(N: int, L: int, K: int, A: "List[int]"):
    a = [A[0]] + [A[i+1] - A[i] for i in range(N-1)] + [L-A[-1]]

    def find_n(x):
        l = 0
        n = 0
        for i in range(len(a)):
            l += a[i]
            if l >=x :
                n += 1
                l = 0   
        if l >= x:
            n += 1
        return n
    
    lo = 1
    hi = L+1
    while (hi-lo>1):
        mid = (lo+hi)//2
        n = find_n(mid)
        if n >= K+1:
            lo = mid
        else:
            hi = mid
    print(lo)

def main():
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L, K, A)
    return

main()
