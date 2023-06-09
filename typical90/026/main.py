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

    def dfs(p, cur):
        nonlocal color, ans1, ans2
        color[p] = cur
        if cur == 0:
            ans1.append(p+1)
        else:
            ans2.append(p+1)
        for next in g[p]:
            if color[next] == -1:
                dfs(next, 1-cur)

    ans1 = []
    ans2 = []
    color = [-1]*N
    g = defaultdict(list)
    for a,b in zip(A,B):
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    dfs(A[0]-1, 0)        
    ans  = ans1 if len(ans1)> len(ans2) else ans2
    print(*ans[:N//2])

def main():
    N = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)
    return

main()
