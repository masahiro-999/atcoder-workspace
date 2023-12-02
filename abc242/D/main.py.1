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


def solve(S,Q,tk):
    s = [ord(s) - ord("A") for s in S]

    for [t,k] in tk:
        k -= 1
        if t == 0:
            base = k
            shift = 0
        else:
            bin_k = format(k,"b")
            num_one = len([x for x in bin_k[-t:] if x == "1"])
            num_zero = t - num_one
            shift = num_zero - num_one
            if bin_k[:-t] == "":
                base = 0
            else:
                base = int(bin_k[:-t],2)
        base_word = s[base]
        ans = (base_word + shift) % 3
        print(chr(ans + ord("A")))

def main():
    S = input()
    Q = int(next(tokens))  # type: int
    tk = [li() for _ in range(Q)]

    solve(S,Q,tk)
    return

main()
