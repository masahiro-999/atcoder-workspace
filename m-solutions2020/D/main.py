import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate,permutations,combinations
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


def solve(N: int, A: "List[int]"):
    d_list = []
    is_going_up = A[0] < A[1]
    bottom = -1
    if is_going_up:
        bottom = A[0]
    for i in range(1,N):
        if is_going_up and (i==N-1 or A[i] > A[i+1]):
            d_list.append((bottom, A[i]))
            is_going_up = False
        if not is_going_up and (i==N-1 or A[i] < A[i+1]):
            bottom = A[i]
            is_going_up = True

    x = 1000
    for bottom, top in d_list:
        x += (x//bottom)*(top-bottom)
    print(x)

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)
    return

if __name__ == '__main__':
    main()
