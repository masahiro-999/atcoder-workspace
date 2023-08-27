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


def solve(N: int, X: "List[int]", Y: "List[int]", Z: "List[int]"):

    t_g = 0
    xyz = []
    sum_z = 0
    for x,y,z in zip(X,Y,Z):
        sum_z += z
        if x > y:
            t_g += z
        else:
            xyz.append((-(-(x+y)//2) -x,z))

    target = -(-sum_z//2) - t_g
    if target <=0:
        ans = 0
    else:
        len_dp = len(xyz)
        dp = [[inf]*(target+1) for _ in range(len_dp+1)]
        dp[0][0] = 0
        
        for i in range(1,len_dp+1):
            for j in range(target+1):
                if dp[i-1][j] != inf:
                    dp[i][j] = min(dp[i][j],dp[i-1][j])
                    dp[i][min(target,j+xyz[i-1][1])] = min(dp[i][min(target,j+xyz[i-1][1])],dp[i-1][j] + xyz[i-1][0])
        ans = dp[len_dp][target]
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    Z = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        Z[i] = int(next(tokens))
    solve(N, X, Y, Z)
    return

main()
