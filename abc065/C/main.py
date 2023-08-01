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

MOD = 1000000007

def solve(N: int, M: int):
    def factorial(n):
        ret = 1
        for i in  range(1,n+1):
            ret *= i
            ret %= MOD
        return ret

    if N < M:
        N,M = M,N

    if (N-M)>1:
        return(0)
    if (N-M)==1:
        return factorial(N)*factorial(M) %MOD
    if (N-M)==0:
        return factorial(N)**2*2%MOD

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    print(solve(N, M))
    return

main()
