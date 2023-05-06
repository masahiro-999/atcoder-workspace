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

def solve(N,f,p):
    ans = -inf
    for pattern in range(1,1<<10):
        d = 0
        for i in range(N):
            c_open = 0
            p1 = pattern
            for j in range(10):
                if p1 &1 == 1 and f[i][j] ==1:
                    c_open += 1
                p1 = p1 >> 1
            d += p[i][c_open]
        ans = max(ans,d)
    print(ans)

def main():
    N = ii()
    f = [li() for _ in range(N)]
    p = [li() for _ in range(N)]
    solve(N,f,p)
    return


main()
