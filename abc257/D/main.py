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

#abc157_dで使用した

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def solve(N: int, X: "List[int]", Y: "List[int]", P: "List[int]"):

    def update_t1(s):
        for i in range(N):
            for j in range(N):
                if i == j:
                    t1[i][j] = False
                else:                    
                    p,d = t[i][j]
                    t1[i][j] = p*s >= d
    
    def dfs(i):
        nonlocal visited
        for j in range(N):
            if t1[i][j] and j not in visited:
                visited.add(j)
                dfs(j)

    def is_successful(s):
        nonlocal visited
        update_t1(s)
        for i in range(N):
            visited = set([i])
            dfs(i)
            if len(visited)==N:
                return True
        return False

    visited = set()
    t = [[0]*N for _ in range(N)]
    t1 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            t[i][j] = (P[i], abs(X[i]-X[j])+abs(Y[i]-Y[j]))

    l = 0
    r = 4000000000
    while (r-l)>1:
        mid = (l+r)//2
        if is_successful(mid):
            r = mid
        else:
            l = mid    
    print(r)

def main():
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        P[i] = int(next(tokens))
    solve(N, x, y, P)
    return

main()
