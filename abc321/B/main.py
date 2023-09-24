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


def solve(N: int, X: int, A: "List[int]"):
    A.sort()
    # 0でもOKの場合
    if sum(A[0:-1])>=X:
        ans = 0
    elif sum(A[1:])<X:
        ans = -1
    else:
        ans = X-sum(A[1:-1])
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    solve(N, X, A)
    return

main()
