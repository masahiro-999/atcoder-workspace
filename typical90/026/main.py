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


def solve(N: int, A: "List[int]", B: "List[int]"):

    def bfs(start, ans1, ans2):
        dist = [-1]*N
        que = deque([start])
        dist[start] = 0
        while que:
            i = que.popleft()
            d = dist[i]
            if d % 2 == 0:
                ans1.append(i+1)
            else:
                ans2.append(i+1)
            for j in g[i]:
                if dist[j]==-1:
                    dist[j] = d+1
                    que.append(j)
        return dist

    ans1 = []
    ans2 = []
    g = defaultdict(list)
    for a,b in zip(A,B):
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    bfs(A[0]-1, ans1, ans2)    
    ans  = ans1 if len(ans1)> len(ans2) else ans2
    print(*ans[:N//2])

def main():
    N = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)
    return

main()
