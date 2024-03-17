import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10, comb
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

def conb2(a):
    return a*(a-1)//2

def solve(N: int, A: "List[int]"):
    c = Counter(A)

    ans = 0
    for _i,v in c.items():
        if v < 2:
            continue
        ans += conb2(v)

    for i in range(N):
        v = c[A[i]]
        if v < 2:
            print(ans)
        else:
            print(ans - conb2(v) + conb2(v-1))

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)
    return

main()
