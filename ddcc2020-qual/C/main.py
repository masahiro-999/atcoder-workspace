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

def solve(H,W,K,s):
    ans = [0]*H
    count = 1
    b = [0]*W
    skip = True
    for i in range(H):
        if "#" in s[i]:
            lastone = s[i].rfind("#")
            for j in range(lastone+1):
                b[j] = count
                if s[i][j] == "#":
                    count += 1
            if lastone < W-1:
                for j in range(lastone,W):
                    b[j] = count-1
            if skip ==True:
                skip = False
                for k in range(i):
                    ans[k] = b[:]
        else:
            if skip == False:
                b[:] = ans[i-1]
        ans[i] = b[:]
    for i in range(H):
        print(*ans[i])

def main():
    H,W,K = mi()
    s= [""]*H
    for i in range(H):
        s[i] = input()

    solve(H,W,K,s)
    return

main()
