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
H = LII()

X = {v: i for i, v in enumerate(sorted(set(H)))}
CH = [X[v] for v in H]
max_ch = max(CH)

from atcoder.lazysegtree import LazySegTree

id_ = inf
e = -inf
ID = inf

def mapping(func, ele):
    if func == ID:
        return ele
    else:
        return func


def composition(func_upper, func_lower):
    if func_upper == ID:
        return func_lower
    else:
        return func_upper


st = LazySegTree(lambda x,y: max(x,y), e, mapping, composition, id_, max_ch+1)


st.apply(0,max_ch+1,0)
# st.apply(1,3,1)

# for i in range(max_ch+1):
#     print(st.get(i))


a = [0]*(N+1)
prev_h = 0
for i in range(1,N+1):
    left = st.get(CH[i-1])
    # print(left)
    a[i] = (i-left)*H[i-1]+a[left]
    st.apply(0,CH[i-1]+1,i)

ans = [x+1 for x in a[1:]]
print(*ans)
