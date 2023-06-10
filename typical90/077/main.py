import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())

YES = "Yes"
NO = "No"

def solve(N: int, T: int, AX: "List[int]", AY: "List[int]", BX: "List[int]", BY: "List[int]"):

def main():
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    AX = [int()] * (N)  # type: "List[int]"
    AY = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        AX[i] = int(next(tokens))
        AY[i] = int(next(tokens))
    BX = [int()] * (N)  # type: "List[int]"
    BY = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        BX[i] = int(next(tokens))
        BY[i] = int(next(tokens))
    solve(N, T, AX, AY, BX, BY)
    return

main()
