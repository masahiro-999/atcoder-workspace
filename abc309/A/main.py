import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
try:
    from pypyjit import set_param
    set_param('max_unroll_recursion=-1')
except ModuleNotFoundError:
    pass
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())

YES = "Yes"
NO = "No"

def solve(A: int, B: int):
    ah = (A-1)//3
    aw = (A-1)%3
    bh = (B-1)//3
    bw = (B-1)%3
    if (ah == bh) and aw+1 == bw:
        print(YES)
    else:
        print(NO)

def main():
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)
    return

main()
