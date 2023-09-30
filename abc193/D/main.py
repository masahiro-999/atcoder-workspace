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


def solve(K: int, S: str, T: str):
    s_count = Counter([int(x) for x in S[:4]])
    t_count = Counter([int(x) for x in T[:4]])
    st_count = Counter([int(x) for x in S[:4]+T[:4]])
    
    def f(count, i):
        count[i] += 1
        ret = 0
        for j in range(1,10):
            ret += j*10**count[j]
        count[i] -= 1
        return ret
    s_f = [f(s_count,i) for i in range(1,10)]
    t_f = [f(t_count,i) for i in range(1,10)]

    win_count = 0
    total_count = 0
    for i in range(1,10):
        case_i = K-st_count[i]
        for j in range(1,10):
            if i == j:
                case_j = K-st_count[j] -1
            else:
                case_j = K-st_count[j]
            if s_f[i-1] > t_f[j-1]:
                win_count += case_i * case_j
            total_count += case_i * case_j

    ans = win_count/total_count
    print(ans)

def main():
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(K, S, T)
    return

main()
