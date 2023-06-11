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


def solve(p_str: str, q_str: str):
    a = [0,3,1,4,1,5,9]
    b = [sum(a[:i+1]) for i in range(len(a))]
    p = ord(p_str)-65
    q = ord(q_str)-65
    ans = abs(b[q] - b[p])
    print(ans)

def main():
    p = next(tokens)  # type: str
    q = next(tokens)  # type: str
    solve(p, q)
    return

main()
