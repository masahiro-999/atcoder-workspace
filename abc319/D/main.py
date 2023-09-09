import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect_right
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


def solve(N,M,l):
    def check2(l,w):
        sum_l = 0
        m = 0
        for a in l:
            if sum_l + a > w:
                sum_l = a
                m += 1
            else:
                sum_l += a
        if sum_l > 0:
            m += 1
        return m

    def check(l, w):
        p = w
        M = 1
        while True:
            i = bisect_right(l, p)
            if i == len(l):
                break
            p = l[i-1] + w
            M += 1
        return M
        
    l2 = [x+1 for x in l]
    l2_acc = [0] + list(accumulate(l2))
    w_max = (l2_acc[-1])
    w_min = max(l)
    l = w_min
    r = w_max
    while r - l > 1:
        mid = (l+r)//2
        if check(l2_acc, mid) <= M:
            r = mid
        else:
            l = mid
    print(r-1)        


def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    l = li()
    solve(N,M,l)
    return

main()
