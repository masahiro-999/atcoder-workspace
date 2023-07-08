import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())


def f(x):
    ret = 1
    for i in x:
        ret *= int(i)
    return ret

def str_cmp(str1, str2):
    # str2はソート済み
    s1 =[i for i in str1]
    s1.sort()
    s2 =[i for i in str2]
    return s1 == s2

def solve(N: int, B: int):
    ans = 0
    def create_num_and_count(str, i):
        nonlocal ans
        if len(str) == 11:
            return
        for j in range(i,9+1):
            str_next = str+f'{j}'
            # print(str_next)
            m = B+f(str_next)
            if 1 <= m <= N and str_cmp(f'{m}', str_next):  
                ans += 1
            create_num_and_count(str_next,j) 
    create_num_and_count("",0)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, B)
    return

main()
