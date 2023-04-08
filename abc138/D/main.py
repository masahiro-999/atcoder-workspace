import sys
from collections import deque, Counter, defaultdict
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1


def solve(N: int, Q: int, a: "List[int]", b: "List[int]", p: "List[int]", x: "List[int]"):
    table_q = defaultdict(int)
    for p1, x1 in zip(p, x):
        table_q[p1] += x1

    t = defaultdict(list)
    for a1, b1 in zip(a,b):
        t[a1].append(b1)
        t[b1].append(a1)

    ans = [-1] * (N+1)
    q = deque()
    q.append(1)
    ans[1] = table_q[1]
    while q:
        p = q.popleft()
        for next in t[p]:
            if ans[next]==-1:
                ans[next] = ans[p] + table_q[next]
                q.append(next)

    print(*ans[1:])
        

def main():
    N,Q = mi()  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i], b[i] = li()
    p = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        p[i], x[i] = li()
    solve(N, Q, a, b, p, x)
    return

main()
