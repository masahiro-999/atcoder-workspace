import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate,permutations,combinations
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

def f(cx,cy,r,x,y):
    cx = round(cx * 10000)
    cy = round(cy * 10000)
    r *= 10000
    x *= 10000
    y *= 10000
    if r*r >= (x-cx)**2+(y-cy)**2:
        return 1
    return 0

def count_dot_widin_r_at_x(cx,cy,R,x):
    up_y = find_y(cx,cy,R,x,1,int(R+1)+1)
    down_y = find_y(cx,cy,R,x,-1,int(-R-1)-1)
    return up_y - down_y + f(cx,cy,R,x,0)

def find_y(cx,cy,R,x,start_l,start_r):
    l = start_l
    r = start_r
    if not f(cx,cy,R,x,l):
        return 0
    while abs(r-l) > 1:
        mid = (r+l)//2
        if f(cx,cy,R,x,mid):
            l = mid
        else:
            r = mid
    return l

def solve(X: float, Y: float, R: float):
    X = X % 1
    Y = Y % 1
    if X > 0.5:
        X -= 1
    if Y > 0.5:
        Y -= 1
    mix_x = int(-R+X)
    max_x = int(R+X)
    ans = 0
    for x in range(mix_x,max_x+1):
        ans += count_dot_widin_r_at_x(X,Y,R,x)
    print(ans)
def main():
    X = float(next(tokens))  # type: float
    Y = float(next(tokens))  # type: float
    R = float(next(tokens))  # type: float
    solve(X, Y, R)
    return

if __name__ == '__main__':
    main()
