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

def find_nonzero_min(s):
    a = list(filter(lambda x: x%10!=0, sorted(s)))
    if len(a) > 0:
        return a[0]
    else:
        return None
    
def solve(N: int, s: "List[int]"):
    all_sum = sum(s)
    if all_sum % 10 == 0:
        a = find_nonzero_min(s)
        if a is None:
            print(0)
        else:
            print(all_sum - a)
    else:
        print(all_sum)

def main():
    N = int(next(tokens))  # type: int
    s = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, s)
    return

main()
