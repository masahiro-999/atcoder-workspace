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

YES = "Yes"
NO = "No"

def solve(N: int):
    n_str = str(N)
    ans = YES
    if len(n_str) == 1:
        ans = YES
    else:
        for i in range(1, len(n_str)):
            if n_str[i-1] <= n_str[i]:
                ans = NO
                break   
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    solve(N)
    return

main()
