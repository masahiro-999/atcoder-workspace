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
try:
    from pypyjit import set_param
    set_param('max_unroll_recursion=-1')
except ModuleNotFoundError:
    pass

dxdy1 = ((0, 1), (0, -1), (1, 0), (-1, 0))  # 上下左右
dxdy2 = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))  # 8方向すべて
dxdy3 = ((0, 1), (1, 0))  # 右 or 下
dxdy4 = ((1, 1), (1, -1), (-1, 1), (-1, -1))  # 斜め

inf = 1<<60

N = II()
S = [I() for _ in range(N)]

def move(p,dx,dy):
    x,y = p
    x += dx
    y += dy
    if not (0<= x <N and 0<=y<N) or S[x][y]=="#":
        return p
    else:
        return(x,y)

ans = inf
def bfs(p1,p2):
    global ans
    visited = [False]*(60**4)
    q = deque()
    if p1 > p2:
        p1,p2 = p2,p1
    visited[p1[0]*60**3+p1[1]*60**2+p2[0]*60+p2[1]] = True
    q.append((p1,p2,0))
    while q:
        p1,p2,d = q.popleft()
        for dx,dy in dxdy1:
            # next_p1 = move(p1,dx,dy)
            # next_p2 = move(p2,dx,dy)
            x,y = p1
            x += dx
            y += dy
            if not (0<= x <N and 0<=y<N) or S[x][y]=="#":
                next_p1 = p1
            else:
                next_p1 = (x,y)

            x,y = p2
            x += dx
            y += dy
            if not (0<= x <N and 0<=y<N) or S[x][y]=="#":
                next_p2 = p2
            else:
                next_p2 = (x,y)
            if next_p1 == next_p2:
                return d+1
            if next_p1 > next_p2:
                next_p1,next_p2 = next_p2,next_p1
            if visited[next_p1[0]*60**3+next_p1[1]*60**2+next_p2[0]*60+next_p2[1]]:
                continue
            visited[next_p1[0]*60**3+next_p1[1]*60**2+next_p2[0]*60+next_p2[1]] = True
            q.append((next_p1, next_p2, d+1))
    return -1

p=[]
for i in range(N):
    for j in range(N):
        if S[i][j] == "P":
            p.append((i,j))

# print(p)
ans = bfs(*p)
print(ans)