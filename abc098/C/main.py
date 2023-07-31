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
    n_left = list(accumulate([1 if x == "W" else 0 for x in S]))
    n_right = list(accumulate([1 if x == "E" else 0 for x in S[::-1]]))[::-1]

    ans = inf
    for i in range(N):
        if i == 0:
            left = 0
        else:
            left = n_left[i-1]

        if i == N-1:
            right = 0
        else:
            right = n_right[i+1]
        ans = min(ans, left+right)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)
    return

main()
