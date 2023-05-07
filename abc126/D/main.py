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



def solve(N: int, u: "List[int]", v: "List[int]", w: "List[int]"):
    ans = [-1]*N
    t = [[] for _ in range(N)]
    for u1,v1,w1 in zip(u,v,w):
        u1 -= 1
        v1 -= 1
        t[u1].append((v1,w1))
        t[v1].append((u1,w1))

    q = deque()

    q.append(u[0])
    ans[u[0]] = 0
    while q:
        a = q.popleft()
        for next, next_w in t[a]:
            if ans[next] == -1:
                if next_w %2 ==0:
                    ans[next] = ans[a]
                else:
                    ans[next] = 1-ans[a]
                q.append(next)
    print(*ans, sep="\n")

def main():
    N = ii()  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    w = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i], v[i], w[i] = mi()
    solve(N, u, v, w)
    return

main()
