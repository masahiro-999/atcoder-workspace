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


def solve(N, S, Q, q):
    s = [x for x in S]
    word_kind = 0
    history = []
    for t,x,c in q:
        if t ==1:
            s[x-1] = c
            if word_kind  != (2 if c < "a" else 1):
                history.append(((x-1),c))
        elif t == 2:
            word_kind = 1
            history = []
        else:
            word_kind = 2
            history = []

    if word_kind != 0:
        for i in range(N):
            if word_kind == 1:
                s[i] = s[i].lower()
            if word_kind == 2:
                s[i] = s[i].upper()

    for i, c in history:
        s[i] = c

    str = "".join(s)

    print(str)

def main():
    def getq():
        a = input().split()
        a[0] = int(a[0])
        a[1] = int(a[1])
        return a
    N = int(next(tokens))  # type: int
    S = input()
    Q = int(next(tokens))
    q = [getq() for _ in range(Q)]
    solve(N, S, Q, q)
    return

main()
