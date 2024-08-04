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

# A = [2, 5, 6, 5, 2, 1, 7]

# N = len(A)
# sm = 0
# for i in range(N-1):
#     x = 0
#     for j in range(i+1,N):
#         aa = 0
#         for x in range(i,j+1):
#             aa ^= A[x]
#         sm += aa


# def total_xor_sum(A):
#     N = len(A)
#     # 累積 XOR 配列を計算
#     prefix_xor = [0] * N
#     prefix_xor[0] = A[0]
#     for i in range(1, N):
#         prefix_xor[i] = prefix_xor[i - 1] ^ A[i]

#     sm = 0
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if i == 0:
#                 aa = prefix_xor[j]
#             else:
#                 aa = prefix_xor[j] ^ prefix_xor[i - 1]
#             sm += aa

#     return sm


def total_xor_sum(A):
    N = len(A)
    # 最大ビット長を計算
    max_bit_length = max(A).bit_length()
    
    sm = 0
    for bit in range(max_bit_length):
        count_ones = 0
        xor = 0
        count_zeros =1
        count_ones = 0
        for a in A:
            xor ^= a>>bit&1
            if xor:
                count_ones += 1
            else:
                count_zeros += 1
        sm += count_zeros * count_ones * (1 << bit)

    return sm - sum(A)


sm = total_xor_sum(A)
print(sm)

