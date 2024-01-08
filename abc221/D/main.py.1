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


def solve(N: int, A: "List[int]", B: "List[int]"):
    d = defaultdict(int)
    ans_count = Counter()
    for a, b in zip(A, B):
        d[a] += 1
        d[a + b] -= 1
    d_key = sorted(d.keys())
    n  = 0
    for i in range(len(d_key) - 1):
        n += d[d_key[i]]
        ans_count[n] += d_key[i + 1] - d_key[i]
    ans = [ans_count[i] for i in range(1, N + 1)]
    print(*ans)                 

def main():
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)
    return

main()
