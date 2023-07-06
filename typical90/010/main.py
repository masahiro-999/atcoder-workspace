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


def solve(N: int, C: "List[int]", P: "List[int]", Q: int, L: "List[int]", R: "List[int]"):
    c1 = [P[i] if C[i]==1 else 0 for i in range(N)]
    c2 = [P[i] if C[i]==2 else 0 for i in range(N)]

    a1 = list(accumulate(c1))
    a2 = list(accumulate(c2))

    def get_ans(l,r,a):
        if l == 0:
            s = 0
        else:
            s = a[l-1]
        return a[r] - s
    for l,r in zip(L,R):
        print(get_ans(l-1,r-1,a1), get_ans(l-1,r-1,a2))

def main():
    N = int(next(tokens))  # type: int
    C = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        C[i] = int(next(tokens))
        P[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, C, P, Q, L, R)
    return

main()
