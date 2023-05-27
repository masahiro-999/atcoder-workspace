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

def solve(N: int, M: int, H: int, K: int, S: str, xy):
    xy_set = set()
    for [x,y] in xy:
        xy_set.add((x,y))
    ans = YES
    x = 0
    y = 0
    for s in S:
        if s == "R":
            x += 1
        elif s == "L":
            x -= 1
        elif s == "U":
            y += 1
        elif s == "D":
            y -= 1
        H -= 1
        if H <0:
            ans = NO
            break
        if (x,y) in xy_set:
            if H < K:
                xy_set.remove((x,y))
                H = K
    print(ans)        

def main():
    N,M,H,K = mi()  # type: int
    S = input()  # type: str
    xy = [li() for _ in range(M)]
    solve(N, M, H, K, S, xy)
    return

main()
