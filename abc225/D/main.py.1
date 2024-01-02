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

def solve(N, Q, q_list):
    forward = defaultdict(lambda: -1)
    backward = defaultdict(lambda: -1)
    for q in q_list:
        if q[0] == 1:
            _, a, b = q
            forward[a] = b
            backward[b] = a
        elif q[0] == 2:
            _, a, b = q
            del forward[a]
            del backward[b]
        else:
            _, a = q
            before_a = []
            p = a
            while p != -1:
                p = backward[p]
                if p != -1:
                    before_a.append(p)
            after_a = []
            p = a
            while p != -1:
                p = forward[p]
                if p != -1:
                    after_a.append(p)
            ans = list(reversed(before_a)) + [a] + after_a
            print(len(ans), *ans)

def main():
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    q_list = [li() for _ in range(Q)]
    solve(N, Q, q_list)
    return

main()
