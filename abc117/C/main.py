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


def solve(N: int, M: int, X: "List[int]"):
    if N >= M:
        return 0
    else:
        X.sort()
        d = [(i,X[i+1] - X[i]) for i in range(M-1)]
        d.sort(key=lambda x: x[1],reverse=True)
        d2 = d[:N-1]
        d2.sort(key=lambda x: x[0])

        split_pos = [-1] + [i for i,_ in d2] + [M-1]

        ans = 0
        for i in range(len(split_pos)-1):
            ans += X[split_pos[i+1]] - X[split_pos[i]+1]
        return ans

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    print(solve(N, M, X))
    return

main()
