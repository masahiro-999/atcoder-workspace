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


def solve(R: int, G: int, B: int, N: int):
    ans = 0
    for i in range(N//R+1):
        for j in range((N-R*i)//G+1):
            n_rem = N-i*R-j*G
            if n_rem < 0:
                continue
            if n_rem % B == 0:
                ans += 1
    print(ans)

def main():
    R = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(R, G, B, N)
    return

main()
