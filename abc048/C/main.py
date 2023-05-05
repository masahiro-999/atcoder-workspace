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



def solve(N: int, x: int, a: "List[int]"):
    ans = 0
    if a[0]>x:
        ans = a[0] - x
        a[0] -= ans
    for i in range(1,N):
        d = max(0,a[i]+a[i-1] - x)
        ans += d
        a[i] -= d
    print(ans)


def main():
    N,x = mi()  # type: int
    a = li()  # type: "List[int]"
    solve(N, x, a)
    return

main()
