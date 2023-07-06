import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect, bisect_left
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


def solve(N: int, X: "List[int]", Y: "List[int]"):
    def degree(i,j):
        return atan2((Y[i]-Y[j]), (X[i]-X[j]))*180/pi

    def sub(a,b):
        x = abs(a-b)
        if x > 180:
            x = 360-x
        return x

    def find_max(d):
        max_x = 0
        for a in d:
            target = a + 180
            if target <= d[0] or target >= d[-1]:
                x = max(sub(d[0], a), sub(d[-1], a))
            else:
                i = bisect_left(d,target)
                x = max(sub(d[i], a), sub(d[i-1], a))
            max_x = max(max_x, x)
        return max_x

    d = []
    ans = 0
    for i in range(N):
        d = [degree(i,j) for j in range(N) if j!=i]
        d.sort()
        ans = max(ans,find_max(d))
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, X, Y)
    return

main()
