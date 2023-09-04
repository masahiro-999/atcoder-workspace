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


def solve(N: int, x: "List[int]", y: "List[int]"):
    ans_set = set()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            xi,yi = x[i],y[i]
            xj,yj = x[j],y[j]
            dx,dy = xj-xi,yj-yi
            gcd_xy = gcd(dx,dy)
            if gcd_xy == 0:
                # 何方も0の場合はない
                if dx == 0:
                    dx, dy = 0, 1
                else:
                    dx, dy = 1, 0
            else:
                dx,dy = dx//gcd_xy,dy//gcd_xy
            ans_set.add((dx,dy))
            ans_set.add((-dx,-dy))

    ans = len(ans_set)
    # print(ans_set)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)
    return

main()
