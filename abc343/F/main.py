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
A = LII()

from atcoder.segtree import SegTree

def f2(a,b):
    if a[0]==b[0]:
        if a[2]<b[2]:
            return((a[0],a[1]+b[1],b[2],b[3]))
        elif a[2]>b[2]:
            return((a[0],a[1]+b[1],a[2],a[3]))
        else:
            return((a[0],a[1]+b[1],a[2],a[3]+b[3]))
    else:
        if a[0]<b[0]:
            a,b = b,a
        if a[2]<b[0]:
            return((a[0],a[1],b[0],b[1]))
        elif a[2]>b[0]:
            return((a[0],a[1],a[2],a[3]))
        else:
            return((a[0],a[1],a[2],a[3]+b[1]))
    
# 遅い
def f(a,b):
    cnt = Counter()
    for x in [a,b]:
        cnt[x[0]] += x[1]
        cnt[x[2]] += x[3]

    k_list = sorted(cnt.keys(), reverse=True)
    if len(k_list)== 0:
        return ((0,0,0,0))
    if len(k_list)== 1:
        return (k_list[0], cnt[k_list[0]], 0,0)
    return (k_list[0], cnt[k_list[0]], k_list[1], cnt[k_list[1]])

# print(f((2,2,1,1),(4,4,3,3)))
st = SegTree(f2, (0,0,0,0), N)
for i,a in enumerate(A):
    st.set(i,(a,1,0,0))

for _ in range(Q):
    cmd, x1, x2 =LII()
    if cmd == 1:
        st.set(x1-1,((x2,1,0,0)))
    else:
        x = st.prod(x1-1,x2)
        print(x[3])