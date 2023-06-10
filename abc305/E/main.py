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


def solve(N: int, M: int, K: int, a: "List[int]", b: "List[int]", p: "List[int]", h: "List[int]"):
    u = defaultdict(list)
    visited = defaultdict(lambda : -1)

    for a,b in zip(a,b):
        u[a].append(b)
        u[b].append(a)
    # 遠くまでいける点を優先して移動させていく。探索した頂点はsに保存
    s = set()
    phq = [(-h1,p1) for p1,h1 in zip(p,h)]
    heapify(phq)
    while phq:
        d,p1 = heappop(phq)
        d = -d
        s.add(p1)
        if d == 0:
            continue
        for nextp in u[p1]:
            if visited[nextp] < d-1:
                visited[nextp] = d-1
                heappush(phq, (-(d-1),nextp))

    s_list = list(s)
    s_list.sort()
    print(len(s_list))
    print(*s_list)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    p = [int()] * (K)  # type: "List[int]"
    h = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        p[i] = int(next(tokens))
        h[i] = int(next(tokens))
    solve(N, M, K, a, b, p, h)
    return

main()
