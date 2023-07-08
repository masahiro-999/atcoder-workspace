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


def solve(N1, N2, M: int, a: "List[int]", b: "List[int]"):
    N = N1+N2
    def bfs(g, start):
        dist = [-1]*(N+1)
        que = deque([start])
        dist[start] = 0
        while que:
            i = que.popleft()
            d = dist[i]
            for j in g[i]:
                if dist[j]==-1:
                    dist[j] = d+1
                    que.append(j)
        return dist
    
    g = defaultdict(list)

    for i,j in zip(a,b):
        i -= 1
        j -= 1
        g[i].append(j) 
        g[j].append(i) 

    dist1 = bfs(g, 0)
    dist2 = bfs(g,N-1)
    max1 = max(dist1)
    max2 = max(dist2)
    ans = max1+max2+1
    print(ans)
    
def main():
    N1 = int(next(tokens))
    N2 = int(next(tokens))       
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N1, N2, M, a, b)
    return

main()
