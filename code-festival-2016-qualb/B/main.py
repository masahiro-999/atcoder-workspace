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


YES = "Yes"
NO = "No"

def solve(N: int, A: int, B: int, S: str):
    b = 0
    ab = 0
    for x in S:
        if x == "a":
            if ab < A+B:
                ab += 1
                print(YES) 
            else:
                print(NO)
        elif x == "b":
            if ab < A+B and b < B:
                ab += 1
                b += 1
                print(YES)
            else:
                print(NO)
        else:
            print(NO)

def main():
    N, A, B = mi()  # type: int
    S = input()  # type: str
    solve(N, A, B, S)
    return

main()
