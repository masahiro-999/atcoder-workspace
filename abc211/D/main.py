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

MOD = 1000000007

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    g = defaultdict(list)
    for a, b in zip(A, B):
        g[a].append(b)
        g[b].append(a)
    
    def bfs(s):
        dist = [-1] * (N+1)
        num_path = [0] * (N+1)
        dist[s] = 0
        num_path[s] = 1
        q = deque([s])
        while q:
            v = q.popleft()
            for nv in g[v]:
                if dist[nv] != -1:
                    if dist[nv] == dist[v] + 1:
                        num_path[nv] += num_path[v]
                        num_path[nv] %= MOD
                    continue
                dist[nv] = dist[v] + 1
                num_path[nv] = num_path[v]
                q.append(nv)
        return num_path

    num_path = bfs(1)
    print(num_path[N])

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
