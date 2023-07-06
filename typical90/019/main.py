import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())

memo = {}
import json

c1 = 0
c2 = 0

def get_ans(a):
    global c1,c2
    c1 += 1
    a_key=json.dumps(a)
    r = memo.get(a_key,None)
    if r is None:
        c2 += 1
        if a ==[]:
            return 0
        result = []
        for i in range(len(a)-1):
            b = a[:i]+a[i+2:]
            d = abs(a[i]-a[i+1])
            result.append(get_ans(b)+d)
        r = min(result)
        memo[a_key] = r
    return r

def solve(N: int, A: "List[int]"):
    global c1,c2

    ans = get_ans(A[:])
    print(ans)
    print(c1,c2)
    print(len(memo))

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    solve(N, A)
    return

main()
