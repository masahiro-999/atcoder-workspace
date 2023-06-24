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


def solve(H,W,Q,Q_list):
    def to_index(r,c):
        return (r-1)*W+(c-1)
    
    u = UnionFind(H*W)
    t = [0]*(H*W)

    for q in Q_list:
        if q[0] == 1:
            r,c = q[1:]
            i = to_index(r,c)
            t[i] = 1
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0< r+dr <= H and 0< c+dc <= W:
                    j = to_index(r+dr, c+dc)
                    if t[j] == 1:
                        u.union(i,j)
        else:
            ra, ca, rb, cb = q[1:]
            i = to_index(ra,ca)
            j = to_index(rb,cb)
            if t[i] == 1 and t[j] == 1 and u.find(i) == u.find(j):
                print(YES)
            else:
                print(NO) 

def main():
    H = int(next(tokens))
    W = int(next(tokens))
    Q = int(next(tokens))
    Q_list = [li() for _ in range(Q)]
    solve(H,W,Q,Q_list)
    return

main()
