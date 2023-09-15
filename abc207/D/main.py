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

YES = "Yes"
NO = "No"

def solve(N,ab,cd):
    if N == 1:
        print(YES)
        return
    def create_set(ab,i0,i1,ab_x1,ab_y1):
        # ab[i0]を原点、ab[i1]を基本ベクトルとした座標系でのab[i]の座標の集合を返す
        ret = set()
        x0,y0 = ab[i0]
        x1,y1 = ab[i1][0]-x0,ab[i1][1]-y0
        if x1**2 + y1**2 != ab_x1**2 + ab_y1**2:
            return False
        x2,y2 = y1,-x1        
        for i in range(N):
            if i == i0 or i == i1:
                continue
            x,y = ab[i][0]-x0,ab[i][1]-y0
            ret.add((x*x1+y*y1,x*x2+y*y2))
        return ret
    
    def check(ab,cd):
        # ab[0]を原点、ab[1]を基本ベクトルとした座標系でのab[i]の座標の集合を返す
        x0,y0 = ab[0]
        x1,y1 = ab[1][0]-x0,ab[1][1]-y0
        s_ab = create_set(ab,0,1,x1,y1)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                s_cd = create_set(cd,i,j,x1,y1)
                if s_ab == s_cd:
                    return True
        return False
    
    if check(ab,cd):
        print(YES)
    else:
        print(NO)
    
def main():
    N = int(next(tokens))  # type: int
    ab = [li() for _ in range(N)]  # type: "List[List[int]]"
    cd = [li() for _ in range(N)]  # type: "List[List[int]]"
    solve(N,ab,cd)
    return

main()
