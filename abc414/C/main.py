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
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
sys.setrecursionlimit(10000000)
inf = float('inf')

A = II()
N = II()

ans = 0

# for i in range(min(N,9)+1):
#     str8 = []
#     n = i
#     while n>0:
#         str8+=str(n%8)
#         n//=8
#     if str8 == str8[::-1]:
#         ans += i
#         print(i)


str_n = str(N)
n = len(str_n)
topn = 10**((n+1)//2)
# print(topn)
for j in range(2):
    for i in range(1,int(topn)+1):
        str_i = str(i)
        len_i = len(str_i)
        bottom = str_i[:len_i-1+j][::-1]
        a = int(str_i+bottom)
        # print(i,j,str_i, bottom)
        if a > N:
            break
        str8 = []
        n = a
        while n>0:
            str8.append(n%A)
            n//=A
        str8n = (len(str8)+1)//2
        if str8[:str8n] == str8[-str8n:][::-1]:
            ans += a
            # print(a)
        
print(ans)
