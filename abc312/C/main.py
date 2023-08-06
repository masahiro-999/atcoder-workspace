import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect, bisect_left
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


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    def num_b(x):
        # if B[0] > x:
        #     return M
        # if B[M-1] < x:
        #     return 0
        return M-bisect_left(B, x)
    def num_a(x):
        # if A[0] > x:
        #     return 0
        # if A[N-1] < x:
        #     return N
        return bisect(A, x)

    A.sort()
    B.sort()
    ans = A[0]
    l = min(B[0], A[0])-1
    r = max(A[N-1], B[M-1])+1
    while r-l > 1:
        x = (r+l) //2
        if num_a(x) >= num_b(x):
            r = x
        else:
            l = x
    print(r)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, A, B)
    return

main()
