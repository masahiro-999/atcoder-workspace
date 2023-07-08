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


def solve(N: int, K: int, ab):
    ab.sort(key=lambda x: x[0], reverse=True)
    sum_b = 0
    ans_i = -1
    for i in range(N):
        sum_b += ab[i][1]
        if sum_b > K:
            ans_i = i
            break
    if ans_i == -1:
        print(1)
    else:
        ans = ab[ans_i][0]+1
        print(ans)


def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    ab = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        ab[i] = (int(next(tokens)),int(next(tokens)))
    solve(N, K, ab)
    return

main()
