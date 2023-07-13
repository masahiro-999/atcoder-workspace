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

def solve(N: int, M: int, s_list: "List[int]", c_list: "List[int]"):
    no_head_value = True 
    for s,c in zip(s_list,c_list):
        if N != 1 and s == 1 and c == 0:
            return -1
        if N != 1 and s == 1 and c != 0:
            no_head_value = False

    if N != 1 and no_head_value:
        s_list.append(1)
        c_list.append(1)

    d = [0] * N
    for s,c in zip(s_list,c_list):
        if not 0<= N-s < N:
            return -1 
        if d[N-s] == 0 or d[N-s] == c:
            d[N-s] = c
        else:
            return -1
    
    s = "".join([str(x) for x in d[::-1]])

    if len(f'{int(s)}') != N:
        return -1
    
    return int(s)


def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    s = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        s[i] = int(next(tokens))
        c[i] = int(next(tokens))
    print(solve(N, M, s, c))
    return

main()
