from io import BytesIO, IOBase

import sys
import os

from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10
from bisect import bisect, bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce, cache
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from itertools import product, accumulate,permutations,combinations, count, islice
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

N,M,K = LII()
ab = [LII() for _ in range(M)]

g_out = defaultdict(set)
in_count = Counter()

for a,b in ab:
    g_out[a].add(b)
    in_count[b] += 1

q = set()
for i in range(1,N+1):
    if in_count[i]==0:
        q.add(i)

ans = []
from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

@bootstrap
def p(q,p_list):
    if not q:
        if len(p_list)==N:
            ans.append(p_list[:])
            if len(ans)==K:
                for a in ans:
                    print(*a)
                exit()
        else:
            print(-1)
            exit()
    for i in list(islice(q,K)):
        q.remove(i)
        p_list.append(i)
        for next in g_out[i]:
            in_count[next] -= 1
            if in_count[next] == 0:
                q.add(next)
        yield p(q, p_list)
        for next in g_out[i]:
            if in_count[next] == 0:
                q.remove(next)
            in_count[next] += 1
        p_list.pop()
        q.add(i)
    yield

p(q,[])
print(-1)    


# ans = []
# def p(not_used,result):
#     print(not_used, result)
#     if not not_used:
#         ans.append(result[:])
#         if len(ans)==K:
#             for a in ans:
#                 print(*a)
#             exit()
#         return
#     for i in list(not_used):
#         not_used.remove(i)
#         result.append(i)
#         if i in atob:
#             b = atob[i]
#             depend[b] -= 1
#             if depend[b]==0:
#                 not_used.add(b)
#                 p(not_used,result)
#                 not_used.remove(b)
#             depend[b] += 1
#         else:
#             p(not_used,result)
#         result.pop()
#         not_used.add(i)

# not_used = set(range(1,N+1))
# for b in set_b:
#     not_used.remove(b)

# p(not_used,[])
# print(-1)