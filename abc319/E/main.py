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



def solve(N: int, X: int, Y: int, P: "List[int]", T: "List[int]", Q: int, q_list: "List[int]"):
    base_time = sum(P) + sum(T) + X + Y
    T_shift = [X] + T[:-1]
    t_mod_p = sum([t % p for t, p in zip(T_shift, P)])
    def x_mod_p(x):
        ret = x
        for p in P:
            ret %= p
        return ret
    x_mod_p_table = [x_mod_p(x) for x in range(P[0])]
    def calc_time(x):
        return base_time + t_mod_p - x_mod_p_table[x%P[0]]

    for q in q_list:
        print(calc_time(q))

def main():
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    P = [int()] * (N - 1)  # type: "List[int]"
    T = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        P[i] = int(next(tokens))
        T[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    q = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, X, Y, P, T, Q, q)
    return

main()
