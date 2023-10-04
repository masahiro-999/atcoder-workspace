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

def solve2(N: int, C: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    d = defaultdict(int)
    for i,j,k in zip(a,b,c):
        d[i] += k
        d[j+1] -= k

    prev = 0
    ans = 0
    sum_v = 0
    for k,v in sorted(d.items()):
        ans += min(sum_v,C)*(k-prev)
        sum_v += v
        prev = k

    print(ans)

def solve(N: int, C: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    active=set()
    sum_active = 0
    event = []
    for i,x in enumerate(a):
        event.append((x,False,i)) 
    for i,x in enumerate(b):
        event.append((x,True,i))
    event.sort()
    ans = 0
    prev_x = 0
    for x,is_end,i in event:
        if not is_end:
            ans += min(C, sum_active)*((x-1)-prev_x+1)
            active.add(i)
            sum_active += c[i]
            prev_x = x
        else:
            # end
            ans += min(C, sum_active)*(x-prev_x+1)
            active.remove(i)
            sum_active -= c[i]
            prev_x = x+1
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve2(N, C, a, b, c)
    return

main()
