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

YES = "Yes"
NO = "No"

def solve(c: "List[List[int]]"):
    total = sum([sum(x) for x in c])

    if total /3 == sum([c[i][i] for i in range(3)]):
        return True
    else:
        return False
        

    a1 = sum_h(c,0) + sum_v(c,0) - sum_ab
def main():
    c = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    if solve(c):
        print(YES)
    else:
        print(NO)
    return

main()
