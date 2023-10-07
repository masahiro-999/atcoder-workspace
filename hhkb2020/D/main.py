import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate,permutations,combinations
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

def solve2(T,t):
    def p(n,x):
        # 幅nの中に幅xを置く場合の数
        return n-x+1 % MOD
    def sum_n(a,n):
        # 初項a,項数n,項差1の和
        return (2*a+(n-1))*n//2 % MOD

    for N,A,B in t:
        if A+B >N:
            ans = 0
        else:
            ans1 = p(N,A)*p(N,B)*sum_n(1,N-A-B+1)*4
            ans2 = sum_n(1,N-A-B+1)**2*4
            ans = (ans1 - ans2) % MOD
        print(ans)

def solve(T,t):
    def p(n,x):
        # 幅nの中に幅xを置く場合の数
        return n-x+1
    def sum_n(a,n):
        return (2*a-(n-1))*n//2

    for N,A,B in t:
        if N < A+B:
            ans = 0
        else:
            if A<B:
                A,B = B,A
            ans = pow(p(N,A),2,MOD) * pow(p(N,B),2,MOD)
            ans %= MOD
            ans -= pow(sum_n(p(N,A+1),B-1)*2,2,MOD)
            ans -= sum_n(p(N,A+1),B-1)*2*p(N,A)*p(A,B)*2
            ans %= MOD
            ans -= pow(p(N,A),2,MOD)*pow(p(A,B),2,MOD)
            ans %= MOD
        print(ans)

def main():
    T = int(next(tokens))
    t = [li() for _ in range(T)]
    solve(T,t)
    return

main()
