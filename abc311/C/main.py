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
    def check(s):
        nonlocal visited
        while True:
            if s in visited:
                return s
            else:
                visited.add(s)
                s = d[s]

    visited = set()

    d = {}
    for i in range(1,N+1):
        d[i] = A[i-1]

    s = check(i)
    s1 = s
    ans = []
    while True:
        ans.append(s)
        s = d[s]
        if s == s1:
            break
    print(len(ans))
    print(*ans)



def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)
    return

main()
