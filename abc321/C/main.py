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

def solve(K: int):
    nums_321 = []
    for i in range(2,1024):
        nums = [j for j in range(10) if i & 1<<j]
        nums.sort()
    
        a = 0
        for x in nums[::-1]:
            a = a*10+x
        nums_321.append(a)
    nums_321.sort()

    ans = nums_321[K-1]
    print(ans)


def main():
    K = int(next(tokens))  # type: int
    solve(K)
    return

main()
