import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate,permutations
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


def solve(N: int, A: "List[List[int]]", M: int, X: "List[int]", Y: "List[int]"):
    def is_valid(l):
        for i in range(len(l)-1):
            p = l[i]
            q = l[i+1]
            try:
                if q in t[p]:
                    return False
            except KeyError:
                continue
        return True
    
    def calc_time(i_list):
        return sum(A[i][j] for i,j in zip(i_list,range(N)))

    t = defaultdict(list)
    for x,y in zip(X,Y):
        x -= 1
        y -= 1
        t[x].append(y)
        t[y].append(x)

    ans = inf
    for i_list in permutations(range(0,N), N):
        if is_valid(i_list):
            time = calc_time(i_list)
            ans = min(ans, time)
    if ans == inf:
        print(-1)
    else:
        print(ans)

def main():
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    M = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, A, M, X, Y)
    return

main()
