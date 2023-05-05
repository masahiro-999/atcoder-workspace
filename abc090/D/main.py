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



def solve(N: int, K: int):
    def count_a(N,b):
        p = N // b
        r = N % b
        return max(0,b-K)*p + max(0,r+1-K) -(1 if K==0 else 0)
    
    ans = 0
    for i in range(1,N+1):
        ans += count_a(N, i)
    print(ans)

def main():
    N,K = mi()  # type: int
    solve(N, K)
    return

main()
