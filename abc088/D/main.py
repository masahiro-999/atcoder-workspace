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

def solve(H,W,S):
    q = deque()
    if S[0][0] == ".":
        q.append((0,0))
        d =[[-1]*W for _ in range(H)] 
        d[0][0] = 1
        while q:
            y,x = q.popleft()
            for dy,dx in [(1,0), (-1,0),(0,1),(0,-1)]:
                if 0<=y+dy<H and 0<=x+dx<W and d[y+dy][x+dx]==-1 and S[y+dy][x+dx]==".":
                    d[y+dy][x+dx] = d[y][x]+1
                    q.append((y+dy,x+dx))
        min_d = d[H-1][W-1]
    else:
        min_d = -1

    if min_d == -1:
        print(-1)
    else:
        count = 0
        for s in S:
            for x in s:
                if x == ".":
                    count +=1
        print(count-min_d)

def main():
    H,W = mi()
    S = []
    for i in range(H):
        S.append(input())
    solve(H,W,S)

    return

main()
