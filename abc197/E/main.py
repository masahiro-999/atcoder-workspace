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
xc = [LII() for _ in range(N)]

min_max = {}
for x,c in xc:
    if c not in min_max:
        min_max[c] = (x,x)
    else:
        c0,c1 = min_max[c]
        min_max[c] = (min(x, c0), max(x, c1))

min_max[N+1] = (0,0)
c_list = sorted(min_max.keys())

n_c_list = len(c_list)
dp = [[0]*2 for _ in range(n_c_list+1)]
dp[0][0]=(0,0)
dp[0][1]=(0,0)

# print(min_max)
# print(c_list)

for i,c in enumerate(c_list):
    mi,mx = min_max[c]
    d = mx-mi
    dp[i+1][0] = (min(dp[i][0][0] +abs(mi - dp[i][0][1]), dp[i][1][0] + abs(mi - dp[i][1][1]))+d, mx)
    dp[i+1][1] = (min(dp[i][0][0] +abs(mx - dp[i][0][1]), dp[i][1][0] + abs(mx - dp[i][1][1]))+d, mi)

ans = min(dp[n_c_list][0][0],dp[n_c_list][1][0])
print(ans)