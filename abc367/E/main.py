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

N, K = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

NN = 60  # 最大2^60回の操作に対応できるように設定

# ダブリングのテーブルを作成
d1 = [[0] * N for _ in range(NN+1)]

# 1回の操作後の位置を初期化
for i in range(N):
    d1[0][i] = X[i]-1

# ダブリングの事前計算
for i in range(1, NN):  # 2^1, 2^2, ..., 2^NN回後の位置を計算
    for j in range(N):
        d1[i][j] = d1[i-1][d1[i-1][j]]

# K回操作した後の配列Aを求める
for i in range(NN):
    if (K >> i) & 1:  # Kのiビット目が1なら、その操作を適用
        A2 = [0] * N
        for j in range(N):
            A2[j] = A[d1[i][j]]
        A = A2

print(*A)