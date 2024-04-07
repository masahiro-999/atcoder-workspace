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
YES = "Yes"
NO = "No"

H,W = LII()
A = [I() for _ in range(H)]

N = II()
RCE =[LII() for _ in range(N)]
RCE =[(r-1,c-1,e) for r,c,e in RCE]

def bfs(r,c,e):
    q = deque()
    q.append((r,c))
    dist = [[-1]*W for _ in range(H)]
    dist[r][c]=e
    while q:
        p = q.popleft()
        i,j = p
        d = dist[i][j]
        if d == 0:
            continue
        for di,dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_i =i+di
            next_j =j+dj
            if 0<=next_i<H and 0<=next_j<W and A[next_i][next_j]!="#" and dist[next_i][next_j]==-1:
                dist[next_i][next_j]= d-1
                q.append((next_i, next_j))
    return dist


for i in range(H):
    for j in range(W):
        if A[i][j]=="S":
            pos_s=(i,j)
        if A[i][j]=="T":
            pos_t=(i,j)

t_rc_i = {}
for i,(r,c,e) in enumerate(RCE):
    t_rc_i[(r,c)] = i

if pos_s not in t_rc_i.keys():
    print(NO)
    exit()

if pos_t not in t_rc_i.keys():
    t_rc_i[pos_t]=N
    N+=1

index_s = t_rc_i[pos_s]
index_t = t_rc_i[pos_t]

from atcoder.dsu import DSU
dsu =DSU(N)

g = defaultdict(list)
for i,(r,c,e) in enumerate(RCE):
    dist = bfs(r,c,e)
    # print(r,c,e)
    # print(dist)
    for (r,c),j in t_rc_i.items():
        if i == j:
            continue
        if dist[r][c] != -1:
            g[i].append(j)

visited = [False]*N
def dfs(s):
    if s == index_t:
        return True
    visited[s] = True
    for next in g[s]:
        if visited[next]:
            continue
        ret = dfs(next)
        if ret :
            return True
    return False

if dfs(index_s):
    print(YES)
else:
    print(NO)

