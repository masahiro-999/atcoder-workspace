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

def count(a,target):
    def rewrite():
        c = 0
        for i in range(1,len(a)):
            if a[i] == target:
                a[i-1] = target
            if a[i-1] == target:
                c += 1

        a.pop(-1)
        return c == len(a)

    ret = 0
    while True:
        ret += 1
        if rewrite():
            break
    return ret

def solve(s: str):
    if all([s[0]==i for i in s]):
        return 0
    a = [x for x in s]
    ans = inf
    for i in [chr(97+i) for i in range(26)]:
        if i in s:
            ans = min(ans, count(a[:],i))
    return ans

def main():
    s = next(tokens)  # type: str
    print(solve(s))
    return

main()
