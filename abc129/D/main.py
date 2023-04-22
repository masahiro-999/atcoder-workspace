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



def solve(H: int, W: int, S: "List[str]"):
    dh =[[0]*W for _ in range(H)]
    dv =[[0]*W for _ in range(H)]
    for i in range(H):
        s = 0
        for e in range(W+1):
            if e ==W or S[i][e] == "#":
                if e-s > 0:
                    for j in range(s,e):
                        dh[i][j] = e-s
                s = e+1
    for i in range(W):
        s = 0
        for e in range(H+1):
            if e ==H or S[e][i] == "#":
                if e-s >0:
                    for j in range(s,e):
                        dv[j][i] = e-s
                s = e+1
    ans = 0
    for i in range(H):
        for j in range(W):
            ans = max(ans, dh[i][j]+dv[i][j])
    print(ans-1)

def main():
    H,W = mi()  # type: int
    S = [input() for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)
    return

main()
