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

def solve(s: str, t: str):
    s_list = [x for x in s]
    t_list = [x for x in t]
    s_list.sort()
    t_list.sort(reverse=True)
    if "".join(s_list) < "".join(t_list):
        print(YES)
    else:
        print(NO)

def main():
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)
    return

main()
