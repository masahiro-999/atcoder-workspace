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

@lru_cache()
def p(a,b,c):
    t = a+b+c
    if a==100 or  b==100 or c==100:
        return 0
    return a/t*(1+p(a+1,b,c)) + b/t*(1+p(a,b+1,c)) + c/t*(1+p(a,b,c+1))    



def solve(A: int, B: int, C: int):
    t = [[[0]*100 for _ in range(100)] for _ in range(100)]
    for a in range(99,-1,-1):
        for b in range(99,-1,-1):
            for c in range(99,-1,-1):
                total = a+b+c
                if total == 0:
                    continue
                if c == 99:
                    t[a][b][c] += c/total
                else:
                    t[a][b][c] += c/total*(1+t[a][b][c+1])
                if b == 99:
                    t[a][b][c] += b/total 
                else:
                    t[a][b][c] += b/total*(1+t[a][b+1][c])
                if a == 99:
                    t[a][b][c] += a/total 
                else:
                    t[a][b][c] += a/total*(1+t[a+1][b][c])


    ans = t[A][B][C]
    print(ans)


def main():
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)
    return

main()
