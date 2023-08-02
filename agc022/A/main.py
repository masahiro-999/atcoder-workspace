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


def solve(S: str):
    l = len(S)
    if S=="zyxwvutsrqponmlkjihgfedcba":
        return -1
    unused = ""
    for i in range(26):
        c = chr(i+97)
        if c not in S:
            unused = c
            break
    if unused:
        return(S+c)
    else:
        pop_list = []
        while S:
            a = S[-1]
            S = S[:-1]
            pop_list.append(a)
            pop_list.sort()
            b = [x for x in pop_list if x > S[-1]]
            if b:
                return S[:-1]+b[0]
        return -1    

# abcdefghijklmnopqrstuvwzyx

def main():
    S = next(tokens)  # type: str
    print(solve(S))
    return

main()
