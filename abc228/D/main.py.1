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
        self.write_pos = defaultdict(lambda : -1)

    def set_write_pos(self, x, write_pos):
        root = self.find(x)
        self.write_pos[root] = write_pos
    
    def get_write_pos(self, x):
        root = self.find(x)
        return self.write_pos[root]

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

        wrote_pos = self.write_pos[y]
    
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        self.write_pos[x] = wrote_pos

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

MOD = 1

def solve(Q: int, tx):
    N = 1 << 20
    a = [-1] * N
    uf = UnionFind(N)
    for t, x in tx:
        if t == 1:
            if a[(x)%N] == -1:
                write_pos = (x)%N
            else:
                write_pos = (uf.get_write_pos((x)%N)+1)%N

            uf.set_write_pos(write_pos, write_pos)
            a[write_pos] = x
            # ひつ前とつなげる
            if a[(write_pos-1)%N] != -1:
                uf.union((write_pos-1)%N, (write_pos)%N)
            # 一つ後とつなげる
            if a[(write_pos+1)%N] != -1:
                uf.union((write_pos)%N, (write_pos+1)%N)

        else:
            print(a[x%N])
    return

def main():
    Q = int(next(tokens))  # type: int
    tx = [li() for _ in range(Q)]
    solve(Q, tx)
    return

if __name__ == '__main__':
    main()
