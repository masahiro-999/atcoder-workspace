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


def solve(N: int, A: "List[int]", B: "List[int]"):
    def dfs(n,d,prev):
        if g[n]:
            ret = []
            for n_next in g[n]:
                if n_next == prev:
                    continue
                ret.append(dfs(n_next, d+1,n))
            if not ret:
                return (n,d)
            ret.sort(key = lambda a:a[1])
            return ret[-1]
        else:
            return (n,d)

    g = defaultdict(list)
    for a,b in zip(A,B):
        g[a].append(b)
        g[b].append(a)
    
    s = A[0]
    (n1,_) = dfs(s, 0, None)
    (n2,d) = dfs(n1, 0, None)
    print(d+1)

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
