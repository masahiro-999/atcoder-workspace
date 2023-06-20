import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())


def solve(N: int, A: "List[int]"):
    c = [0]*N
    ans = []
    for i in range(3*N):
        a = A[i]-1
        c[a] += 1
        if c[a] == 2:
            ans.append((a,i))

    ans.sort(key=lambda x:x[1])
    print(*[x+1 for (x,_) in ans])

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(3 * N)]  # type: "List[int]"
    solve(N, A)
    return

main()
