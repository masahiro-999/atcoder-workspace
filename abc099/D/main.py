import sys
import os
from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10, isqrt
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce, cache
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import product, accumulate,permutations,combinations, count
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = 100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

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

N,C = LII()
D = [LII() for _ in range(C)]
c = [LII() for _ in range(N)]

# t = [[0]*31 for _ in range(31)]
# for i in range(3,30+1):
#     for j in range(3,30+1):
#         for k in range(3,30+1):
#             t[i][j] = min(t[i][j],D[i][k]+D[j][k])

L = [[] for _ in range(3)]
for i in range(N):
    for j in range(N):
        k = (i+1+j+1)%3
        L[k].append(c[i][j])

A = [[0]*3 for _ in range(C)]
for i in range(3):
    for j in range(C):
        x = 0
        for c in L[i]:
            x+=D[c-1][j]
        A[j][i] = x

@bootstrap
def find(t,L,except_list,sm):
    if t == 3:
        yield sm
    mi = inf
    for i in range(C):
        if i in except_list:
            continue
        x = A[i][t]
        x = yield find(t+1,L, except_list+[i], sm+x)
        mi = min(mi,x)
    yield mi

ans = find(0,L,[],0)
print(ans)
