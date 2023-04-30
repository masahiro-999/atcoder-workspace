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



def solve(N: int, A: "List[int]"):
    for i in range(N):
        A[i] -= (i+1)

    A.sort()
    d = [0]*N
    d[0] = A[0]
    for i in range(1,N):
        d[i] = d[i-1]+A[i]

    ans = inf
    for i in range(N):
        sum_l = A[i]*(i+1) - d[i]
        if i ==0:
            sum_r = d[N-1] - A[i]*(N-i)
        else:
            sum_r = d[N-1] - d[i-1] - A[i]*(N-i)
        ans = min(ans, sum_l + sum_r)

    print(ans)
    
def main():
    N = ii()  # type: int
    A = li()  # type: "List[int]"
    solve(N, A)
    return

main()
