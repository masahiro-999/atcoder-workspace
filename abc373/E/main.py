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

N,M,K = LII()
A = LII()

B = [(a,i) for i,a in enumerate(A)]
B.sort()

dprint(B)

SA = sorted(A)
accSA = list(accumulate(SA, initial=0))

total_K = sum(A)
k = K - total_K

def check(i: int ,x: int, k: int):
    # 対象の得票数がa 現在の得票数のTOP　M人（対象を除く）b,残りの票がkの時、aがx追加で獲得した時、勝てるかどうか
    t = SA[i]+x
    n = 0
    r = bisect_left(SA,t+1)
    l = N-M
    if i >= l:
        l -= 1
    if r < l:
        return False
    sm = (accSA[r] - accSA[l])
    n1 = r-l
    n = (t+1)*n1 - sm
    if i >= l:
        n -= x + 1
    # dprint(20,i,r,n,t,sm,n1)
    return n > k-x


if M ==N:
    print(*([0]*N))
    exit()
# dprint(k)
# dprint(check(3,0,k))
# dprint(check(3,1,k))
# dprint(check(3,2,k))
# dprint(check(3,3,k))

ans = [0] * N
for i in range(N):
    if check(i,k,k) == False:
        ans[i] = -1
        continue
    if check(i,0,k):
        ans[i] = 0
        continue
    mi = 0
    mx = k
    while mx - mi > 1:
        md = (mx+mi)//2
        if check(i,md,k):
            mx = md
        else:
            mi = md
    ans[i] = mx

ans = [(B[i][1],a) for i,a in enumerate(ans)]
ans.sort()
ans = [a for i,a in ans]
print(*ans)
