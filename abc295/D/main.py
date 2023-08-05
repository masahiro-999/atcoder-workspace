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

def s_to_n(s):
    return ord(s)-ord("0")

def solve(S: str):
    # d[r] 文字までの嬉しい列の数
    d = []
    bit = 0
    d.append(bit)
    for s in S:
        bit ^= 1<<s_to_n(s)
        d.append(bit)

    c = Counter(d)
    ans = 0
    for x in c.values():
        ans += x*(x-1)//2
    print(ans)
    
def main():
    S = next(tokens)  # type: str
    solve(S)
    return

main()
