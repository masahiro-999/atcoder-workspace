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

from types import GeneratorType

N = II()

@cache
def f(N):
    str_n = str(N)
    if str_n == "1"*len(str_n):
        return (str_n,False)
    ret = []
    for i in range(1,N):
        x1,_ = f(N-i)
        x2,_ = f(i)
        ret.append((x2+"+"+x1,True))
    for i in range(2,isqrt(N)+1):
        if N % i !=0:
            continue
        j = N//i
        x1,f1 = f(i)
        if f1:
            x1 = "("+x1+")"
        x2,f2 = f(j)
        if f2:
            x2 = "("+x2+")"
        ret.append((x1+"*"+x2,False))
    return min(ret, key=lambda x: (len(x[0]),x[1]))

ans,_ = f(N)
print(ans)

# for i in range(1,2000):
#     ans,_ = f(i)
#     if eval(ans) == i:
#         print(i,ans)