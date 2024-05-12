from io import BytesIO, IOBase

import sys
import os

from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce, cache
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from itertools import product, accumulate,permutations,combinations, count
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *
from sortedcontainers import SortedSet, SortedList, SortedDict

BUFSIZE = 4096

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

sys.stdin = IOWrapper(sys.stdin)
sys.stdout = IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

if True:
    def I():
        return input()

    def II():
        return int(input())

    def MII():
        return map(int, input().split())

    def LI():
        return list(input().split())

    def LII():
        return list(map(int, input().split()))

    def TII():
        return tuple(map(int, input().split()))

    def GMI():
        return map(lambda x: int(x) - 1, input().split())

    def LGMI():
        return list(map(lambda x: int(x) - 1, input().split()))

sys.setrecursionlimit(5 * 10 ** 5)
# try:
#     from pypyjit import set_param
#     set_param('max_unroll_recursion=-1')
# except ModuleNotFoundError:
#     pass

dxdy1 = ((0, 1), (0, -1), (1, 0), (-1, 0))  # 上下左右
dxdy2 = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))  # 8方向すべて
dxdy3 = ((0, 1), (1, 0))  # 右 or 下
dxdy4 = ((1, 1), (1, -1), (-1, 1), (-1, -1))  # 斜め

inf = 1<<60

N = II()
C = [I() for _ in range(N)]


def create_g(c):
    g = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if (j+1<N):
                cost = 1 if C[i][j+1]!=c else 0
                g[i*N+j].append((i*N+j+1,cost))
                cost = 1 if C[i][j]!=c else 0
                g[i*N+j+1].append((i*N+j,cost))
            if (i+1<N):
                cost = 1 if C[i+1][j]!=c else 0
                g[i*N+j].append((i*N+j+N,cost))
                cost = 1 if C[i][j]!=c else 0
                g[i*N+j+N].append((i*N+j,cost))

    return g

def bfs(g,pos_start, pos_end):
    q = deque()
    q.append(pos_start)
    dist = [0]*(N*N)
    dist[pos_start] = 0
    visited = [-1]*(N*N)
    visited[pos_start]=0
    while q:
        p = q.popleft()
        for np,c in g[p]:
            if visited[np] != -1:
                continue
            visited[np] = p
            dist[np] = dist[p]+c
            if np == pos_end:
                return dist[np]
            if c == 0:
                q.appendleft(np)
            else:
                q.append(np)
    print(visited)
    assert False

def count(g,visited,pos_start, pos_end,c):
    p = pos_end
    i,j = p//N,p%N
    cnt = 0
    if C[i][j] != c:
        cnt += 1
    while True:
        p = visited[p]
        i,j = p//N,p%N
        if C[i][j] != c:
            cnt += 1
        if p == pos_start:
            break
    return cnt

ans = 0
g = create_g("R")
s = 0
t = N*N-1
ans += bfs(g,s,t)

g = create_g("B")
s = N-1
t = (N-1)*N
ans += bfs(g,s,t)

print(ans)