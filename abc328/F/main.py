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

N,Q = LII()
abd = [LII() for _ in range(Q)]

class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [(-1,0)] * n

    def find(self, x):
        if self.parents[x][0] < 0:
            return (x,0)
        else:
            p,d1 = self.parents[x]
            p,d2 = self.find(p)
            self.parents[x] = (p,d1+d2)
            return self.parents[x]

    def union(self, x, y, d):
        x,dx = self.find(x)
        y,dy = self.find(y)

        if x == y:
            return True

        if self.parents[x][0] > self.parents[y][0]:
            x, y= y, x
            dx,dy = dy,dx
            d = -d
        # print(self.parents[x],self.parents[y])
        self.parents[x] = (self.parents[x][0]+self.parents[y][0],self.parents[x][1])
        self.parents[y] = (x,(dx-dy+d)) 
        return False

    def size(self, x):
        return -self.parents[self.find(x)][0]

    def same(self, x, y):
        return self.find(x)[0] == self.find(y)[0]

    def members(self, x):
        root = self.find(x)[0]
        return [i for i in range(self.n) if self.find(i)[0] == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x[0] < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)[0]].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

dsu = WeightedUnionFind(N)

ans = []
for i,(a,b,d) in enumerate(abd):
    a -= 1
    b -= 1
    if a==b and d !=0:
        continue
    if dsu.same(a,b):
        _,d1 = dsu.find(a)
        _,d2 = dsu.find(b)
        # print(i, a,b,d,d1,d2)
        if d2 != d1+d:
            continue
    else:
        dsu.union(a,b,d)
    # print(i,t)
    ans.append(i+1)

print(*ans)

# dsu = UnionFind(4)

# print(dsu.union(0,1,2))
# print(dsu.find(0))
# print(dsu.find(1))
# print(dsu.union(2,3,3))
# print(dsu.union(2,1,4))
# print(dsu.find(0))
# print(dsu.find(1))
# print(dsu.find(2))
# print(dsu.find(3))
