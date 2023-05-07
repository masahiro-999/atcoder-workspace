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



def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]", Q: int, K: int, X: "List[int]", Y: "List[int]"):
    g = [[] for _ in range(N+1)]
    d = [0] * (N+1)
    def dfs(k,w,prev):
        for n,nw in g[k]:
            if n != prev:
                dfs(n,w+nw,k)
        d[k] = w

    for a,b,c in zip(A,B,C):
        g[a].append((b,c))
        g[b].append((a,c))

    dfs(K,0,-1)

    for x,y in zip(X,Y):
        print(d[x]+d[y])

def main():
    N = ii()  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    c = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i],b[i],c[i] = mi()
    Q,K = mi()  # type: int
    x = [int()] * (Q)  # type: "List[int]"
    y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        x[i],y[i] = mi()
    solve(N, a, b, c, Q, K, x, y)
    return

main()
