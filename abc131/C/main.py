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


def solve(A: int, B: int, C: int, D: int):
    b_c = B//C 
    b_d = B//D 
    b_cd = B//(C*D//gcd(C,D))

    a_c = (A-1)//C 
    a_d = (A-1)//D 
    a_cd = (A-1)//(C*D//gcd(C,D))

    ans = (B-A+1)- (b_c + b_d - b_cd - (a_c + a_d - a_cd))
    print(ans)

def main():
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)
    return

main()
