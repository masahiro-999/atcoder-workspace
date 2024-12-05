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

N = II()
X = LII()

def get_prime_list(num_max):
    prime_table=[1]*(num_max+1)
    prime_table[0] = 0
    prime_table[1] = 0
    for i in range(2, num_max+1):
        k = i*2
        while k <= num_max:
            prime_table[k] = 0
            k += i
    return [i for i in range(2,num_max+1) if prime_table[i]]

prime_list = get_prime_list(50)
# print(prime_list)

n = len(prime_list)

t=[True]*(1<<n)

for x in X:
    b = 0
    for i in range(n):
        if x % prime_list[i]==0:
            b |= 1<<i
    # print(x,b)
    for i in range(1<<n):
        if (i & b) ==0:
            t[i] = False
            # print(i)

ans = None
for i in range(1<<n):
    if t[i] :
        a = 1
        for j in range(n):
            if i>>j&1:
                a *= prime_list[j]
        if ans is None:
            ans = a
        ans = min(ans,a) 

print(ans)
