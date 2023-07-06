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


def solve(T: int, L: int, X: int, Y: int, Q: int, E: "List[int]"):
    def pos_e(t):
        s = 2/T*t*pi
        z = -cos(s)*(L/2)+L/2
        y = -sin(s)*(L/2)
        return(y,z)

    def ans(y,z):
        return atan2(z,sqrt((Y-y)**2+X**2))/pi*180

    for e in E:
        y,z = pos_e(e)
        s = ans(y,z)
        print(s)
        
def main():
    T = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    E = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(T, L, X, Y, Q, E)
    return

main()
