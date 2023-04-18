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



def solve(H: int, N: int, A: "List[int]", B: "List[int]"):

    dp = [inf]*(H+1)
    dp[0] = 0
    for i in range(N):
        for j in range(H):
            tmp = min(H, j+A[i])
            dp[tmp] = min(dp[tmp],dp[j]+B[i])

    print(dp[H])

def main():
    H, N = mi()  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i], B[i] = mi()
    solve(H, N, A, B)
    return

main()
