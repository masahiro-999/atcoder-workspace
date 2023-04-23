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



def solve(N: int, S: str):
    max_x = 0
    c = 0
    for i in range(N+1):
        if i == N or S[i] =="-":
            if c !=0:
                max_x = max(max_x,c)
                c = 0
        else:
            c+=1
    
    if max_x == N or max_x == 0:
        print(-1)
    else:
        print(max_x)


def main():
    N = ii()  # type: int
    S = input()  # type: str
    solve(N, S)
    return

main()
