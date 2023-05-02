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



def solve(N: int, K: int, S: str):
    c = 0
    for i in range(1,N):
        if S[i-1] != S[i]:
            c += 1
    ans = N-1-(c)
    ans = min(N-1, ans +K*2)
    print(ans)

def main():
    N, K = li()  # type: int
    S = input()  # type: str
    solve(N, K, S)
    return

main()
