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

hash = [0]*(N+1)

b = 1000000007
p = 998244353
b_inv = pow(b,-1,p)
b_inv_table =[0]*N

x = 1
for i in range(N):
    b_inv_table[i]=x
    x *= b_inv
    x %= p

bx = 1
for i in range(N)[::-1]:
    hash[i] = (hash[i+1]+(ord(S[i])-ord("a")+1)*bx)%p
    bx *=b

t = defaultdict(list)
for i,s in enumerate(S):
    t[s].append(i)

for k in t.keys():
    t[k].sort()

def cmphash(i,j,n):
    return ((hash[i] - hash[i+n])*b_inv_table[N-i-n])%p == ((hash[j]- hash[j+n])*b_inv_table[N-j-n])%p

# print(cmphash(0,2,2))

def check(n):
    if n == 0:
        True
    for i in range(N-n):
        for j in t[S[i]]:
            if j <i+n or j+n>N:
                continue
            if cmphash(i,j,n):
                return True
    return False

# print(check(2))

l = 0
r = N
while r-l >1:
    mid = (l+r)//2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)

