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


def solve(N: int, K: int, D: int, a: "List[int]"):
    d = [[[-1]*(D) for _ in range(K+1)] for _ in range(N)]
    d[0][1][a[0]%D] = a[0]
    for i in range(N-1):
        for j in range(K+1):
            for k in range(D):
                # 加えない場合
                d[i+1][j][k] = max(d[i+1][j][k], d[i][j][k])
                # 加える場合
                if j == 0:
                    # 初めて加える
                    d[i+1][j+1][(a[i+1])%D] = max(d[i+1][j+1][(a[i+1])%D],a[i+1])
                elif j < K and d[i][j][k] !=-1:
                    d[i+1][j+1][(k+a[i+1])%D] = max(d[i+1][j+1][(k+a[i+1])%D], d[i][j][k]+a[i+1])
    ans = -1
    for i in range(N):
        ans = max(ans, d[i][K][0])
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, D, a)
    return

main()
