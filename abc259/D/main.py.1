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


YES = "Yes"
NO = "No"

def solve(N: int, s_x: int, s_y: int, t_x: int, t_y: int, X: "List[int]", Y: "List[int]", R: "List[int]"):
    def find(x,y):
        for i in range(N):
            xi,yi,ri = X[i], Y[i], R[i]
            if (x-xi)**2 + (y-yi)**2 == ri**2:
                return i
        return None

    u = UnionFind(N)
    for i in range(N-1):
        xi,yi,ri = X[i], Y[i], R[i]
        for j in range(i+1,N):
            xj,yj,rj = X[j], Y[j], R[j]
            d2 = (xi-xj)*(xi-xj)+(yi-yj)*(yi-yj)
            if d2 <= (ri+rj)*(ri+rj) and d2>= (ri-rj)*(ri-rj):
                u.union(i,j)
    s = find(s_x, s_y)    
    t = find(t_x, t_y)

    if u.same(s,t):
        print(YES)
    else:
        print(NO)

        
def main():
    N = int(next(tokens))  # type: int
    s_x = int(next(tokens))  # type: int
    s_y = int(next(tokens))  # type: int
    t_x = int(next(tokens))  # type: int
    t_y = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    r = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, s_x, s_y, t_x, t_y, x, y, r)
    return

main()
