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
S = I()

if S == "1":
    ans = 10**10*2
    print(ans)
    exit()
        
def check110(S):
    for i in range(len(S)//3):
        if S[i*3:i*3+3]!="110":
            return False
    return True

ans = 0
for n1 in range(3):
    if n1>0 and "110"[-n1:] != S[:n1]:
        continue        
    if not check110(S[n1:]):
        continue
    n2 = (N-n1)//3
    r = S[n1+n2*3:]
    n3 = len(r)        
    if "110"[:n3] == r:
        x = 0
        if n1>0:
            x += 1
        if n3>0:
            x += 1
        ans = 10**10-(n2-1) - x
        break

print(ans)