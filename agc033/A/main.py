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



def solve(H: int, W: int, A: "List[str]"):
    t = [[-1]*W for _ in range(H)]
    q = deque()
    for i in range(H):
        for j in range(W):
            if A[i][j] == "#":
                t[i][j] = 0
                q.append((i,j))

    while q:
        i,j = q.popleft()
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0<=i+di<H and 0<=j+dj<W:
                if t[i+di][j+dj] ==-1:
                    t[i+di][j+dj] = t[i][j]+1
                    q.append((i+di,j+dj))
    ans = max([max(x) for x in t])
    print(ans)

def main():
    H,W = mi()  # type: int
    A = [input() for _ in range(H)]  # type: "List[str]"
    solve(H, W, A)
    return

main()
