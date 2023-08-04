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

def solve(N,M,s,p):
    def is_on(s_bin, s_list, p):
        c = 0
        for s in s_list:
            if s_bin & (1<<(s-1)) !=0:
                c+= 1
        return c %2 == p
    
    ans = 0
    for s_bin in range(0,1<<N):
        ok = True
        for i in range(M):
            if not is_on(s_bin, s[i], p[i]):
                ok = False
                break
        if ok:
            ans += 1
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    s =[]
    for i in range(M):
        ss = li()
        s.append(ss[1:])
    p = li()
    solve(N,M,s,p)
    return

main()
