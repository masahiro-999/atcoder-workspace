import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate, permutations
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


def solve(M: int, S: "List[str]"):
    def calc_min_time(t, open_order, target):
        lcm = t*M//gcd(t,M)
        open_i = 0
        for x in range(0,lcm*3,t):
            if S[open_order[open_i]][x%M] == str(target):
                open_i += 1
                if open_i == 3:
                    return x
        return inf

    ans = inf
    for t in range(1, M + 1):
        for open_order in permutations(range(3)):
            for target in range(10):
                ans = min(ans, calc_min_time(t, open_order, target))
    if ans == inf:
        ans = -1
    print(ans)

    
def main():
    M = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(3)]  # type: "List[str]"
    solve(M, S)
    return

main()
