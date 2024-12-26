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

prime_list = get_prime_list(1000000)

ans = 1

p_list = []
num_list = []
for p in prime_list:
    cnt = 0
    while N!=1 and N%p == 0:
        N //= p
        cnt += 1
    if cnt >0:
        p_list.append(p)
        num_list.append(cnt)

if N != 1:
    p_list.append(N)
    num_list.append(1)

ans = []

# print(p_list)
# print(num_list)

for orders in product(*[range(x+1) for x in num_list]):
    a = 1
    for i,x in enumerate(orders):
        # print(x,p_list[i],a)
        # print(i,x)
        a*= p_list[i]**x
    ans.append(a)

ans.sort()
print(*ans, sep="\n")