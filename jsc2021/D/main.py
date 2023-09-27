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

MOD = 1000000007

def solve1(N: int, P: int):
    def is_ok(p):
        for i in range(1,N+1):
            if sum(p[:i]) % P==0:
                return False
        return True

    ans = 0
    for p in product(range(1,P),repeat = N):
        if is_ok(p):
            ans += 1
    return ans

def solve(N: int, P: int):
    if N == 1:
        ans = P-1
    else:
        ans = (P-1)*pow((P-2),(N-1),MOD)
    return ans%MOD

def main():
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    print(solve(N, P))
    return

if __name__ == '__main__':
    main()
