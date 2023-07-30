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


def solve(N: int, K: int, R: int, S: int, P: int, T: str):
    t = {"r":("p",P), "s":("r", R), "p":("s", S)}
    ans = 0
    history = []
    for i in range(N):
        if i < K or history[i-K] != t[T[i]][0]:
            ans += t[T[i]][1]
            history.append(t[T[i]][0])
        else:
            history.append("x")

    print(ans)

def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    T = next(tokens)  # type: str
    solve(N, K, R, S, P, T)
    return

main()
