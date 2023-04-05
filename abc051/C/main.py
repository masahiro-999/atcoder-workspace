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



def solve(sx: int, sy: int, tx: int, ty: int):
    dx = tx - sx
    dy = ty - sy
    UR = "U"*dy + "R"*dx
    DL = "D"*dy + "L"*dx
    ans = f'{UR}{DL}LU{UR}RDRD{DL}LU'
    print(ans)

def main():
    sx, sy, tx, ty = mi()  # type: int
    solve(sx, sy, tx, ty)
    return

main()
