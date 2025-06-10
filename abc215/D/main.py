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

N,M = LII()
A = LII()

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

prime_list = get_prime_list(isqrt(M))

p = set()

for a in A:
    for prime in prime_list:
        if a < prime:
            break
        if a % prime == 0:
            p.add(prime)
            while a % prime == 0:
                a //= prime
    if a != 1:
        p.add(a)

# print(p)
t = [0]*(M+1)
for prime in p:
    x = prime
    while x <= M:
        t[x] = 1
        x += prime
ans = []
for i in range(1,M+1):
    if t[i] == 0:
        ans.append(i)


print(len(ans))
print(*ans, sep="\n")
