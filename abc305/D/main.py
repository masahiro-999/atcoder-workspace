import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect,bisect_left
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


def solve(N,A,Q,lr):

    def f(t):
        x = bisect_left(A,t)
        if x == 0:
            return 0
        if x % 2 == 0:
            # 睡眠中
            return b[x-1] + t - A[x-1]
        else:
            return b[x]
    
    b = [0] * N
    for i in range(1,N):
        if i % 2 == 1:
            b[i] = b[i-1]
        else:
            b[i] = b[i-1] +(A[i]-A[i-1])

    for [l,r] in lr:
        print(f(r)-f(l))

def main():
    N = int(next(tokens)) 
    A = li()
    Q = int(next(tokens)) 
    lr = [li() for _ in range(Q)]
    solve(N,A,Q,lr)
    return

main()
