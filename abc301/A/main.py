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



def solve(N: int, S: str):
    t = 0
    a = 0
    f = -1
    for i in S:
        if i == "T":
            t += 1
            if f == -1 and t == N//2:
                f = "T"
        else:
            a += 1
            if f == -1 and a == N//2:
                f = "A"
    
    if (a == t):
        if f=="T":
            print("T")
        else:
            print("A")
    elif (a > t):
        print("A")
    else:
        print("T")

def main():
    N = ii()  # type: int
    S = input()  # type: str
    solve(N, S)
    return

main()
