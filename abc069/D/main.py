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



def solve(H: int, W: int, N: int, a: "List[int]"):
    
    c = []
    for i, n in enumerate(a):
        for j in range(n):
            c.append(i+1)

    for i in range(H):
        if i % 2 ==0:
            print(*c[i*W:i*W+W])
        else:
            x = c[i*W:i*W+W]
            x.reverse()
            print(*x)

def main():
    H,W = mi()  # type: int
    N = ii()  # type: int
    a = li()  # type: "List[int]"
    solve(H, W, N, a)
    return

main()
