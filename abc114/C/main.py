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

from itertools import product 

def f(s):
    t = [0,0,0,1,1,2,2,3,3,3]
    return t[int(s)]

def solve(N: int):

    ans = 0
    for k in range(1,10):
        for a in product(["3","5","7"], repeat=k):
            if "3" not in a or "5" not in a or "7" not in a:
                continue
            if int("".join(a)) >N:
                break
            ans += 1

    print(ans)

def main():
    N = ii()  # type: int
    solve(N)
    return

main()
