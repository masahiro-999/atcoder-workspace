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


def solve(N: int, b: "List[int]"):
    def find_most_right(b):
        l = len(b)
        for i in range(l-1, -1, -1):
            if b[i] == i+1:
                return i
        return -1
    ans = []    
    while b:
        i = find_most_right(b)
        if i == -1:
            break
        b.pop(i)
        ans.append(i+1)
    if not b:
        print(*ans[::-1], sep="\n")
    else:
        print(-1)

def main():
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, b)
    return

main()
