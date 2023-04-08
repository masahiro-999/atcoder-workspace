import sys
from collections import deque, Counter
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1



def solve(N: int, K: int, x: "List[int]"):
    ans = inf
    for i in range(N-K+1):
        l = i
        r = i+K-1
        t1 = abs(x[l])+x[r] - x[l]
        t2 = abs(x[r])+x[r] - x[l]
        ans = min(ans, t1)
        ans = min(ans, t2)

    print(ans)

def main():
    N, K = mi()  # type: int
    x = li()
    solve(N, K, x)
    return

main()
