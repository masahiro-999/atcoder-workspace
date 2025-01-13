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

N,K = LII()
S = I()

numX = sum((1 for x in S if x == "X"))
numY = sum((1 for x in S if x == "Y"))

if numX < K:
    K = N - K
    S = "".join(["X" if s == "Y" else "Y" for s in S])
    numX,numY = numY,numX

if numY == 0:
    ans = max(0,K-1)
    print(ans)
    exit()

firstY = None
for i,s in enumerate(S):
    if s == "Y":
        lastY = i
        if firstY is None:
            firstY = i

ans = 0
lenX = []
cnt = 0
T = S[firstY:lastY+1]
lenT = len(T)
for i in range(lenT):
    if i != lenT-1:
        if T[i] == "Y" and T[i+1] == "Y":
            ans += 1
    if T[i] == "X":
        cnt += 1
    if (T[i] == "Y" or i == lenT-1) and cnt > 0:
        lenX.append(cnt)
    if T[i] == "Y":
        cnt = 0

ans += K   
lenX.sort()
# print(lenX,lenY,K)
k = K
for l in lenX:
    if k < l:
        break
    k -= l
    ans += 1

print(ans)
