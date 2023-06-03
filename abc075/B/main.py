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

def count(H,W,S,i,j):
    count = 0
    for di in range(-1,2):
        for dj in range(-1,2):
            if di==0 and dj==0:
                continue
            if 0<= i+di < H and 0<= j+dj<W:
                if S[i+di][j+dj] == "#":
                    count += 1
    return count

def solve(H: int, W: int, S: "List[str]"):
    for i in range(H):
        str = ""
        for j in range(W):
            if S[i][j] == "#":
                str += "#"
            else:
                str += f'{count(H,W,S,i,j)}'
        print(str)

def main():
    H,W = mi()  # type: int
    S = [input() for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)
    return

main()
