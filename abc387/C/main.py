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

L,R = LII()

def f1(n):
    ret = 0
    str_n = str(n)
    K = len(str_n)
    for i in range(K-2):
        for j in range(1,10):
            ret += j**(i+1)
            # print(i,j,ret)
    return ret

def f2(n):
    ret = 0
    str_n = str(n)
    K = len(str_n)
    for top in range(1,int(str_n[0])):
        ret += top**(K-1)
    return ret

def f3(n):
    ret = 0
    str_n = str(n)
    K = len(str_n)
    top = int(str_n[0])
    for k in range(1,K):
        ret += min(top,int(str_n[k]))*top**(K-1-k)
        if int(str_n[k])>= top:
            break
    return ret

def f4(n):
    if n < 10:
        return 0
    ret = 1
    str_n = str(n)
    K = len(str_n)
    top = int(str_n[0])
    for i in range(1,K):
        if int(str_n[i])>=top:
            ret = 0
    return ret

def f(n):
    if n <10:
        return 0
    else:
        return f1(n)+f2(n)+f3(n)+f4(n)

ans = f(R) - f(L-1)

print(ans)
# x = 210
# print(f1(x))
# print(f2(x))
# print(f3(x))
# print(f(x))
# print(f(8))



# cnt = 0
# for i in range(1,100000):
#     cnt += f4(i)
#     if cnt != f(i):
#         print(i,cnt, f(i))

