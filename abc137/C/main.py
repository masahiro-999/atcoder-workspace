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

def comb(n,m):
    ret = 1
    for i in range(m):
        ret *= n-i
    for i in range(m):
        ret //= i+1
    return ret

def solve(N: int, S: "List[str]"):
    a = []
    for s in S:
        a.append("".join(sorted([x for x in s])))
    c = Counter(a)
    ans = 0
    for n in c.values():
        ans += comb(n,2)
    print(ans)


def main():
    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, s)
    return

main()
