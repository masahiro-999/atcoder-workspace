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
    r = 0
    l = 0
    i = 0
    c = 0
    while i <N:
        
        if S[i]==")":
            if c == 0:
                r += 1
            else:
                c -=1
        elif S[i] =="(":
            c += 1
        i += 1
    print("("*r+S+")"*c)

def main():
    N = ii()  # type: int
    S = input()  # type: str
    solve(N, S)
    return

main()
