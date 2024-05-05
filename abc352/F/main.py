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

N,M = LII()
abc = [TII() for _ in range(M)]

from atcoder.dsu import DSU
dsu = DSU(N)

def create_pos_list(start):
    def dfs(i):
        for to, c in g[i]:
            if to not in pos_dict:
                pos_dict[to] = pos_dict[i] - c
                dfs(to)
    pos_dict = {}
    pos_dict[start]=0
    dfs(start)
    bits = 0
    pos_list = []
    offset = min(pos_dict.values())
    for k,v in sorted(pos_dict.items(), key=lambda x:x[1]):
        bits |= 1<<(v-offset)
        pos_list.append(k)
    return bits, pos_list

g = defaultdict(list)
n = N
for a,b,c in abc:
    a -= 1
    b -= 1
    if not dsu.same(a,b):
        dsu.merge(a,b)
        n -= 1
    g[a].append((b,c))
    g[b].append((a,-c))

diff = [[] for _ in range(n)]

pos_list = []
cnt_one = 0
special_person = -1
for x in dsu.groups():
    if len(x) == 1:
        cnt_one += 1
        special_person = x[0]
        continue
    pos_list.append(create_pos_list(x[0]))

# print(pos_list)

n = len(pos_list)
order_list = []
def permutation(used, order, i):
    if i == n:
        order_list.append(order[:])
        return
    bits, hito_list = pos_list[i]
    for j in range(N):
        # print(i,j,bin(used))
        if used & bits<<j or bits<<j >= 1<<N:
            continue
        cnt = 0
        for k in range(bits.bit_length()):
            assert bits.bit_count() == len(hito_list)
            if bits>>k & 1:
                assert cnt < bits.bit_count()
                order[j+k] = hito_list[cnt]
                cnt += 1
        permutation(used | bits<<j, order, i+1)
        for k in range(bits.bit_length()):
            if bits>>k & 1:
                order[j+k] = -1

permutation(0, [-1]*N, 0)

# print(order_list)

order_person = [-1]*N
for i in range(N):
    order_person[i] = order_list[0][i]
    for order in order_list:
        if order_person[i] != order[i]:
            order_person[i] = -2
            break

# print(order_person)

cnt = Counter(order_person)
if cnt[-1] ==1 and cnt_one == 1:
    order_person[order_person.index(-1)] = special_person

ans = [-1]*N
for i in range(N):
    try:
        ans[i] = order_person.index(i)
        if ans[i] >=0:
            ans[i] += 1
    except:
        pass

print(*ans)
