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


def solve(N: int, L: "List[int]", R: "List[int]"):
    table = [0]*(200000+1)

    for l,r in zip(L, R):
        table[l] += 1
        table[r] -= 1

    ans = []
    t_sum = 0
    s = 0
    prev = t_sum
    for i,t in enumerate(table):
        t_sum += t
        if prev == 0 and t_sum > 0:
            s = i
        if prev > 0 and t_sum == 0:
            ans.append((s,i))
        prev = t_sum

    for s,e in ans:
        print(s,e)


def main():
    N = int(next(tokens))  # type: int
    L = [int()] * (N)  # type: "List[int]"
    R = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, L, R)
    return

main()
