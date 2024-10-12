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
A = [I() for _ in range(N)]

B = [["X"]*N for _ in range(N)]

def rotate(x,y,dir):
    if dir == 0:
        return x,y
    if dir == 1:
        return y,N-x-1
    if dir == 2:
        return N-x-1,N-y-1
    if dir == 3:
        return N-y-1,x

# print(rotate(0,0,1))
# print(rotate(0,0,2))
# print(rotate(0,0,3))
# print(rotate(0,0,4))

def copy(A,B,n,dir):
    # Aの外側からn週目をBに90*dir度回転してコピー
    for j in range(4):
        for i in range(N-n*2):
            x0 = n+i
            y0 = n
            x1,y1 = rotate(x0,y0,j)
            dist_x, dist_y = rotate(x1,y1,dir)
            # print(x0,y0,x1,y1,dist_x,dist_y)
            B[dist_x][dist_y] = A[x1][y1]
dir = 0
for n in range(N//2):
    dir += 1
    dir %= 4
    copy(A,B,n,dir)
for b in B:
    print("".join(b))

# copy(A,B,1,1)
# for b in B:
#     print("".join(b))

