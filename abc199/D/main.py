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


def create_visit_order_list(visited,N,g,s):
    def dfs(s):
        order.append(s)
        visited[s] = True
        for v in g[s]:
            if not visited[v]:
                dfs(v)
    order = []
    dfs(s)
    return order

def solve(N,M,ab):

    def can_paint(s, c):
        for v in g[s]:
            if colors[v] == c:
                return False
        return True
    def dfs(i=0):
        if i == len(visit_order_list):
            return 1
        s = visit_order_list[i]
        n = 0
        for c in range(1,4):
            if can_paint(s, c):
                colors[s] = c
                n += dfs(i+1)
                colors[s] = 0
        return n 

    g = defaultdict(list)
    for a,b in ab:
        g[a].append(b)
        g[b].append(a)

    colors = [0]*(N+1)
    ans = 1
    visited = [False]*(N+1)
    for i in range(1,N+1):
        if visited[i]:
            continue
        visit_order_list = create_visit_order_list(visited,N,g,i)
        ans *= dfs()

    print(ans)

def main():
    N = int(next(tokens))
    M = int(next(tokens))
    ab = [li() for _ in range(M)]
    solve(N,M,ab)
    return

main()
