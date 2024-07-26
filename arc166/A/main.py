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
inf = 100100100100
debug = False
# debug = True
if debug:
    def dprint(*arg): print(*arg, file=sys.stderr)
else:
    def dprint(*arg): pass

T = II()

def split_list_by_c(x,y):
    for is_separator, group in groupby(zip(x,y), key=lambda x: x[1] == "C"):
        if not is_separator:
            yield list(group)

for _ in range(T):
    N,X,Y = LI()
    N = int(N)
    ans = "Yes"
    for i in range(N):
        if Y[i] == "C" and X[i] != "C":
            ans = "No"
            break
        
    for Z in split_list_by_c(X,Y):
        x,y = zip(*Z)
        x = list(x)


        cnt_x = Counter(x)
        cnt_y = Counter(y)

        add_a = cnt_y["A"] - cnt_x["A"] 
        add_b = cnt_y["B"] - cnt_x["B"]
        if add_a < 0 or add_b < 0:
            ans = "No"
        for i in range(len(x)):
            if add_a >0 and x[i] == "C":
                x[i] = "A"
                add_a -= 1
                if add_a == 0:
                    break
        for i in range(len(x)):
            if x[i] == "C":
                x[i] = "B"

        sm = 0
        for i in range(len(x)):
            if x[i] == "A":
                sm +=1
            if y[i] == "A":
                sm -=1
            if sm < 0:
                ans = "No"
                break

    print(ans)

    # ABAB 
    # BBAA