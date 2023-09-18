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

# @lru_cache(maxsize=None)
# def f(a,b):
#     elif a == 0:
#         return 1
#     elif b == 0:
#         return 1
#     else:
#         return f(a-1,b) + f(a,b-1) +1

def solve(A: int, B: int, K: int):
    f_table = [[0]*(B+1) for _ in range(A+1)]
    for i in range(A+1):
        for j in range(B+1):
            if i == 0:
                f_table[i][j] = 1
            elif j == 0:
                f_table[i][j] = 1
            else:
                f_table[i][j] = f_table[i-1][j] + f_table[i][j-1]
    k = K-1
    a = A
    b = B
    ans = []
    while True:
        if k >= f_table[a-1][b]:
            ans.append("b")
            k -= f_table[a-1][b]
            b -= 1
        else:
            ans.append("a")
            a -= 1
        if a == 0:
            ans += ["b"]*b
            break
        if b == 0:
            ans += ["a"]*a
            break
    print("".join(ans))


def main():
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(A, B, K)
    return

main()
