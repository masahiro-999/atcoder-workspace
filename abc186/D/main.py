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


def solve(N: int, A: "List[int]"):
    A.sort()
    acc_head = [0]+list(accumulate(A))
    acc_tail = [0]+list(accumulate(A[::-1]))
    s = 0
    for i,a in enumerate(A):
        # iより前
        num_head = i
        num_tail = N-1-i
        s += a*num_head - acc_head[num_head]
        s += acc_tail[num_tail] - a*num_tail
    print(s//2)

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)
    return

main()
