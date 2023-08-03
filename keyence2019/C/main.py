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
    a = [a-b for a,b in zip(A,B)]
    c = 0
    a_sum = 0
    for i in a:
        if i < 0:
            a_sum += -i
            c += 1
    a.sort(reverse=True)
    if a_sum == 0:
        return 0
    ans = -1
    for i in a:
        a_sum += -i
        c += 1
        if a_sum <= 0:
            ans = c
            break
        if i < 0:
            break
    return ans

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    print(solve(N, A, B))
    return

main()
