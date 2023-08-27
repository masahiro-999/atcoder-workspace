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
    def dfs(start,d):
        nonlocal disable
        nonlocal d_max,i_max
        disable.add(start)
        visited[start]=True
        for c,i in g[start]:
            if visited[i] == False:
                dfs(i,d+c)
        if d > d_max:
            d_max=d
            i_max=start
        visited[start]=False
            

    visited = [False]*(N+1)
    g = defaultdict(list)
    for a,b,c in zip(A,B,C):
        g[a].append((c,b))
        g[b].append((c,a))

    ans = 0
    i_max = -1
    disable = set()
    for i in range(1,N+1):
        d_max = -1
        dfs(i,0)
        ans = max(ans, d_max)
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
