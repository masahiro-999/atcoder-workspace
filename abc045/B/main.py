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


def solve(S_A: str, S_B: str, S_C: str):
    d = {}
    d["a"] = [x for x in S_A]
    d["b"] = [x for x in S_B]
    d["c"] = [x for x in S_C]
    turn = "a"
    while True:
        if not d[turn]:
            ans = turn
            break
        turn = d[turn].pop(0)
    print(ans.upper())

def main():
    S_A = next(tokens)  # type: str
    S_B = next(tokens)  # type: str
    S_C = next(tokens)  # type: str
    solve(S_A, S_B, S_C)
    return

main()
