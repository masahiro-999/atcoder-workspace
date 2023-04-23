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



def solve(N: int, D: int, T: "List[int]"):
    ans = -1
    for i in range(1,N):
        if T[i] -T[i-1] <= D:
            ans = T[i]
            break
    print(ans)

def main():
    N, D = mi()  # type: int
    T = li()
    solve(N, D, T)
    return

main()
