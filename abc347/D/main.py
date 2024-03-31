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

a,b,C = LII()

def solv(a,b,C):

    z2 = a+b - C.bit_count()
    if z2 < 0 or z2%2 == 1:
        return -1

    n_both_one = z2//2
    n_one_x = a - n_both_one
    n_one_y = b - n_both_one

    if n_one_x < 0 or n_one_y < 0:
        return -1
    if n_one_x + n_one_y + n_both_one >60:
        return -1
    X = 0
    Y = 0
    for i in range(60):
        if C>>i&1:
            if n_one_x > 0:
                X |= 1<<i
                n_one_x -= 1
            elif n_one_y > 0:
                Y |= 1<<i
                n_one_y -= 1
        else:
            if n_both_one > 0:
                X |= 1<<i
                Y |= 1<<i
                n_both_one -= 1
    return (X,Y)

ans = solv(a,b,C)
if  ans == -1:
    print(-1)
else:
    print(*ans)

# for X in range(1<<8):
#     for Y in range(1<<8):
#         C = X^Y
#         a = bin(X).count("1")
#         b = bin(Y).count("1")
#         ans = solv(a,b,C)
#         if ans == -1:
#             print("WA")
#             print(a,b,bin(C))
#             exit()
#         else:
#             X,Y = ans
#             if X^Y != C or a != bin(X).count("1") or b != bin(Y).count("1"):
#                 print("WA")
#                 print(a,b,bin(C))
#                 print(bin(X),bin(Y),bin(C))
#                 exit()

# for a in range(5):
#     for b in range(5):
#         for C in range(1<<11):
#             ans = solv(a,b,C)
#             if ans == -2:
#                 print("WA")
#                 print(a,b,bin(C))
#                 exit()
#             if ans == -1:
#                 # print(a,b,bin(C))
#                 continue
#             else:
#                 X,Y = ans
#                 if X^Y != C or a != bin(X).count("1") or b != bin(Y).count("1"):
#                     print("WA")
#                     print(a,b,C)
#                     print(bin(X),bin(Y),bin(C))
#                     exit()
