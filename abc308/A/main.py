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

def solve(S: "List[int]"):
    def check1():
        prev = S[0]
        for s in S[1:]:
            if prev > s:
                return False
            prev = s
        return True
    
    def check2():
        for s in S:
            if not 100<= s <=675:
                return False
            if s % 25 != 0:
                return False
        return True

    if check1 () and check2():
        print(YES)
    else:
        print(NO)


def main():
    S = [int(next(tokens)) for _ in range(8)]  # type: "List[int]"
    solve(S)
    return

main()
