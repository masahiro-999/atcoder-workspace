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
import math


def solve(S: int):
    # s = x2*y3 -x3*y2
    # s = 1000000000*y3 -y2
    x1 = 0
    y1 = 0
    x2 = 1000000000
    y3 = math.ceil(S / x2)
    x3 = 1
    y2 = x2*y3 -S
    
    print(x1, y1, x2, y2, x3, y3)

def main():
    S = ii()  # type: int
    solve(S)
    return

main()
