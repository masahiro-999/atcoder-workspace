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


def solve(N: int, X: int, S: str):

    bits = [0]*10000000
    bin_X = format(X,"b")
    for i,b in enumerate(bin_X):
        bits[i] = int(b)

    base = len(bin_X) -1
    for s in S:
        if s =="U":
            base -= 1
        else:
            base += 1
            if s == "R":
                bits[base] = 1
            else:
                bits[base] = 0

    bin_ans = "".join(map(str, bits[:base+1]))
    ans = int(bin_ans,2)

    print(ans)

def main():
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    S = input()  # type: str
    solve(N, X, S)
    return

main()
