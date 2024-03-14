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
ab = [LII() for _ in range(N-1)]
Q =II()
kv = [LII() for _ in range(Q)]

g = defaultdict(list)
for a,b in ab:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dist = [-1]* N
order = []
K = len(bin(100000))-2+1
par = [[0]*N for _ in range(K)]

def dfs(s,d):
    dist[s] = d
    order.append(s)
    for next in g[s]:
        if dist[next] == -1:
            par[0][next] = s
            dfs(next,d+1)
dfs(0,0)
# print(g)
# print(dist)
for k in range(1,K):
    for i in range(N):
        par[k][i] = par[k-1][par[k-1][i]]
# print(par)

order_rev = [0]*N
for i in range(N):
    order_rev[order[i]]=i

def get_up_n(s,n):
    bin_n = bin(n)[2:]
    n2 = len(bin_n)-1
    for i in range(n2,-1,-1):
        if bin_n[-(i+1)]=="1":
            s = par[i][s]
    return s

def dist_two_point(v0,u0):
    v1,u1 = v0,u0
    if dist[v1] < dist[u1]:
        v1,u1 = u1,v1
    d = dist[v1]-dist[u1]
    n = dist[u1]
    v1 = get_up_n(v1,d)
    if v1 != u1:
        for i in range(K-1,-1,-1):
            v2 = par[i][v1]
            u2 = par[i][u1]
            if v2 !=u2:
                v1,u1=v2,u2
                n -= 1<<i
        d = dist[v0]+dist[u0] - (n-1)*2     
    return d

for x in kv:        
    k = x[0]
    v = [xx -1 for xx in x[1:]]
    v.sort(key=lambda x: order_rev[x])
    VN = len(v)
    d = 0
    for i in range(VN):
        d += dist_two_point(v[i],v[(i+1)%VN])
    d //=2
    print(d)