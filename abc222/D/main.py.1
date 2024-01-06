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


MOD = 998244353


def solve(N: int, a_list: "List[int]", b_list: "List[int]"):
    ans = 1
    a1 = a_list[0]
    b1 = b_list[0]
    dp = [1]*(b1-a1+1)
    for i in range(1,N):
        dp_acc = list(accumulate(dp))
        a1 = a_list[i-1]
        a2 = a_list[i]
        b1 = b_list[i-1]
        b2 = b_list[i]
        dp_next = [0]*(b2-a2+1)
        for i in range(a2,b2+1):
            dp_next[i-a2] = dp_acc[min(b1-a1,i-a1)] % MOD
        ans %= MOD
        dp = dp_next
    ans = sum(dp)%MOD
    print(ans)
    return

def main():
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a, b)
    return

main()
