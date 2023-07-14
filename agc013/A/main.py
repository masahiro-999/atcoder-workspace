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

def find_next_start(N, A, start):
    if N-start < 3:
        return N
    i = start
    prev_a = A[i]
    prev_d = 0
    i += 1
    while i < N:
        a = A[i]
        if a > prev_a:
            d = 1
        elif a < prev_a:
            d = -1
        else:
            d = 0
        if prev_d != 0 and d != 0 and d != prev_d:
            return i
        if prev_d == 0:
            prev_d = d
        prev_a = a
        i += 1
    return i

def solve(N: int, A: "List[int]"):
    ans = 0
    start = 0
    while start<N:
        ans += 1
        start = find_next_start(N,A,start)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)
    return

main()
