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

N = II()
P = LII()

t = [0]*(N+1)

for i,v in enumerate(P):
    t[v] = i

def move(i,j):
    global P
    q = P[:i]+P[i+2:]
    P = q[:j]+P[i:i+2]+q[j:]

l = []
t = N-1
for i in range(N-2):
    n = P.index(i+1)
    if n==i:
        continue
    if n > N-2:
        move(N-2,N-3)
        l.append((N-2,N-3))
        n = P.index(i+1)
    move(n,i)
    l.append((n,i))

ans = True
for i in range(N):
    if P[i]!=i+1:
        ans = False
        break

if ans:
    print("Yes")
    print(len(l))
    for i,j in l:
        print(i+1,j)
else:
    print("No")