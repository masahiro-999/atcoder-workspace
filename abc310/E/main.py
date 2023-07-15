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


def solve(N: int, S: str):
    def nand(a,b):
        return 1- (a & b)

    a = [int(x) for x in S]
    a1 = [0] * N
    a1[0] = a[0]
    for i in range(1,N):
        a1[i] = nand(a1[i-1],a[i])

    a2 = [0] * N
    a2[1] = a[1]
    for i in range(2,N):
        a2[i] = nand(a2[i-1],a[i])

    # print(a1)         
    # print(a2)
    ans = 0
    f = 1         
    for i in range(0,N,2):
        ans += a1[i]*f
        f += 1

    f = 1
    for i in range(1,N,2):
        ans += a2[i]*f
        f += 1

    print(ans)


def main():
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)
    return

main()
