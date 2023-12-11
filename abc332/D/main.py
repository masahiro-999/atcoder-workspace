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

inf = 1<<60

H,W = TII()
A = [LII() for _ in range(H)]
B = [LII() for _ in range(H)]

def count_swap(p):
    L = len(p)
    ret = 0
    for i in range(L-1):
        for j in range(i+1,L):
            if p[i]>p[j]:
                ret += 1
    return ret

ans = inf
for ph, pw in product(
    permutations(range(H),H),
    permutations(range(W),W)
):
    for i,j in product(range(H),range(W)):
        if A[ph[i]][pw[j]] != B[i][j]:
            break
    else:
        # print(ph,pw)
        ans = min(ans, count_swap(ph)+count_swap(pw))

if ans == inf:
    ans = -1
print(ans)

# 01 02 03 04 05
# 06 07 08 09 10
# 11 12 13 14 15
# 16 17 18 19 20

# 01 03 02 05 04
# 11 13 12 15 14
# 06 08 07 10 09
# 16 18 17 20 19

# 710511029 136397527 763027379 644706927 447672230
# 979861204 57882493 442931589 951053644 152300688
# 43971370 126515475 962139996 541282303 834022578
# 312523039 506696497 664922712 414720753 304621362
# 325269832 191410838 286751784 732741849 806602693

# 806602693 732741849 286751784 191410838 325269832
# 304621362 414720753 664922712 506696497 312523039
# 834022578 541282303 962139996 126515475 43971370
# 152300688 951053644 442931589 57882493 979861204
# 447672230 644706927 763027379 136397527 710511029