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

YES = "Yes"
NO = "No"

def solve(N: int, a: "List[int]"):
    def num_dev2(x):
        for i in range(3):
            if x % 2 != 0:
                break
            x = x //2
        return i
    
    n = [num_dev2(i) for i in a]
    n0 = len(list(filter(lambda x: x == 0, n)))
    # n1 = filter(lambda x: x == 1, n)
    n2 = len(list(filter(lambda x: x == 2, n)))
    n1 = N - n0 - n2
    if n1 == 0 and n0 > n2+1:
        print(NO)
    elif n1 != 0 and n0 > n2:
        print(NO)
    else:
        print(YES)


def main():
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)
    return

main()
