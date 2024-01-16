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

def solve(N,M,a):
    table = defaultdict(lambda: -1)
    q_list = []*M
    for i in range(M):
        q_list.append(deque(a[i]))
    q = deque(range(M))
    while q:
        i = q.popleft()
        try:
            a = q_list[i].popleft()
        except IndexError:
            continue
        if table[a] != -1:
            q.append(i)
            q.append(table[a])
            del table[a]
        else:
            table[a] = i

    if len(table) == 0:
        ans = YES
    else:
        ans = NO
    print(ans)

def main():
    N = int(next(tokens)) 
    M = int(next(tokens)) 
    a = [0] * M
    for i in range(M):
        k = int(next(tokens))
        a[i] = li()
    solve(N,M,a)
    return

main()
