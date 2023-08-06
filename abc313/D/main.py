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

def q_and_a(q):
    print("? "+ " ".join(map(str,q)), flush=True)
    return ii()

def solve1(N):
    a = [0]*N
    for i in range(N):
        a[i] = q_and_a([i+1])
    print("! "+" ".join(map(str,a)), flush=True)

def solve(N, K):
    q_list = []
    for i in range(1, K+2):
        q = [x for x in range(1, K+2) if x!=i]
        q_list.append(q)

    a = [0]*(N)
    ans = [0]*(N)
    for i,q in enumerate(q_list):
         ans[i] = q_and_a(q) 

    top_k = reduce(lambda a,b: a^b, ans[:K+1], 0)
    for i in range(K+1):
        a[i] = ans[i] ^ top_k

    for i in range(K+2, N+1):
        q = [x for x in range(1,K)]+[i]
        a[i-1] = q_and_a(q) ^ reduce(lambda a,b: a^b, a[:K-1], 0)
    print("! "+" ".join(map(str,a)), flush=True)

def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    if K == 1:
        solve1(N)
    else:
        solve(N, K)
    return

main()
