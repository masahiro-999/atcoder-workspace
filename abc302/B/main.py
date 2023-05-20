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


def check(H,W,S,i0,j0,dir):
    ans = []
    (dy,dx) = dir
    t="snuke"
    for i in range(5):
        i1 = i0+dy*i
        j1 = j0+dx*i
        ans.append((i1+1,j1+1))
        if 0<=i1<H and 0<=j1<W and S[i1][j1] ==t[i]:
            continue
        else:
            return False
    return ans


def solve(H: int, W: int, S: "List[str]"):
    for i in range(H):
        for j in range(W):
            if S[i][j] == "s":
                for dir in [(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]:
                    ans = check(H,W,S,i,j,dir)
                    if ans:
                        for r,c in ans:
                            print(r,c)
                        return
    

def main():
    H,W = mi()  # type: int
    S = [input() for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)
    return

main()
