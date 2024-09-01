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

H,W,N = LII()
RC = [[x-1 for x in LII()] for _ in range(N)]
RC.append([H-1,W-1])
RC.append([0,0])
RC.sort()
ans = 0
# print(RC)

# 最大値を求めるsegtreeを使う
from atcoder.segtree import SegTree

st = SegTree(max, (0,-1) , W)

back = [0]*(len(RC))
for i in range(len(RC)):
    r,c = RC[i]
    mx_value,idx = st.prod(0,c+1)
    back[i] = idx
    st.set(c,(mx_value+1,i))

# for i in range(W):
#     print(st.get(i))
# print(back)
# back[N-1]から逆にたどっていく
ans = st.all_prod()[0]
path = []
i,j = H-1,W-1
p = len(RC)-1
while i != 0 or j != 0:
    p = back[p] 
    ni,nj = RC[p]
    di = i-ni
    dj = j-nj
    path.append((di,dj))
    i,j = ni,nj

print(ans-2)
for di,dj in path[::-1]:
    print("D"*di,end="")
    print("R"*dj,end="")
print("")