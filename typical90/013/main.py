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


def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):

    def bfs(s,t):
        q = [(0,s)]
        t[s] = 0
        heapify(q)
        visited = defaultdict(bool)
        while q:
            (d,p) = heappop(q)
            if visited[p] == True:
                continue
            visited[p] = True
            for next_p,c in u[p]:
                if t[next_p] > d + c:
                    # 新しいパスの方が近い
                    t[next_p] = d + c
                    heappush(q, (t[next_p], next_p))

    u = defaultdict(list)
    for a,b,c in zip(A,B,C):
        a -= 1
        b -= 1
        u[a].append((b,c))
        u[b].append((a,c))

    t1 = [inf]*N
    tn = [inf]*N

    bfs(0,t1)
    bfs(N-1,tn)

    for i in range(N):
        ans = t1[i] +tn[i]
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
