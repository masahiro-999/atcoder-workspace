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

N,H,W = TII()
ab = [TII() for _ in range(N)]

oklist = []
for i in range(1<<N):
    sm = 0
    for j in range(N):
        if i>>j&1:
            sm += ab[j][0]*ab[j][1]
    if sm == H*W:
        oklist.append(i)

def can_put(t,i,j,a,b):
    # 座標i,jにa*bの長方形を置けるか
    for x in range(a):
        for y in range(b):
            if i+x >= H or j+y >= W:
                return False
            if t[i+x][j+y] != 0:
                return False
    return True

def check(p_list,s):
    # print(p_list,s)
    t = [[0]*W for _ in range(H)]
    n = 0
    def sub(q,n):
        if q == len(s):
            return True
        # print(q,s[p_list[q]],n)
        # if n >= H*W:
        #     return False
        p = p_list[q]
        a,b = ab[s[p]]
        # あいてるところを探す
        while True:
            i = n//W
            j = n%W
            n += 1
            if t[i][j] == 0:
                break
        for a,b in [(a,b),(b,a)]:
            if can_put(t,i,j,a,b):
                for x in range(a):
                    for y in range(b):
                        t[i+x][j+y] = 1
                ret = sub(q+1,n)
                if ret == True:
                    return True
                for x in range(a):
                    for y in range(b):
                        t[i+x][j+y] = 0
        return False
    return sub(0,0)

ans = NO
for i in oklist:
    s = []
    for j in range(N):
        if i>>j&1:
            s.append(j)
    # print(s)
    ans = NO
    for p_list in permutations(range(len(s))):
        if check(p_list,s):
            print(YES)
            exit()


print(NO)