import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())


def solve(N: int, K: int, S: str):
    d = [[inf]*26 for _ in range(N)]
    for i in range(N-1, -1 , -1):
        if i !=N-1:
            d[i] = d[i+1][:]
        c =ord(S[i])-ord("a")
        d[i][c] = i

    def find_min(i,j):
        for c in range(26):
            if d[i][c] <=j:
                return (d[i][c],c)

    sp = 0
    ans = ""
    while len(ans) < K:
        ep = N-K+len(ans)
        (p, c) = find_min(sp, ep)
        ans += chr(c+ord("a"))
        sp = p+1
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)
    return

main()
