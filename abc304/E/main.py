import sys
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1

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

def solve(N: int, M: int, u: "List[int]", v: "List[int]", K: int, x: "List[int]", y: "List[int]", Q: int, p: "List[int]", q: "List[int]"):
    g1 = UnionFind(N+1)
    for i in range(M):
        g1.union(u[i],v[i])

    good = True
    nglist = set()
    for i in range(K):
        if g1.same(x[i],y[i]):
            good = False
        nglist.add((g1.find(x[i]), g1.find(y[i])))
        nglist.add((g1.find(y[i]), g1.find(x[i])))

    for i in range(Q):
        if good == True and (g1.find(p[i]), g1.find(q[i])) not in nglist:
            print(YES)
        else:
            print(NO)



def main():
    N,M = mi()  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i],v[i] = mi()
    K = ii()  # type: int
    x = [int()] * (K)  # type: "List[int]"
    y = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        x[i],y[i] = mi()
    Q = ii()  # type: int
    p = [int()] * (Q)  # type: "List[int]"
    q = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i],q[i] = mi()
    solve(N, M, u, v, K, x, y, Q, p, q)
    return

main()
