from io import BytesIO, IOBase

import sys
import os

from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from itertools import product, accumulate,permutations,combinations, count
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *

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


N,A,B,C = TII()  # type: int
D = [LII() for _ in range(N)]

# 都市0から都市ｘまでの最小コストをＢＦＳで求める

inf = 10**18

# 密グラフのダイクストラ
# プライオリティキューを用いず最小のパスをすべて操作して求める場合
# https://qiita.com/convexineq/items/aca8dde73cc866aa362a
def dijkstra(s,t,D):
    done = [False]*N
    t[s] = 0
    for _ in range(N):
        # 未確定で最小のpを調べる
        (d,p) = min([(d,p) for p,d in enumerate(t) if done[p]==False])
        done[p] = True
        # pの次の値を更新する
        for i in range(N):
            if done[i]:
                continue
            t[i] = min(t[i],d + D[p][i])

# heapqueueを使う場合
# def dijkstra(s,t,D):
#     q = [(0,s)]
#     t[s] = 0
#     heapify(q)
#     while q:
#         (d,p) = heappop(q)
#         if t[p] < d:
#             continue
#         for next_p in range(N):
#             if next_p == p:
#                 continue
#             c = D[p][next_p]
#             if t[next_p] > d + c:
#                 # 新しいパスの方が近い
#                 t[next_p] = d + c
#                 heappush(q, (t[next_p], next_p))

t1 = [inf]*N
tn = [inf]*N

D1 = [[x*A for x in d] for d in D]
Dn = [[x*B+C for x in d] for d in D]

dijkstra(0,t1,D1)
dijkstra(N-1,tn,Dn)

ans = inf
for i in range(N):
    # print(i, t1[i]+tn[i])
    ans = min(ans,t1[i]+tn[i])

# print("--")
# print(t1)
# print("--")
# print(tn)
print(ans)