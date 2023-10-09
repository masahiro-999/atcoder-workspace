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

YES = "Yes"
NO = "No"

pol = []
for i in range(3):
    pol.append([I() for _ in range(4)])

num_p = 0
for p in pol:
    for line in p:
        count = Counter(line)
        num_p+=count["#"]

# @lru_cache()
def check_valid_didj(p,di,dj):
    for i,j in product(range(4), repeat=2):
        if p[i][j]=="#":
            if not (0<=i+di<4 and 0<=j+dj<4):
                return False
    return True

# @lru_cache()
def rot(i,j,dir):
    for _ in range(dir):
        i,j = j,3-i
    return i,j

def move_and_put(src,dest,di,dj,dir):
    dest = deepcopy(dest)
    for i0,j0 in product(range(4), repeat=2):
        if src[i0][j0] == "#":
            i,j = rot(i0+di, j0+dj,dir)
            if dest[i][j] !=0:
                return None
            dest[i][j] = 1
    return dest


def put_pol_n(p0,n):
    for di,dj,dir in product(range(-3,4), range(-3,4), range(4)):
        if not check_valid_didj(pol[n],di,dj):
            continue
        p1 =  move_and_put(pol[n],p0,di,dj,dir)
        if p1 is not None:
            if n == 2:
                return True
            if put_pol_n(p1, n+1):
                return True
    return False

if num_p != 16:
    ans = False
else:
    p0 = [[0]*4 for _ in range(4)]
    ans = put_pol_n(p0, 0)

print(YES if ans else NO)