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


def solve(S: str):
    dir_left = True 
    q = deque()
    for s in S:
        if s == "R":
            dir_left = not dir_left
        else:
            if dir_left:
                if q and q[-1] == s:
                    q.pop()
                else:
                    q.append(s)
            else:
                if q and q[0] == s:
                    q.popleft()
                else:
                    q.appendleft(s)
    if not dir_left:
        q.reverse()
    print("".join(q))
    return


def main():
    S = next(tokens)  # type: str
    solve(S)
    return

main()
