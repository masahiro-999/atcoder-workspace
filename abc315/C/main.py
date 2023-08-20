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


def solve(N: int, F: "List[int]", S: "List[int]"):
    tt = defaultdict(list)
    for f,s in zip(F,S):
        tt[f].append(s)

    max_s1 = []
    for s_list in tt.values():
        max_s1.append(max(s_list))
    if len(max_s1)>=2:
        max_s1.sort(reverse=True)
        s = max_s1[0]
        t = max_s1[1]
        ans = s+t
    else:
        ans = -1

    for s_list in tt.values():
        if len(s_list) >= 2:
            s_list.sort(reverse=True)
            s = s_list[0]
            t = s_list[1]
            ans = max(ans,s+t//2)

    print(ans)

def main():
    N = int(next(tokens))  # type: int
    F = [int()] * (N)  # type: "List[int]"
    S = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        F[i] = int(next(tokens))
        S[i] = int(next(tokens))
    solve(N, F, S)
    return

main()
