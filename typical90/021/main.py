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

class Scc:
    def __init__(self, n):
        self.g = defaultdict(list)
        self.g_rev = defaultdict(list)
        self.n = n

    def clear_visited(self):
        self.visited = [False] * self.n

    def rdfs(self, i):
        self.path.add(i)
        self.visited[i] = True
        for n in self.g_rev[i]:
            if n not in self.path and not self.visited[n]:
                self.rdfs(n)

    def dfs(self, s):
        self.visited[s] = 1
        for n in self.g[s]:
            if not self.visited[n]:
                self.dfs(n)
        self.order.append(s)

    def add_edge(self, a, b):
        self.g[a].append(b)
        self.g_rev[b].append(a)

    def forward_dfs(self):
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i)

    def reverse_dfs(self):
        result = []
        for i in reversed(self.order):
            if self.visited[i]:
                continue
            self.path = set()
            self.rdfs(i)
            result.append(self.path)
        return result

    def scc(self):
        self.order = []
        self.clear_visited()
        self.forward_dfs()
        self.clear_visited()
        return self.reverse_dfs()


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    
    scc = Scc(N)
    for i in range(M):
        scc.add_edge(A[i]-1, B[i]-1)
    
    result = scc.scc()
    ans = 0
    for i in result:
        l = len(i)
        ans += l*(l-1)//2

    print(ans)

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

main()
