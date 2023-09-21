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


def solve(N,S,Q,T):
    S = [c for c in S]
    flip = False
    for t,a,b in T:
        if t == 1:
            if flip:
                a = (a+N)%(2*N)
                b = (b+N)%(2*N)
            S[a-1],S[b-1] = S[b-1],S[a-1]
        else:
            flip = not flip
    if flip:
        S = S[N:]+S[:N]
    print(''.join(S))

def main():
    N = int(next(tokens))
    S = next(tokens)
    Q = int(next(tokens))
    T = [li() for _ in range(Q)]
    solve(N,S,Q,T)
    return

main()
