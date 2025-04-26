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
inf = 100100100100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

N = II()
S = I()
T = I()

NS = [ord(s)-ord("a") for s in S]
NT = [ord(t)-ord("a") for t in T]

used = [0]*26

g = [-1]*26
rev_g = [set() for _ in range(26)]

from atcoder.scc import SCCGraph
scc_graph = SCCGraph(26)

for ns,nt in zip(NS,NT):
    if g[ns] != -1 and g[ns] != nt:
        print(-1)
        exit()
    g[ns] = nt
    used[ns] = 1
    rev_g[nt].add(ns)
    scc_graph.add_edge(ns,nt)

scc = scc_graph.scc()
ans = 0

ans = sum(g[x] != x for x in range(26) if used[x])

cnt_single = 0
ng = 1
for node_list in scc:
    set_node_list = set(node_list)
    only_self = True
    for x in node_list:
        if (rev_g[x] | set_node_list != set_node_list):
            only_self = False
    cnt = 1
    if (len(node_list)==1) or  not only_self:
        cnt = 0
    if (len(node_list)==1 and not used[node_list[0]]) or  not only_self:
        ng = 0
    if (len(node_list)==1 and used[node_list[0]]) and only_self:
        cnt_single += 1
    ans += cnt
    

if cnt_single == len(scc):
    ng = 0

if ng:
    print(-1)
    exit()

print(ans)
