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

def solve(S: "List[str]", T: "List[str]"):
    n = 0
    for s,t in zip(S,T):
        if s != t:
            n+=1
    if n == 0:
        print(YES)
    elif n %2 == 0:
        print(NO)
    else:
        print(YES)


def main():
    S = [next(tokens) for _ in range(3)]  # type: "List[str]"
    T = [next(tokens) for _ in range(3)]  # type: "List[str]"
    solve(S, T)
    return

main()
