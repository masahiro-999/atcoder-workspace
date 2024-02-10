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
A = TII()
S = I()

pos = defaultdict(list)

for i,s in enumerate(S):
    pos[s].append(i)

X_list = {}
cnt = [0]*3
for i in pos["X"][::-1]:
    cnt[A[i]]+=1
    X_list[i] = cnt[:]
X_keys = sorted(list(X_list.keys()))

M_list = {}
cnt = [0]*3
for i in pos["M"]:
    cnt[A[i]]+=1
    M_list[i] = cnt[:]
M_keys = sorted(list(M_list.keys()))

# print(X_list)
# print(M_list)
    
def mex(a,b,c):
    s = [a,b,c]
    if 0 not in s:
        return 0
    if 1 not in s:
        return 1
    if 2 not in s:
        return 2
    if 3 not in s:
        return 3
    return 4
# print(f'{X_keys=} {M_keys=}')
ans = 0
for i in pos["E"]:
    b = A[i]
    index_x = bisect_right(X_keys,i)
    if index_x == len(X_keys):
        continue
    c_list=X_list[X_keys[index_x]]

    index_m = bisect_left(M_keys,i)-1
    if index_m < 0:
        continue
    a_list=M_list[M_keys[index_m]]
    for a,na in enumerate(a_list):
        if na == 0:
            continue
        for c,nc in enumerate(c_list):
            if nc == 0:
                continue
            ans += mex(a,b,c)*na*nc
            # print(i,a,na,c,nc,mex(a,b,c)*na*nc)

print(ans)