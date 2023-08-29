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


def solve(N: int, A: "List[int]"):
    q = deque()

    ans = 0
    for a in A:
        ans += 1
        if len(q) == 0:
            q.append((a,1))
        else:
            x,num = q[-1]
            if x == a:
                if num+1 == x:
                    q.pop()
                    ans -= x
                else:
                    q[-1] = (x, num+1)
            else:
                q.append((a,1))
        print(ans)

def main():
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)
    return

main()
