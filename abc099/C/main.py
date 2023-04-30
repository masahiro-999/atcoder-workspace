import sys
from collections import deque, Counter, defaultdict
from itertools import product
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1



def solve(N: int):
    def getdp(i):
        ret = []
        if i-1 >=0:
            ret.append(dp[i-1])
        p6 = 6
        while i-p6>=0:
            ret.append(dp[i-p6])
            p6 *= 6
        p9 = 9
        while i-p9>=0:
            ret.append(dp[i-p9])
            p9 *= 9
        return ret

    dp = [0]*(N+1)
    for i in range(1,N+1):
        dp[i] = 1+min(getdp(i))

    ans = dp[N]
    print(ans)

def main():
    N = ii()  # type: int
    solve(N)
    return

main()
