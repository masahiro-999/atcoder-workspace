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

def solve(X: int, Y: int, Z: int, S: str):
    ans = 0
    d1 = 0 # current="a"
    d2 = inf # current="A"
    for s in S:
        if s == "a":
            d1,d2 = min(d1 + X, d2 + Z+X),min(d1 + Z+Y, d2+Y)
        else:
            d1,d2 = min(d1 + Y, d2 + Z+Y),min(d1 + Z+X, d2+X)
    ans = min(d1,d2)
    print(ans)

def main():
    X, Y, Z = mi()  # type: int
    S = input()  # type: str
    solve(X, Y, Z, S)
    return

main()

