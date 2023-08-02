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

def solve(N: int, a: "List[int]"):
    c = Counter(a)
    if c[0]==N:
        return YES
    if N % 3 != 0:
        return NO
    v = list(c.values())
    k = list(c.keys())
    if len(v) == 3 and sum(v) == N and v[0]==v[1] and v[1]==v[2]:
        if k[0]^k[1]==k[2]:
            return YES
    if len(v) == 2 and c[0] == N//3:
            return YES
    return NO

def main():
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, a))
    return

main()
