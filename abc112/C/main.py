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



def solve(N: int, xyh):
    d = []
    for cx in range(101):
        for cy in range(101):
            prev_ch = -1
            for x,y,h in xyh:
                if h ==0:
                    continue
                ch = h + abs(cx-x) + abs(cy-y)
                if prev_ch != -1 and prev_ch != ch:
                    break
                prev_ch = ch
            else:
                d.append((cx, cy, ch))

    for cx,cy,ch in d:
        for x,y,h in xyh:
            h1 = max(0,ch - abs(cx-x) - abs(cy-y))
            if h != h1:
                break
        else:
            print(cx,cy,ch)
            return


def main():
    N = ii()  # type: int
    xyh = [li() for _ in range(N)]  # type: "List[int]"
    solve(N, xyh)
    return

main()
