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


def solve(N: int, M: int, A: "List[int]", B: "List[int]", X: "List[int]", Y: "List[int]"):
    def dfs(s,x,y):
        nonlocal result, result_ok
        for t in g[s]:
            if result[t[0]] == [None,None]:
                result[t[0]] = [x+t[1],y+t[2]]
                dfs(t[0],x+t[1],y+t[2])
            else:
                if result[t[0]] != [x+t[1],y+t[2]]:
                    result_ok[t[0]] = False

    result = [[None,None] for _ in range(N)]
    result[0] = [0,0]

    result_ok = [True]*N
    g = defaultdict(list)
    for i in range(M):
        g[A[i]-1].append((B[i]-1,X[i],Y[i]))
        g[B[i]-1].append((A[i]-1,-X[i],-Y[i]))

    dfs(0,0,0)
    for i in range(N):
        if result_ok == False or result[i] == [None,None]:
            print("undecidable")
        else:
            print(*result[i])


def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, A, B, X, Y)
    return

main()
