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



def solve(N: int, M: int):
    d = M//N
    ans = 1
    for i in range(1,int(M**.5)+1):
        if M %i ==0:
            a = M//i
            if a <= d:
                ans = max(ans, a)
            if i <= d:
                ans = max(ans, i)
    print(ans)


def main():
    N, M = li()  # type: int
    solve(N, M)
    return

main()
