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


def solve(N: int, K: int, A: "List[List[int]]"):
    def count_over_n_in_sqr(n,k):
        # 中央値は、大きい方からk*k//2+1番目の数
        # 中央値はn以下か？を言い換えると
        # nを超える数を1にしたとき、k*kの中の1の数がk*k//2+1未満か？
        a_over_n = [[1 if a > n else 0 for a in a_list] for a_list in A]
        acc_over_n = [ list(accumulate([0]+a)) for a in a_over_n]
        col = [[a[j+k] - a[j] for j in range(N-k+1)] for a in acc_over_n] 
        transpose_col = [list(t) for t in zip(*col)]
        acc_transpose_col = [list(accumulate([0]+a)) for a in transpose_col]
        ans  = [[a[j+k] - a[j] for j in range(N-k+1)] for a in acc_transpose_col] 
        for i in range(N-k+1):
            for j in range(N-k+1):
                if ans[i][j] < (k*k//2+1):
                    return True
        return False

    l = -1 # False 
    r = 10**9+1 # True
    while r-l > 1:
        mid = (r+l)//2
        if count_over_n_in_sqr(mid,K):
            r = mid
        else:
            l = mid
    print(r)
    return

def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, K, A)
    return

main()
