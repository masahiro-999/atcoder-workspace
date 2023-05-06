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

def solve(H,W,c):

    s =[0]*min(H,W)

    for j in range(W):
        i = 0
        count = 0
        while j >=-1 and i <=H:
            if i<H and j >=0 and c[i][j] == "#":
                count +=1
            else:
                count //=2
                if count > 0:
                    s[count-1] += 1
                count = 0
            j -= 1
            i += 1


    for i in range(1,H):
        j = W-1
        count = 0
        while j >=-1 and i <= H:
            if i<H and j >=0 and c[i][j] == "#":
                count +=1
            else:
                count //=2
                if count > 0:
                    s[count-1] += 1
                count = 0
            j -= 1
            i += 1

    print(*s)


def main():

    H,W = mi()  # type: int
    c = [input() for _ in range(H)]  # type: "List[int]"
    solve(H,W, c)
    return

main()
