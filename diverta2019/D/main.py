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



def solve(N: int):
    k = 1
    ans = 0
    for k in range(1, int(N**0.5)+1):
        if N%k ==0:
            x = N//k-1
            if k < x:
                ans += x
        k+= 1
    print(ans)

def main():
    N = ii()  # type: int
    solve(N)
    return

main()
