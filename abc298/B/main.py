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


YES = "Yes"
NO = "No"

def rotate(N,a):
    b =[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            b[N-1-j][i] = a[i][j]
    return b

def check(N,a,b):
    for i in range(N):
        for j in range(N):
            if a[i][j] and (b[i][j] == False):
                return False
    return True


def solve(N: int, A: "List[List[int]]", B: "List[List[int]]"):
    ans = NO
    for i in range(4):
        if check(N, A, B):
            ans = YES
            break
        A = rotate(N,A)
    print(ans)


def main():
    N = ii()  # type: int
    A = [li() for _ in range(N)]  # type: "List[List[int]]"
    B = [li() for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A, B)
    return

main()
