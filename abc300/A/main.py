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



def solve(N: int, A: int, B: int, C: "List[int]"):
    for  i,val in enumerate(C):
        if val == A+B:
            print(i+1)
            break


def main():
    N,A,B = mi()  # type: int
    C = li()  # type: "List[int]"
    solve(N, A, B, C)
    return

main()
