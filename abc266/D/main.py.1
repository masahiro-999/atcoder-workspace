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


def solve(N: int, T: "List[int]", X: "List[int]", A: "List[int]"):
    M = 100000
    dp = [[-1]*5 for _ in range(M+1)]
    dp[0][0] = 0
    txa = defaultdict(lambda: -1)
    for t,x,a in zip(T,X,A):
        txa[t] = (x,a)
    for i in range(1,M+1):
        for j in range(5):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j-1 >=0: dp[i][j] = max(dp[i][j], dp[i-1][j-1])
            if j+1 < 5: dp[i][j] = max(dp[i][j], dp[i-1][j+1])
            if dp[i][j] != -1 and txa[i] != -1 and txa[i][0] == j:
                dp[i][j] = dp[i][j] + txa[i][1]
    ans = max(dp[M])
    print(ans)
                
def main():
    N = int(next(tokens))  # type: int
    T = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    A = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, T, X, A)
    return

main()
