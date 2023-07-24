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

def solve(N: int, A: int, B: int, C: int, D: int, S: str):
    def judgement_block(a_list):
        c_block = Counter()
        n = 1
        prev = a_list[0]
        for a in a_list[1:]+"X":
            if a != prev:
                if prev == "#":
                    c_block[n] += 1
                n = 1
            else:
                n += 1
            prev = a
        return max(list(c_block.keys())) == 1

    def judgement_space(l, r):
        if l == 0:
            l += 1
        if r == len(S)-1:
            r -= 1
        for i in range(l, r+1):
            if S[i-1] == "." \
                and S[i] == "." \
                and S[i+1] == ".":
                return True
        return False

    A -= 1
    B -= 1
    C -= 1
    D -= 1

    cond1 = judgement_block(S[B:D+1]) and judgement_block(S[A:C+1])
    cond2 = D > C or judgement_space(B, D)
    if cond1 and cond2:
        print(YES)
    else:
        print(NO)


def main():
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, A, B, C, D, S)
    return

main()
