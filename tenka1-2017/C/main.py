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
    for h in range(1,3501):
        for n in range(1,3501):
            a = N*h*n
            b = 4*h*n-n*N-h*N
            if b >0 and a % b==0:
                w = a//b
                print(h,n,w)
                return()

def main():
    N = ii()  # type: int
    solve(N)
    return

main()
