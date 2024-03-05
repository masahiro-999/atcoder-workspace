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

def dprint(*x):
    print(*x, file=sys.stderr)

def p2d(x):
    for i,v in enumerate(x):
        dprint(i,":",*["*" if x==inf else x for x in v])

N,M = TII()
X = N+M+1
X2 = 1<<X
M2 = 1<<M
NN2 = 1<<(N+1)

dp =[[inf]*(X2) for _ in range(X)]

inv_speed = [0]*M2
for j in range(M2):
    inv_speed[j] = 1/(1<<len([1 for x in bin(j) if x == "1"]))

xy = [TII() for _ in range(N)]
pq = [TII() for _ in range(M)]
P = [(0,0)]+xy+pq

# 原点から移動した先を初期値にする。
for i in range(X):
    if i == 0:
        continue
    x1,y1 = P[i]
    dp[i][1<<i]=sqrt((x1)**2+(y1)**2)

for s in range(X2):
    for i in range(X):
        if s>>i &1 == 0:
            continue
        x1,y1 = P[i]
        for j in range(X):
            if s>>j&1 == 1:
                continue
            x2,y2 = P[j]
            d = sqrt((x1-x2)**2+(y1-y2)**2) 
            time = dp[i][s]+ d*inv_speed[s>>(N+1)]
            dp[j][s|1<<j] = min(dp[j][s|1<<j], time)
            # dprint(s,i,j,d,time,dp[i][s],dp[j][s|1<<j])

# p2d(dp)
ans = inf
for j in range(M2):
    ans = min(ans, dp[0][j<<(N+1)|(NN2-1)])
print(ans)