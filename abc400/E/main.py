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

NN=1000000
prime_list = get_prime_list(NN)


ptable=set()

for p1 in prime_list:
    for p2 in prime_list:
        if p1 == p2:
            continue
        if p1 * p2 > NN:
            break
        i = 1
        p1n = p1
        while True:
            j = 1
            p2n = p2
            while True:
                x = p1n*p2n
                if x > NN:
                    break
                ptable.add(x)
                p2n *= p2
            p1n *= p1
            if p1n > NN:
                break

ptable = list(ptable)
ptable.sort()

# print(ptable[:10])


Q = II()
for _ in range(Q):
    AA = II()
    A = isqrt(AA)
    i = bisect_right(ptable,A)
    ans = ptable[i-1]**2
    # print(AA,A,i,ptable[i],ans)   
    print(ans)