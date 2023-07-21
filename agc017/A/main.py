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

MOD = 2

def comb(n,m):
    ret = 1
    for i in range(m):
        ret *= n-i
    for i in range(m):
        ret //= i+1
    return ret

def solve(N: int, P: int, A: "List[int]"):
    a = [x % 2 for x in A]
    c = Counter(a)
    n_zero = c[0]
    n_one = c[1]
    ans = 0
    for i in range(P, n_one+1, 2):
        ans += comb(n_one,i)
    ans *= 2** n_zero
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, A)
    return

main()
