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


def solve(N: int, M: int):
    def add(p1,p2):
         return (p1[0]+p2[0], p1[1]+p2[1])
    def is_ok(p):
        return 0<= p[0]<N and 0<=p[1]<N

    mx = int(sqrt(M))
    can_move = set()
    for i in range(0,mx+1):
        for j in range(i,mx+1):
            if i*i+j*j == M:
                can_move.add((i,j))
                can_move.add((i,-j))
                can_move.add((-i,j))
                can_move.add((-i,-j))
                can_move.add((j,i))
                can_move.add((j,-i))
                can_move.add((-j,i))
                can_move.add((-j,-i))

    d = defaultdict(lambda : -1)
    d[(0,0)] = 0
    q = deque()
    q.append((0,0))
    while q:
        pos = q.popleft()
        for dxdy in can_move:
                pos_next = add(pos, dxdy)
                if is_ok(pos_next) and d[pos_next] == -1:
                     q.append(pos_next)
                     d[pos_next] = d[pos]+1

    for i in range(N):
        print(" ".join([str(d[(i,j)]) for j in range(N)]))

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)
    return

main()
