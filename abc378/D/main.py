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


from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

H,W,K = LII()
S = [I() for _ in range(H)]

visited = [[False]*W for _ in range(H)]

cnt = 0
@bootstrap
def dfs(sy,sx,k):
    global cnt
    # print(sy,sx,k, visited)
    if k == 0:
        cnt += 1
        yield

    # sx,sy からK回移動する。同じ場所は通らない。
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        x,y = sx,sy
        x += dx
        y += dy
        if x < 0 or x >= W or y < 0 or y >= H:
            continue
        if S[y][x] == "#":
            continue
        if visited[y][x]:
            continue
        visited[y][x] = True
        yield dfs(y,x,k-1)
        visited[y][x] = False
    yield
    
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            visited[i][j] = True
            cnt = 0
            dfs(i,j,K)
            visited[i][j] = False
            ans += cnt
print(ans)

# cnt = 0
# visited[0][0] = True
# dfs(0,0,K)
# print(cnt)

