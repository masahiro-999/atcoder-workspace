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


def solve(H,W,c):
    # 高橋君がマス (1,1) から歩き始めるとき、彼が立ち止まるまでに通ることのできるマスは最大で何マスですか？
    def bfs(sx,sy):
        d = [[-1]*W for _ in range(H)]
        d[sx][sy] = 1
        q = deque([(sx,sy)])
        while q:
            pos = q.popleft()
            x,y = pos
            for dx,dy in [(1,0),(0,1),]:
                nx,ny = x+dx,y+dy
                if 0<=nx<H and 0<=ny<W and d[nx][ny]==-1 and c[nx][ny]=='.':
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))
        return d
    d = bfs(0,0)
    ans = 0
    for i in range(H):
        for j in range(W):
            if d[i][j] != -1:
                ans = max(ans,d[i][j])
    print(ans)

def main():
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    c = [input() for _ in range(H)]  # type: "List[str]"
    solve(H, W, c)
    return

main()
