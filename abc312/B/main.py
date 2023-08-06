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

def solve(N: int, M: int, S: "List[str]"):

    def is_black33(i1,j1):
        for i in range(3):
            for j in range(3):
                if S[i+i1][j+j1] == ".":
                    return False
        return True

    def is_whiteV(i1,j1):
        for i in range(4):
            if S[i+i1][j1] == "#":
                    return False
        return True

    def is_whiteH(i1,j1):
        for j in range(4):
            if S[i1][j+j1] == "#":
                    return False
        return True

    def match_tak_code(i1,j1):
        return is_black33(i1,j1) and is_whiteH(i1+3,j1) and is_whiteV(i1,j1+3) and \
           is_black33(i1+6,j1+6) and is_whiteH(i1+5,j1+5) and is_whiteV(i1+5,j1+5)

    for i in  range(N-9+1):
        for j in  range(M-9+1):
             if match_tak_code(i,j):
                  print(i+1, j+1)
        
                       


def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, M, S)
    return

main()
