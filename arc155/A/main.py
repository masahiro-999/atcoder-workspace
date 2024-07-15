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

T = II()

def is_kaibun(S):
    n =len(S)//2
    if n == 0:
        return True
    return S[:n] == S[-n:][::-1]

assert(is_kaibun("a"))
assert(is_kaibun("aa"))
assert(is_kaibun("aba"))

for _ in range(T):
    N,K = LII()
    S = I()
    S = [x for x in S]

    n,K = divmod(K,2*N)
    # if n %2 == 1:
    #     S=S[::-1]
    r = K - N
    if r <= 0:
        R = S[:K][::-1]
        if is_kaibun(S+R) and is_kaibun(R+S):
            ans = "Yes"
        else :
            ans = "No"
    else:
        assert r >= 0
        R = S[-r:][::-1]
        RS = S[::-1]
        if is_kaibun(S+R+RS) and is_kaibun(R+RS+S):
            ans = "Yes"
        else :
            ans = "No"
    print(ans)