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


def solve(N: int, a: "List[int]"):
    def div(a,x):
        ret = []
        for i in range(N):
            c = 0
            while a[i] % x ==0:
                a[i] //= x
                c += 1
            ret.append(c)
        return ret

    b2 = div(a,2)
    b3 = div(a,3)

    if all([a[0]==a[i] for i in range(1,N)]):
        ans = sum(b2) -len(b2)*min(b2) + sum(b3) -len(b3)*min(b3)
    else:
        ans = -1
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)
    return

main()
