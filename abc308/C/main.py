import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache,cmp_to_key 
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

def cmp(x,y):
    xi,xa,xb = x
    yi,ya,yb = y
    d = (ya+yb)*xa - (xa+xb)*ya
    if d == 0:
        return xi-yi
    else:
        return -d 

def solve(N: int, A: "List[int]", B: "List[int]"):
    r = [(i,a,b) for i,a,b in zip(range(N),A,B)]
    # print(r)
    r1 = sorted(r, key=cmp_to_key(cmp))
    ans = [i+1 for (i,_,_) in r1]
    print(*ans)

def main():
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)
    return

main()
