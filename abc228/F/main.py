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

H,W,h1,w1,h2,w2 = TII()

h2=min(h2,h1)
w2=min(w2,w1)

A = [TII() for _ in range(H)]

def get_sum(A,i,j,h,w):
    return A[i+h][j+w]-A[i][j+w]-(A[i+h][j]-A[i][j])

def create_2d_acc(A):
    A1 =[list(accumulate(a, initial=0)) for a in A]
    A2 = list(zip(*A1))
    A3 =[list(accumulate(a, initial=0)) for a in A2]
    A4 = list(zip(*A3))
    return A4

def create_score(accA,h,w):
    score = [[0]*(W-w+1) for _ in range(H-h+1)]
    for i,j in product(range(H-h+1), range(W-w+1)):
        score[i][j]=get_sum(accA,i,j,h,w)
    return score

def slide_max(A,k):
    q = deque()
    ret = []
    for i,a in enumerate(A,start=1):
        # remove old one
        if q and q[0][1]+k<=i:
            q.popleft()
        # aより小さいものは除く
        while q and q[-1][0] <a:
            q.pop()
        q.append((a,i))
        if i<k:
            continue
        ret.append(q[0][0])
    return ret

# a = [1,2,3,2,4,1,2,6,3,1,1,1]
# print(a)
# print(slide_max(a,3))

accA = create_2d_acc(A)

black_score = create_score(accA,h1,w1)
white_score = create_score(accA,h2,w2)

tmp = [slide_max(x,w1-w2+1) for x in white_score]
tmp2 = list(zip(*tmp))
tmp3 = [slide_max(x,h1-h2+1) for x in tmp2]
white_slide_max = list(zip(*tmp3))

# print("---")
# print(white_score)
# print("---")
# print(tmp)
# print("---")
# print(tmp3)

ans = 0
for i,j in product(range(H-h1+1), range(W-w1+1)):
    a1 = black_score[i][j] - white_slide_max[i][j]
    ans = max(ans,a1)
print(ans)