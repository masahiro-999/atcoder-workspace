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


def solve(N: int):
    d = defaultdict(set)
    s = 0
    i = 1
    while s < N:
        s += i
        i += 1
    max_i = i
    ans = set([i for i in range(1,max_i)])
    if s-N > 0:
        ans.remove(s - N)
    return list(ans)

def main():
    ans = set()
    N = int(next(tokens))  # type: int
    ans = solve(N)
    print(*ans, sep="\n")
    return

main()
