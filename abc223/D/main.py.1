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


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    forward = defaultdict(list)
    backword = defaultdict(list)
    for a, b in zip(A, B):
        forward[a].append(b)  # a -> b
        backword[b].append(a)  # b -> a

    top_list = []
    for i in range(1, N + 1):
        if not backword[i]:
            top_list.append(i)
    heapify(top_list)

    ans = []
    while top_list:
        top = heappop(top_list)
        ans.append(top)
        for b in forward[top]:
            backword[b].remove(top)
            if not backword[b]:
                heappush(top_list, b)
    print(*ans) if len(ans) == N else print(-1)
        
def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)
    return

if __name__ == '__main__':
    main()
