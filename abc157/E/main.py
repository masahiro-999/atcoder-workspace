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

N = II()
S = [x for x in I()]
Q = II()


from atcoder.fenwicktree import FenwickTree

ft = defaultdict(lambda : FenwickTree(N))

for i,s in enumerate(S):
    ft[s].add(i,1)
    # dprint(i,s,[ft[s].sum(i,i+1) for i in range(N)])


for _ in range(Q):
    cmd, a,b = LI()
    if cmd == "1":
        i = int(a)-1
        now = S[i]
        ft[now].add(i,-1)
        ft[b].add(i,1)
        S[i]=b
        # dprint(cmd,a,b,[ft[b].sum(i,i+1) for i in range(N)])

    else:
        l,r = int(a)-1, int(b)+1-1
        dup = 0
        for k,v in ft.items():
            dup += max(0,v.sum(l,r)-1)
            # if v.sum(l,r)>1:
            #     dprint(k,[v.sum(i,i+1) for i in range(N)])
        # dprint(r-l-dup, dup,l,r,[ft["a"].sum(i,i+1) for i in range(N)])
        print(r-l-dup)