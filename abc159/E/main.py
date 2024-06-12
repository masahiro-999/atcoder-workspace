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
# input = sys.stdin.readline
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

H,W,K = LII()
S = [I() for _ in range(H)]

def check(n):
    for i in range(1<<(H-1)):
        x = n
        g = []
        s = 0
        for j in range(H):
            if i>>j&1:
                g.append((s,j+1))
                s = j+1
        g.append((s,H))
        dprint(g)
        t = [0]*H
        for g_index,(l,r) in enumerate(g):
            for i in range(l,r):
                t[i]=g_index
        dprint(t)
        x -= len(g)-1 
        if x<0:
            continue

        cnt = [0]*len(g)
        for j in range(W):
            copy_cnt = cnt[:]
            for i in range(H):
                if S[i][j]=="1":
                    cnt[t[i]]+=1
            dprint(i,j,cnt)
            if max(cnt)>K:
                x -= 1
                dprint(j,x)
                cnt = [x-y for x,y in zip(cnt, copy_cnt)]
                if max(cnt)>K:
                    break
            if x <0:
                break
        else:
            return True
    return False

# dprint(check(0))
# dprint(check(1))
# dprint(check(2))
# dprint(check(3))

l = -1
r = W-1+H-1
while r-l >1:
    mid =(l+r)//2
    if check(mid):
        r = mid
    else:
        l = mid

print(r)