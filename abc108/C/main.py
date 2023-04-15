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



def solve(N: int, K: int):
    c = 0
    ans = 0
    for i in range(1,N+1):
        if i %K == 0:
            c += 1
    ans = c **3
    if K %2 == 0:
        c = 0
        for i in range(1,N+1):
            if i %K == K//2:
                c += 1
        ans += c**3
    print(ans)


def main():
    N,K = mi()  # type: int
    solve(N, K)
    return

main()
