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

def f(n, flag):
    # print(n, flag)
    if n == 0:
        return flag
    elif n == 1:
        return not flag
    bitlen = n.bit_length()
    return f(n - (1 << (bitlen-1)), not flag)

# print(f(3, False))
# print(f(4, False))
# print(f(5, False))
# print(f(6, False))

S = I()
Q = II()
ans = []
for k in LII():
    k -= 1
    l = len(S)
    n = k//l
    r = k%l
    x = f(n, False)
    s = S[r]
    if x:
        if s in ascii_lowercase:
            s = s.upper()
        else:
            s = s.lower()
    ans.append(s)

print(*ans)