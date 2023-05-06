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


YES = "Yes"
NO = "No"


def solve(H,W,a,b):

    def cmp(s,t):
        for i in range(H):
            for j in range(W):
                if b[i][j] != a[(i+s)%H][(j+t)%W]:
                    return False
        return True

    ans = NO
    for s in range(H):
        for t in range(W):
            if cmp(s,t):
                ans = YES
                break
    print(ans)    

def main():
    H,W = mi()  # type: int
    a = [input() for _ in range(H)]  # type: "List[int]"
    b = [input() for _ in range(H)]  # type: "List[int]"
    solve(H,W, a, b)
    return

main()
