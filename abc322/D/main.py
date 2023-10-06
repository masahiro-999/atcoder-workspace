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

def create_set(p):
    ret = set()
    for i in range(4):
        for j in range(4):
            if p[i][j] == "#":
                ret.add((i,j))
    return ret
def rot(x,y,r):
    if r == 0:
        return (x,y)
    elif r == 1:
        return (y,3-x)
    elif r == 2:
        return (3-x,3-y)
    else:
        return (3-y, x)

def moved_ply(pol):
    ret = []
    for i in range(-4,5):
        for j in range(-4,5):
            for r in range(4):
                p = []
                for x,y in pol:
                    pos = rot(x+i,y+j,r)
                    if not (0<=pos[0]<4 and 0<=pos[1]<4):
                        break
                    p.append(rot(x+i,y+j,r))
                else:
                    ret.append(set(p))
    return ret

def solve(p):

    polyomino = [create_set(x) for x in p]
    if 16 != sum([len(x) for x in polyomino]):
        ans = NO
    else:  
        ans = NO
        all_filled = set([(x,y) for x,y in product(range(4),range(4))])
        x = [moved_ply(x) for x in polyomino]
        for try_pol in product(*x):
            marged = reduce(lambda x,y:x|y, try_pol)
            if marged == all_filled:
                ans = YES
                break
    print(ans)

def main():
    p =[[input() for _ in range(4)] for _ in range(3)]
    solve(p)
    return

if __name__ == '__main__':
    main()
