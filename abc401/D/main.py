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
from itertools import product, accumulate,permutations,combinations, count, groupby
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

import random

N,K = LII()
S = I()

# K = 5
# N = 10

# while True:
#     S =[random.choice(".o?") for _ in range(N)]
#     S = "".join(S)
#     for i in range(len(S)-1):
#         if S[i:i+2]=="oo":
#             break
#     else:
#         break


num_o = len(list(x for x in S if x=="o"))
num_q = len(list(x for x in S if x=="?"))
num_d = len(list(x for x in S if x=="."))

# K = num_o + random.randrange(num_q+1)
# print(S,K)

T = [t for t in S]

def fill(T0):
    T = T0[::]
    for i in range(len(T)):
        if T[i] == "?":
            if i == 0 or T[i-1]==".":
                T[i] = "o" 
            else:
                T[i] = "."
    # print(T0,T)
    return T

for i in range(N-1):
    if T[i]=="o" and T[i+1]=="?":
        T[i+1] = "."
        num_q -= 1
        num_d +=1
    if T[i]=="?" and T[i+1]=="o":
        T[i] = "."
        num_q -= 1
        num_d +=1

max_o = 0
for k,v in groupby(T):
    g = len(list(v))
    if k == "?":
        max_o += (g+1)//2
free_o = K - num_o
# print(f"{max_o=}")
# print(f"{free_o=}")

if free_o == 0:
    for i in range(N):
        if T[i] == "?":
            T[i] = "." 
elif free_o == max_o:
    T1 = fill(T)
    T2 = fill(T[::-1])[::-1]
    for i,t1,t2 in zip(count(),T1,T2):
        if t1 != t2:
            T[i] = "?"
        else:
            T[i] = t1


print("".join(T))