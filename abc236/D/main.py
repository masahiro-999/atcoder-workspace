import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
from functools import reduce
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


def solve(N,a):

    def f(remain_numbers_set, curent_value):
        if remain_numbers_set == set():
            return curent_value
        n_min = min(list(remain_numbers_set))
        copy_of_remain_numbers_set = remain_numbers_set.copy()
        copy_of_remain_numbers_set.remove(n_min)
        ret_max = -1
        for i in copy_of_remain_numbers_set:
            tmp = copy_of_remain_numbers_set.copy()
            tmp.remove(i)
            ret_max = max(ret_max,
                f(tmp, curent_value ^ a[n_min-1][i-1]))
        return ret_max
    
    ans = f(set(range(1,2*N+1)),0)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    a = [[0]*(i+1) + li() for i in range(2*N-1)]
    solve(N,a)
    return

main()
