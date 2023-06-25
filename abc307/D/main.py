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


def solve(N: int, S: str):
    stack = []
    a = []
    for s in S:
        if s == "(":
            stack.append(a)
            a = ["("]
        elif s == ")":
            if stack:
                a = stack.pop()
            else:
                a.append(s)
        else:
            a.append(s)
    ans = []
    for x in stack:
        ans += x
    ans += a
    ans = "".join(ans)
    print(ans)


def main():
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)
    return

main()
