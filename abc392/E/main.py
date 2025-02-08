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

N,M = LII()
AB = [LII() for _ in range(M)]

from atcoder.dsu import DSU

duble = []

dsu = DSU(N)

num_group = N

for i,(a,b) in enumerate(AB):
    a -= 1
    b -= 1
    if dsu.same(a,b):
        duble.append(i)
    else:
        dsu.merge(a,b)
        num_group -= 1

leader_list = []

for x_list in dsu.groups():
    leader_list.append(dsu.leader(x_list[0]))

# print(leader_list)

NN = len(leader_list)
leader_index = Counter()
for i,leader in enumerate(leader_list):
    leader_index[leader] = i

dsu2 = DSU(N)
# leader毎の使用できるiのList
duble_leader = defaultdict(list)
for i in duble:
    a,b = AB[i]
    a -= 1
    b -= 1
    u = leader_index[dsu.leader(a)]
    duble_leader[u].append(i)

not_connected = set(range(NN))

not_connected2 = [x for x in not_connected if len(duble_leader[x]) != 0]
not_connected3 = [x for x in not_connected if len(duble_leader[x]) == 0]
all = not_connected2+not_connected3
# print()
q = []
ans = []
for x in duble_leader[all[0]]:
    q.append(x)
for target in all[1:]:
    # print("start", q)
    i = q.pop()
    a,b = AB[i]
    c = leader_list[target]+1
    ans.append((i+1,a,c))
    for x in duble_leader[target]:
        q.append(x)
    # print(i,a,b,c,q)

print(len(ans))
for x in ans:
    print(*x)
