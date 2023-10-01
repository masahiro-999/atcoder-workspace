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


def solve(N,K,P,A):
    # dp[p1,p2,..pk] コストの総和の最小値
    dp = defaultdict(lambda: inf)
    dp["0"*K] = 0
    for i in range(N):
        c,a = A[i]
        ndp = defaultdict(lambda: inf)
        for k,v in dp.items():
            # a,cを使わない
            ndp[k] = min(ndp[k], v)
            # a,cを使う
            ok = False
            for j in range(K):
                if int(k[j]) <P:
                    ok = True
                    break
            if ok:
                nk = [int(x) for x in k]
                for j in range(K):
                    nk[j] = min(P,nk[j]+a[j])
                nk = "".join([str(x) for x in nk])
                ndp[nk] = min(ndp[nk], v+c)
        dp = ndp    
    ans = inf
    for k,v in dp.items():
        ok = True
        for j in range(K):
            if int(k[j]) <P:
                ok = False
                break
        if ok:
            ans = min(ans,v)
    if ans == inf:
        print(-1)
    else:
        print(ans)
    return

def main():
    N = int(next(tokens))
    K = int(next(tokens))
    P = int(next(tokens))
    A = [0]*N
    for i in range(N):
        c = int(next(tokens))
        a = [int(next(tokens)) for _ in range(K)]
        A[i] = (c,a)
    solve(N,K,P,A)
    return

main()
