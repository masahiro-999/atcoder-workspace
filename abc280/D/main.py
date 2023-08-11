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


def solve(K: int):
    def count_n(c,v):
        ret = 0
        while c % v ==0:
            c //= v
            ret += 1
        return ret
    
    def get_n(v,i):
        c = 0
        while i > 0:
            c += 1
            i -= 1
            i -= count_n(c,v)
        return v*c

    n = int(sqrt(K))
    c = Counter()
    x = K
    for i in range(2,n+1):
        while x % i == 0: 
            x //= i
            c[i] += 1
    if  x > 1:
        c[x] += 1
    a = [get_n(value, count) for value,count in c.items()]
    ans = max(a)
    print(ans)

def main():
    K = int(next(tokens))  # type: int
    solve(K)
    return

main()
