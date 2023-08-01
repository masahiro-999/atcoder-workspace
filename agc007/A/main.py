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

YES = "Possible"
NO = "Impossible"

def solve(H,W,d):
    def go_right(i,j):
        ret = j
        while j < W and d[i][j] == "#":
            ret = j
            j += 1
        return(ret)

    def is_all_zero(i,j1,j2):
        for j in range(j1,j2):
            if d[i][j] == "#":
                return False
        return True
    
    i = 0
    j = 0
    ans = YES
    for i in range(H):
        if not is_all_zero(i,0,j):
            ans = NO
            break
        j = go_right(i,j)
        if not is_all_zero(i,j+1,W):
            ans = NO
            break
    print(ans)

def main():
    H = int(next(tokens))
    W = int(next(tokens))
    d = [input() for _ in range(H)]
    solve(H,W,d)
    return

main()
