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

YES = "Yes"
NO = "No"

def solve(N: int, S: int, A: "List[int]", B: "List[int]"):

    d = [[False]*(S+1) for _ in range(N+1)]
    d[0][0] = True
    for i,(a,b) in enumerate(zip(A,B)):
        for j in range(S+1):
            if d[i][j]:
                if j+a <= S:
                    d[i+1][j+a] = True
                if j+b <= S:
                    d[i+1][j+b] = True

    if d[N][S]:
        ans = []
        s = S
        for i,(a,b) in reversed(list(enumerate(zip(A,B)))):
            if d[i][s-a]:
                ans.append("H")
                s -= a
            else:
                ans.append("T")
                s -= b
        ans = "".join(reversed(ans))
        print(YES)
        print(ans)
    else:
        print(NO)

def main():
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, S, a, b)
    return

main()
