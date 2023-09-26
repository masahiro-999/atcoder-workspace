import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect_left, bisect_right
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


def solve(N: int, M: int, P: int, A: "List[int]", B: "List[int]"):
    B.sort()
    acc_b = [0]+list(accumulate(B))
    ans = 0
    for a in A:
        max_b = P-a
        # max_b 未満の個数
        idx = bisect_left(B, max_b)
        ans += a*idx + acc_b[idx] +P*(len(B)-idx)

    print(ans)



def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, P, A, B)
    return

main()