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


def solve(A: int, B: int, X: int):

    if A+B > X:
        return 0
    
    k = 1
    while True:
        if 10**(k-1)*A+k*B <= X:
            k += 1
        else:
            k -= 1
            break
    X -= B*k
    max_x = X//A
    x = min([10**k-1,max_x, 1000000000])
    return (x)

def main():
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    print(solve(A, B, X))
    return

main()
