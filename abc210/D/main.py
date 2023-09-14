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


def solve(H: int, W: int, C: int, A: "List[List[int]]"):
    d = [[inf]*W for _ in range(H)]
    ans = inf
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                d[i][j] = A[i][j]
            elif i == 0:
                ans = min(ans, A[i][j]+d[i][j-1]+C)
                d[i][j] = min(d[i][j-1]+C, A[i][j])
            elif j == 0:
                ans = min(ans, A[i][j]+d[i-1][j]+C)
                d[i][j] = min(d[i-1][j]+C, A[i][j])
            else:
                ans = min(ans, A[i][j]+d[i-1][j]+C, A[i][j]+d[i][j-1]+C)
                d[i][j] = min(d[i-1][j]+C, d[i][j-1]+C, A[i][j])
             
    return ans

def main():
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    ans1 = solve(H, W, C, A)
    ans2 = solve(H, W, C, list(reversed(A)))
    print(min(ans1, ans2))
    return

if __name__ == '__main__':
    main()
