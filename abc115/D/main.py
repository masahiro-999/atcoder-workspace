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



def solve(N: int, X: int):
    
    def patties(N,X):
        if N==0:
            return 1
        if X==1:
            return 0
        if X <= 1+l[N-1]:
            return patties(N-1,X-1)
        if X == 2+l[N-1]:
            return p[N-1]+1
        return p[N-1] + 1 + patties(N-1,X-(1+l[N-1]+1))
    
    p = [0] * (N+1)
    l = [0] * (N+1)
    p[0] = 1
    l[0] = 1
    for i in range(1,N+1):
        p[i] = 1+p[i-1]*2
        l[i] = 3+l[i-1]*2
    
    ans = patties(N,X) 
    print(ans)


def main():
    N, X = mi()  # type: int
    solve(N, X)
    return

main()
