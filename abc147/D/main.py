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


MOD = 1000000007

def solve(N: int, A: "List[int]"):
    ans = 0
    for i in range(60):
        c0=0
        c1=0
        for a in A:
            if a & (1<<i):
                c1+=1
            else:
                c0+=1
        ans += (1<<i)*c1*c0
        ans = ans % MOD
    print(ans)

def main():
    N = ii()  # type: int
    A = li()  # type: "List[int]"
    solve(N, A)
    return

main()
