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

H,W = LII()
A = [I() for _ in range(H)]
Q = II()

def move(h1,a,H):
    if a >= h1:
        return a-h1
    else:
        return H-(h1-a)

def create_table(h1,h2,H):
    table_h = [0]*H
    j = h1
    dir = 1 if (h1+1)%H == h2 else -1 
    for i in range(H):
        table_h[i] = j
        j = (j+dir)%H
    return table_h

h1 = 0
h2 = 1
w1 = 0
w2 = 1
for _ in range(Q):
    a,b = LII()
    a -= 1
    b -= 1
    h1 = move(h1,a,H)
    h2 = move(h2,a,H)
    w1 = move(w1,b,W)
    w2 = move(w2,b,W)
    # print(h1,h2,w1,w2)

table_h = create_table(h1,h2,H)
table_w = create_table(w1,w2,W)

ans = [[""]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        ni = table_h[i]
        nj = table_w[j]
        ans[ni][nj] = A[i][j]
    

for i in range(H):
    print("".join(ans[i]))
