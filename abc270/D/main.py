import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect_right
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


def solve(N: int, K: int, A: "List[int]"):
    d = [[0,inf] for _ in range(N+1)]

    d[0][0] = 0
    d[0][1] = 0

    for i in range(1,N+1):
        for j in range(2):
            for k in range(K):
                a = A[k]
                if i-a >=0:
                    if j % 2 == 0:
                        d[i][0] = max(d[i-a][1]+a, d[i][0])
                    else:
                        d[i][1] = min(d[i-a][0], d[i][1])
    ans = d[N][0]
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, K, A)
    return

main()
