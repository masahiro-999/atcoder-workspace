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

def bfs(H,W,s,sx,sy):
    q = deque()
    q.append((sy,sx))
    d = [[-1]*W for _ in range(H)]
    d[sy][sx] = 0
    while q:
        y,x = q.popleft()
        for (dx,dy) in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=x+dx < W and 0<=y+dy<H and s[y+dy][x+dx] == "." and d[y+dy][x+dx] == -1:
                d[y+dy][x+dx] = d[y][x]+1
                q.append((y+dy,x+dx))
    return max([max(l) for l in d])
                
def solve(H,W,s):
    ans = 0
    for i in range(H):
        for j in range(W):
            if s[i][j] == ".":
                ans = max(ans, bfs(H,W,s,j,i))
    print(ans)

def main():
    H,W = mi()
    s = [0]*H
    for i in range(H):
        s[i] = input()

    solve(H,W,s)

    return

main()
