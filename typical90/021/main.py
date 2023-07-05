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

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    def get_dfs_path(g, path, i):
        path.add(i)
        visited[i] = 1
        for n in g[i]:
            if n not in path and visited[n] == 0:
                get_dfs_path(g, path, n)

    def dfs(s):
        visited[s] = 1
        for n in g[s]:
            if visited[n] == 0:
                dfs(n)
        order.append(s)

    g = defaultdict(list)
    g_rev = defaultdict(list)
    for a,b in zip(A,B):
        a -= 1
        b -= 1
        g[a].append(b)
        g_rev[b].append(a)

    visited = [0] * N
    order = []
    for i in range(N):
        if visited[i] == 0:
            dfs(i)

    visited = [0] * N
    ans = 0
    for i in reversed(order):
        if visited[i] != 0:
            continue
        path = set()
        get_dfs_path(g_rev, path, i)
        l = len(path)
        ans += l*(l-1)//2

    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)
    return

main()
