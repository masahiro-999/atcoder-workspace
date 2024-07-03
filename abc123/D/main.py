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

X,Y,Z,K = LII()
A = LII()
B = LII()
C = LII()

mx =[X,Y,Z]

q = []
heapify(q)

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

a=0
b=0
c=0
x = A[a]+B[b]+C[c]
visited = set()
heappush(q,(-x,a,b,c))
ans = []
while q:
    x,*a = heappop(q)
    ans.append(-x)
    if len(ans)==K:
        break
    for i in range(3):
        b = a[:]
        b[i]+=1
        if b[i] == mx[i]:
            continue
        if (b[0],b[1],b[2]) in visited:
            continue
        visited.add((b[0],b[1],b[2]))
        x = A[b[0]]+B[b[1]]+C[b[2]]
        heappush(q,(-x,*b))

print(*ans, sep="\n")