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


def solve(N,Q,ab,cd):
    g = defaultdict(list)
    for a, b in ab:
        g[a].append(b)
        g[b].append(a)

    color = [-1] * (N+1)
    color[1] = 0
    def dfs(v):
        for nv in g[v]:
            if color[nv] != -1:
                continue
            color[nv] = 1 - color[v]
            dfs(nv)
        return    
    dfs(1)
    for c, d in cd:
        if color[c] == color[d]:
            print("Town")
        else:
            print("Road")


def main():
    N = int(next(tokens))
    Q = int(next(tokens))
    ab = [li() for _ in range(N-1)]
    cd = [li() for _ in range(Q)]
    solve(N,Q,ab,cd)
    return

main()
