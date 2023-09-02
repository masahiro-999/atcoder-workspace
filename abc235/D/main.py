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


def solve(a: int, N: int):
    max_n = 10**len(str(N))
    visited = [-1]*(max_n+1)
    visited[1] = 0
    q = deque([1])
    while q:
        i = q.popleft()
        if i*a <= max_n:
            if visited[i*a] == -1:
                visited[i*a] = visited[i]+1
                q.append(i*a)
        str_i = str(i)
        if len(str_i)>1 and str_i[-1] != "0":
            str_i = str_i[-1]+str_i[:-1]
            if int(str_i) <= max_n:
                if visited[int(str_i)] ==-1:
                    visited[int(str_i)] = visited[i]+1
                    q.append(int(str_i))
        
    ans = visited[N]
    if ans == inf:
        ans = -1

    print(ans)

def main():
    a = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(a, N)
    return

main()
