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
A = LII()
B = LII()

cnt_a = Counter(A)
cnt_b = Counter(B)
if cnt_a  != cnt_b:
    print("No")
    exit()

v = list(cnt_a.values())
if max(v) > 1:
    print("Yes")
    exit()

from atcoder.fenwicktree import FenwickTree


def count_tr(A):
    ret = 0
    ft = FenwickTree(5000)
    for a in A[::-1]:
        a -= 1
        ft.add(a,1)
        ret += ft.sum(0,a)
    return ret

# print(count_tr([1,2,2]))
# print(count_tr([2,1,2]))

a = count_tr(A)
b = count_tr(B)

if a%2 == b%2:
    print("Yes")
else:
    print("No")