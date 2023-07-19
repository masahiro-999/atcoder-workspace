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

YES = "YES"
NO = "NO"

def solve(N: int, D: "List[int]", M: int, T: "List[int]"):
    d_count = Counter(D)

    ans = YES
    for t in T:
        if d_count[t] == 0:
            ans = NO
            break
        d_count[t] -= 1
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    D = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    M = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, D, M, T)
    return

main()
