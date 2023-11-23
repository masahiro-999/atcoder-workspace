import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect_left
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


def solve(Q,q_list):
    def get_ans(acc_c):
        i = bisect_left(acc_n_list, acc_c)
        # d = acc_n_list[i] - acc_c
        return nx_list[i-1] + (acc_c-acc_n_list[i-1])*x_list[i]

    acc_n_list = [0]
    x_list = [0]
    nx_list = [0]

    acc_n = 0
    acc_nx = 0
    acc_c = 0
    prev_ans = 0
    for q in q_list:
        if q[0] == 1:
            [x,c] = q[1:]
            acc_n = acc_n + c
            acc_nx = acc_nx + x*c            
            acc_n_list.append(acc_n)
            x_list.append(x)
            nx_list.append(acc_nx)
        else:
            c = q[1]
            acc_c += c
            ans = get_ans(acc_c)
            print(ans - prev_ans)
            prev_ans = ans


def main():
    Q = int(next(tokens))  # type: int
    q_list = [li() for _ in range(Q)]
    solve(Q,q_list)
    return

main()
