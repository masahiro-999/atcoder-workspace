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



def solve(H: int, W: int, a: "List[List[int]]"):
    ans = []
    for i in range(H-1):
        for j in range(W):
            if a[i][j] % 2:
                a[i][j] -= 1
                a[i+1][j] += 1
                ans.append((i+1,j+1,i+1+1,j+1))
    i = H-1
    for j in range(W-1):
        if a[i][j] % 2:
            a[i][j] -= 1
            a[i][j+1] += 1
            ans.append((i+1,j+1,i+1,j+1+1))

    print(len(ans))    
    for a in ans:
        print(*a)

def main():
    H,W = mi()  # type: int
    a = [li() for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, a)
    return

main()
