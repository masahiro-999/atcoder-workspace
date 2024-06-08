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
input = sys.stdin.readline
# input = lambda: sys.stdin.readline().rstrip("\r\n")
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
from atcoder.scc import SCCGraph


N = II()
A = LII()

scc_g = SCCGraph(N)

g = defaultdict(int)
b = defaultdict(list)

for i,a in enumerate(A):
    a -= 1
    g[i]=a
    b[a].append(i)
    scc_g.add_edge(i,a)

S = scc_g.scc()
dprint(S)

result = [0]*N
loop_node_set = set()

for s in S:
    if len(s)==1 and g[s[0]]!=s[0]:
        continue
    for i in s:
        result[i] = len(s)
        loop_node_set.add(i)

def dfs(v,ans):
    result[v] = ans
    for n in b[v]:
        dfs(n, ans+1)

for s in loop_node_set:
    for n in b[s]:
        if n not in loop_node_set:
            dfs(n, result[s]+1)

dprint(result)
ans = sum(result)
print(ans)

