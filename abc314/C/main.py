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


def solve(N: int, M: int, S: str, C: "List[int]"):
    mt = [[] for _ in range(M)]
    mt2 = [{} for _ in range(M)]
    for i,value in enumerate(C):
        mt[value-1].append(i)
    for i in range(M):
        mt[i] = mt[i][::-1]
        top = mt[i][0]
        prev = mt[i][0]
        for j in mt[i][1:]:
            mt2[i][prev] = j
            prev = j
        mt2[i][prev] = top
    ans = []
    for i in range(N):
        color = C[i]
        next = mt2[color-1][i]
        ans.append(S[next])
    print("".join(ans))
    
def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, S, C)
    return

main()
