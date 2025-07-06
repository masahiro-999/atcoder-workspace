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

@bootstrap
def get_min(P):

    N = len(P)
    if N==1:
        yield P

    P1 = P[:N//2]
    P2 = P[N//2:]

    ret1 = yield get_min(P1)
    ret2 = yield get_min(P2)

    yield ret1+ret2 if ret1 <  ret2 else ret2+ret1


T = II()
for _ in range(T):
    N = II()
    P = LII()
    ans = get_min(P)
    print(*ans)

"""
1 5 6 7 2 4 3 8

5 1 6 7 2 4 3 8

8 3 4 2 1 5 7 6

2 4 3 8 1 5 6 7




1 5 6 7 2 4 3 8



1 
1 4 2 3     3 2 4 1


8 3 4 2 1 5 7 6


"""