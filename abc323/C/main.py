import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate,permutations,combinations
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


def solve(N: int, M: int, A: "List[int]", S: "List[str]"):
    def total(i):
        s = 0
        for i,x in enumerate(S[i]):
            if x =="o":
                s += A[i]
        return s
    
    total_table = [total(i)+(i+1) for i in range(N)]
    mx = max(total_table)
    for i in range(N):
        d = mx - total_table[i]
        if d > 0:
            x = [A[j] for j in range(M) if S[i][j] == "x"]
            x.sort(reverse=True)
            c = 0
            for x1 in x:
                if d < 0:
                    break
                d -= x1
                c += 1
            print(c)
        else:
            print(0)
def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, M, A, S)
    return

main()
