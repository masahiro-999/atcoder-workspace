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

table0 ={"R":1, "G":2, "B": 3}
table_list =[{"R":1, "G":3, "B": 2},{"R":3, "G":2, "B": 1},{"R":2, "G":1, "B": 3}]
N = II()
S_in = I()
T_in = I()

b = 1000000007
p = 998244353
# b = 10

# h(n) = X[0]*b**(n-1) + X[1]*b**(n-2)+ ... +X[n-1]*b**(0) 
def create_hash(X):
    hash = [0]*(len(X)+1)
    hash[0] = 0
    for i in range(len(X)):
        hash[i+1] = (hash[i]*b+X[i])%p
    return hash

pow_b = []
x = 1
for i in range(N+1):
    pow_b.append(x)
    x*=b
    x%=p

@cache
def pow_cache(x,y,z):
    return pow(x,y,z)

def hash(h,s,t):
    # いずれの方法もTLEになった。定数倍で引っかかった
    # return (h[t+1]-h[s]*pow(b,t+1-s,p))%p 
    # return (h[t+1]-h[s]*pow_cache(b,t+1-s,p))%p 
    return (h[t+1]-h[s]*pow_b[t+1-s])%p 

ans = 0

for table in table_list:
    S = [table0[x] for x in S_in]
    T = [table[x] for x in T_in]

    hash_s = create_hash(S)
    hash_t = create_hash(T)

    if hash(hash_s,0,N-1) == hash(hash_t,0,N-1):
        ans += 1
    for k in range(1,N):
        if hash(hash_s,k,N-1) == hash(hash_t,0,N-k-1):
            ans += 1
        if hash(hash_t,k,N-1) == hash(hash_s,0,N-k-1):
            ans += 1

    # if S == T:
    #     ans += 1
    # for k in range(1,N):
    #     if S[k:N] == T[0:N-k]:
    #         ans += 1
    #     if T[k:N] == S[0:N-k]:
    #         ans += 1

print(ans)

# h = create_hash([1,2,3])
# h2 = create_hash([2,1,1,2,3])
# print(h)
# print(h2)
# print(hash(h,0,2))
# print(hash(h2,2,4))