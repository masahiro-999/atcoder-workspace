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


def solve(N: int, h: "List[int]"):
    def find_nonzero(h):
        a = 0
        while a < N:
            if h[a] != 0:
                break
            a+= 1
        if a == N:
            return None,None
        b = a
        while b < N:
            if h[b] == 0:
                break
            b += 1
        return a,b

    ans = 0
    while True:
        a,b = find_nonzero(h)
        if a is None:
            break
        ans += 1
        for i in range(a,b):
            h[i] -= 1
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, h)
    return

main()
