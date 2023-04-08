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



def solve(N: int, A: "List[int]"):
    A.sort()
    B = A[:]
    for i in range(1,N):
        B[i] += B[i-1]

    ans = N
    for i in range(N-2,-1,-1):
        if B[i]*2 < A[i+1]:
            ans = N-i-1
            break 
    print(ans)

def main():
    N = ii()  # type: int
    A = li()
    solve(N, A)
    return

main()
