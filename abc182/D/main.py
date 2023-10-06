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


def solve(N,A):
    acc_a = accumulate(A)
    max_a = [0]*N
    p = 0
    mx = 0
    for i,a in enumerate(A):
        p += a
        mx = max(mx,p)
        max_a[i] = mx        
 
    ans = 0
    p = 0
    for i,a in enumerate(acc_a):
        ans = max(ans,p+max_a[i])
        p+=a
    print(ans)

def main():
    N = int(next(tokens))
    A = li()
    solve(N,A)
    return

main()
