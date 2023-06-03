import sys
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from bisect import bisect
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
	
def solve(W: int, H: int, N: int, P: "List[int]", Q: "List[int]", A: int, a: "List[int]", B: int, b: "List[int]"):

    c = Counter()
    for i in range(N):
        p,q = P[i], Q[i]
        x = bisect(a,p)
        y = bisect(b,q)
        c[(x,y)] += 1

    maxv = max(c.values())
    minv = min(c.values()) if len(c) == (A+1)*(B+1) else 0
    print(minv, maxv)

def main():
    W,H = mi()  # type: int
    N = ii()  # type: int
    p = [int()] * (N)  # type: "List[int]"
    q = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        p[i],q[i]  = mi()
    A = ii()  # type: int
    a = li()
    B = ii()  # type: int
    b = li()
    solve(W, H, N, p, q, A, a, B, b)
    return

main()
