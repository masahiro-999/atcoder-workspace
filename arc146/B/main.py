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

N,M,K = LII()
A = LII()

def f(A,x: int,m: int):
    n = x.bit_length()
    c = []
    for a in A:
        b = 0
        for i in range(n)[::-1]:
            if (x>>i&1)==1 and (a>>i&1)==0:
                b += 1<<i
            if (a>>i&1) ==1 and (x>>i&1)==0 and b > 0:
                b -= 1<<i
            # print(a,x,i,b,flag)
            
        c.append(b)
    # print(x,A,c)
    c.sort()
    return sum(c[:K]) <=m

# assert f([4],10,8)
# exit()
# x=1010
# a=0000
# b=1001010

L = 31
ok = 0
ng = (1<<L)
while ng - ok > 1:
    mid = (ok + ng) // 2
    if f(A, mid, M):
        ok = mid
    else:
        ng = mid
print(ok)


