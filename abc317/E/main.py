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


def solve(H,W,a):

    def bfs(s):
        sy,sx = s
        q = deque()
        q.append(s)
        d = [[-1]*W for _ in range(H)]
        d[sy][sx] = 0
        while q:
            y,x = q.popleft()
            for (dx,dy) in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0<=x+dx < W and 0<=y+dy<H and a[y+dy][x+dx] == "." and d[y+dy][x+dx] == -1:
                    d[y+dy][x+dx] = d[y][x]+1
                    q.append((y+dy,x+dx))
        return d

    s = -1
    g = -1
    for i in range(H):
        for j in range(W):
            if a[i][j] == "S":
                s = (i,j)
            elif a[i][j] == "G":
                a[i][j] = "."
                g = (i,j)
            elif a[i][j] == ">":
                j += 1
                while j <W and a[i][j] in [".","|"] :
                    a[i][j] ="-"
                    j += 1
            elif a[i][j] == "<":
                j -= 1
                while j >= 0 and a[i][j] in [".","|"] :
                    a[i][j] ="-"
                    j -= 1
            elif a[i][j] == "v":
                ii = i+1
                while ii <H and a[ii][j] in [".","-"] :
                    a[ii][j] ="|"
                    ii += 1
            elif a[i][j] == "^":
                ii = i-1
                while ii >= 0 and a[ii][j] in [".","-"] :
                    a[ii][j] ="|"
                    ii -= 1
    d = bfs(s)
    ans = d[g[0]][g[1]]
    print(ans)


def main():
    H = int(next(tokens)) 
    W = int(next(tokens)) 
    a =[[s for s in input()]  for _ in range(H)]
    solve(H,W,a)
    return

main()
