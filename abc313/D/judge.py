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

K= 3
N= 5
import random
a = [random.randrange(2) for _ in range(N)]

print(N,K, flush=True)

while True:
    inp = input().split()
    if inp[0] == "?":
        ans = 0
        for i in map(int,inp[1:]):
            ans += a[i-1]
        print(ans % 2, flush=True)
    else:
        b = list(map(int,inp[1:]))
        if a == b:
            print("OK")
        else:
            print("NO")
        print(a)
        print(b)
        
        break

