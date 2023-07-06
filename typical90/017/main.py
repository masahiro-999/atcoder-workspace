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


def solve(N: int, M: int, L: "List[int]", R: "List[int]"):
    def create_c(l):
        ret = []
        count = 0
        prev_i = 0
        for i in l:
            for _ in range(i-prev_i):
                ret.append(count)
            count += 1
            prev_i = i
        for _ in range(N-len(ret)):
            ret.append(count)
        return ret
    
    def count_between(c,i,j):
        if i > j:
            i,j = j,i
            # i<j
        return c[j-1] - c[i]

    def count_cross(i,j):
        # i<j
        i_end_list = d[i]
        j_end_list = d[j]
        ret = 0
        for i_end in i_end_list:
            ret += count_between(c_table[j],i,i_end)
        return ret

    d = defaultdict(list)
    c_table = [None]*N
    for l,r in zip(L,R):
        l -= 1
        r -= 1
        d[l].append(r)
        d[r].append(l)
    for i in range(N):
        d[i].sort()
        c_table[i] = create_c(d[i])
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            ans += count_cross(i,j)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = [int()] * (M)  # type: "List[int]"
    R = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, M, L, R)
    return

main()
