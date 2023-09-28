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


def solve(N: int):
    if N < 10:
        print(0)
        return
    
    def n(keta):
        if keta == 1:
            return 9
        else:
            return 9*10**(keta-1)

    str_n = str(N)
    half_keta = len(str_n)//2
    if len(str_n)%2 != 0:
        N = 10**(half_keta*2)-1
        str_n = str(N)

    ans = sum([n(x) for x in range(1,half_keta+1)])
    ans -= (10**half_keta-1)-int(str_n[:half_keta])
    if int(str_n[:half_keta]) > int(str_n[half_keta:]):
        ans -= 1 
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    solve(N)
    return

main()
