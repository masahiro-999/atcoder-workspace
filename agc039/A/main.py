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


def solve(S: str, K: int):

    def first_diff(S):
        l = len(S)
        for i in range(l):
            if S[i] != S[(i+1)%l]:
                return (i+1)%l
        return -1

    fd = first_diff(S)
    if fd == -1:
        return len(S)*K //2

    S1 = S[fd:]+S[:fd]
    c = 1
    c_sum = 0
    c_last = 0
    l = len(S)
    for i in range(l):
        if S1[i] != S1[(i+1)%l]:
            c_sum += c // 2
            c_last = c // 2
            c = 1
        else:
            c += 1
    if c > 2:
        c_sum += c // 2
        c_last = c // 2
    ans = c_sum*K
    if S[0] == S[-1]:
        ans -= c_last
        c1 = first_diff(S)
        c2 = first_diff(S[::-1])
        ans += c1 // 2 + c2 // 2
    return(ans)

def main():
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    print(solve(S, K))
    return

main()
