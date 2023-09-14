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


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    d = [[-1]*N for _ in range(N)]
    for i in range(N):
        d[i][i] = 0
    for a, b, c in zip(A, B, C):
        d[a-1][b-1] = c

    ans = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][k] != -1 and d[k][j] != -1:
                    if d[i][j] == -1:
                        d[i][j] = d[i][k] + d[k][j]
                    else:
                        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                if d[i][j] != -1:
                    ans += d[i][j]
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)
    return

main()
