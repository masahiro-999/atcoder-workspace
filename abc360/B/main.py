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

S,T = LI()

N = len(S)

def f(w,c):
    a = []
    i = 0
    while True:
        x = S[i*w:(i+1)*w]
        if x == "":
            break
        a.append(x)
        i+= 1

    ret = []
    for x in a:
        if c-1 < len(x):
            ret.append(x[c-1])
    return "".join(ret)

for w in range(1,N):
    for c in range(1,w+1):
        x = f(w,c)
        # print(w,c,x)
        if x == T:
            print("Yes")
            exit()

print("No")