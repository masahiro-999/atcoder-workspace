import sys
import os
from math import ceil, floor, sqrt, pi, factorial, gcd,lcm,sin,cos,tan,asin,acos,atan2,exp,log,log10, isqrt, comb
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce, cache
from operator import add, iand, ior, itemgetter, mul, xor
from string import ascii_lowercase, ascii_uppercase, ascii_letters
from typing import *
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import product, accumulate,permutations,combinations, count, groupby
from dataclasses import dataclass
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = float('inf')

N,Q = LII()

@dataclass
class TrieNode:
    children: dict
    s : str
    parent: dict

sv = None
PC = [None]*N
for _ in range(Q):
    q = LI()
    if q[0]=="1":
        p = int(q[1])
        PC[p-1] = sv
    elif q[0]=="2":
        p = int(q[1])
        s = q[2]
        new_node = TrieNode(None,s,PC[p-1])
        if PC[p-1]:
            PC[p-1].children = new_node
        PC[p-1]= new_node
    else:
        p = int(q[1])
        sv = PC[p-1]

ans = []
while sv:
    ans.append(sv.s)
    sv = sv.parent

print("".join(ans[::-1]))