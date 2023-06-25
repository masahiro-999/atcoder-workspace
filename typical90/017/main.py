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


def solve(N: int, M: int, L: "List[int]", R: "List[int]"):
    def is_cross(l1, r1, l2, r2):
        if l1 in [l2,r2] or r1 in [l2,r2]:
            return False
        if l1 > r1:
            l1,r1 = r1,l1
        if l2 > r2:
            l2,r2 = r2,l2
        return (l1 < l2 < r1)  != (l1 < r2 < r1) 

    ans = 0
    for i in range(M-1):
        for j in range(i+1,M):
            if is_cross(L[i],R[i],L[j],R[j]):
                ans += 1
    print(ans)
def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, M, L, R)
    return

main()
