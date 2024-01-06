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
MOD = 998244353

N,M,K = TII()
A = LII()
uv = [TII() for _ in range(N-1)]

g = defaultdict(list)

A = [a-1 for a in A]

back = defaultdict(int)

for i,(u,v) in enumerate(uv):
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    if u > v:
        u,v = v,u
    back[(u,v)] = i

path_count = [0]*(N-1)

def count_up_path(a,b):
    if a == b:
        return
    # print(a,b)
    path = [-1]*N
    q = deque()
    q.append(a)
    while q:
        p = q.popleft()
        if p == b:
            break
        for next in g[p]:
            if path[next] == -1:
                path[next]=p
                q.append(next)
    s = b
    while True:
        t = path[s]
        x,y = s,t
        if x > y:
            x,y = y,x
        path_count[back[(x,y)]]+= 1
        # print("ab", x,y)
        s = t
        if s == a:
            break
    # print(path)
    # print(path_count)

for i in range(1,M):
    count_up_path(A[i-1],A[i])

total_path = sum(path_count)
if (total_path-K)%2 == 1:
    ans = 0
else:
    target = (total_path-K)//2
    n = len(path_count)
    dp = defaultdict(int)
    dp[0] = 1
    for i in range(n):
        next_dp = defaultdict(int)
        for j in dp.keys():
            if path_count[i]+j<=target:
                next_dp[path_count[i]+j] += dp[j]
                next_dp[path_count[i]+j] %= MOD
            next_dp[j] += dp[j]
            next_dp[j] %= MOD
        dp = next_dp
    ans = dp[target] % MOD
print(ans)
