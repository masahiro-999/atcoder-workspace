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

# floor_sqrt(n) = floor(sqrt(n))
def floor_sqrt(n):
    # Binary Search
    left = 0
    right = n
    while left < right:
        center = (left + right + 1) // 2
        if center * center <= n:
            left = center
        else:
            right = center - 1
    return left

def solve(N: int, M: int):
    mx = int(sqrt(M))
    can_move = set()
    for i in range(0,mx+1):
        j = floor_sqrt(M - i*i)
        if i*i+j*j == M:
            can_move.add((i,j))
            can_move.add((i,-j))
            can_move.add((-i,j))
            can_move.add((-i,-j))

    d =[[-1]*N for _ in range(N)]
    d[0][0] = 0
    q = deque()
    q.append((0,0))
    while q:
        pos = q.popleft()
        for dxdy in can_move:
                pos_next = pos[0]+dxdy[0],pos[1]+dxdy[1] 
                if 0<=pos_next[0]<N and 0<=pos_next[1]<N and d[pos_next[0]][pos_next[1]] == -1:
                     q.append(pos_next)
                     d[pos_next[0]][pos_next[1]] = d[pos[0]][pos[1]]+1

    for i in d:
        print(*i)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)
    return

main()
