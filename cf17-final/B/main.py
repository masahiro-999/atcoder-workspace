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

def solve(S: str):
    c = Counter(S)
    n = [v for i,v in c.items()]
    n.sort()
    if len(n) == 1:
        if n[0] > 1:
            ans = NO
        else:
            ans = YES
    elif len(n) == 2:
        if n[-1] == 1:
            ans = YES
        else:
            ans = NO
    else:
        b = n[2] - n[0]
        if b > 1:
            ans = NO
        else:
            ans = YES
    print(ans)

def main():
    S = next(tokens)  # type: str
    solve(S)
    return

main()
