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
    a = {
        "tourist": 3858,
        "ksun48": 3679,
        "Benq": 3658,
        "Um_nik": 3648,
        "apiad": 3638,
        "Stonefeang": 3630,
        "ecnerwala": 3613,
        "mnbvmar": 3555,
        "newbiedmy": 3516,
        "semiexp": 3481,
    }

    print(a[S])
    
def main():
    S = next(tokens)  # type: str
    solve(S)
    return

main()
