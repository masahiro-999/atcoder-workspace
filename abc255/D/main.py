import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect,bisect_left,bisect_right
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


def solve(N: int, Q: int, A: "List[int]", X: "List[int]"):
    A.sort()
    A_acc = [0] + list(accumulate(A))

    for x in X:
        i_le = bisect_left(A,x)
        i_gt = bisect_right(A,x)
        sum_le = A_acc[i_le]
        sum_gt = A_acc[N] - A_acc[i_gt]
        ans = x*i_le - sum_le + sum_gt - x*(N-i_gt)
        print(ans)

def main():
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    X = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, A, X)
    return

main()
