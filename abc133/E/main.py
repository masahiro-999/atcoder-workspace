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

def prepare(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
 
    return factorials, invs


def choose(n,a):
    if a == 0:
        return 1
    if n<a or a <0:
        return 0
    return (factorials[n] * (invs[n-a] * invs[a])) % MOD

def perm(x,k):
    if k == 0:
        return 1
    if k <0 or x < k:
        return 0
    return (factorials[x] * invs[x-k]) % MOD


MOD = 1000000007
factorials, invs = prepare(100000,MOD)
N,K = LII()

g = defaultdict(list)

for _ in range(N-1):
    a,b = LII()
    a -=1
    b -=1
    g[a].append(b)
    g[b].append(a)


ans = 1

@bootstrap
def dfs(s,p):
    global ans
    if p is None:
        x = K
        n = len(g[s])+1
    else:
        x = K-2
        n = len(g[s])-1

    if n <0 or x < n:
        ans = 0
    ans *= (factorials[x] * invs[x-n]) % MOD
    ans %= MOD
    # print(s,p,x,n,ans)
    for ns in g[s]:
        if ns == p:
            continue
        yield dfs(ns,s)
    yield

dfs(0,None)

print(ans)