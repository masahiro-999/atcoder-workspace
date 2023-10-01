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

def int_base(s, base):
    x = 0
    for c in s:
        x = x * base + int(c)
    return x

def solve(X: str, M: int):
    k = len(X)
    c = Counter([int(x) for x in X])
    d = max(c.keys())
    if not int_base(X,d+1) <= M:
        print(0)
        return    
    if k == 1:
        print(1)
        return
    l = d+1
    r = M+1
    while r - l >1:
        mid = (l+r)//2
        if int_base(X,mid) <=M:
            l = mid
        else:
            r = mid
    ans = l -d
    print(ans)

def main():
    X = next(tokens)  # type: str
    M = int(next(tokens))  # type: int
    solve(X, M)
    return

main()
