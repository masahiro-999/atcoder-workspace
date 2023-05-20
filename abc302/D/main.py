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



def solve(N: int, M: int, D: int, A: "List[int]", B: "List[int]"):
    A.sort(reverse = True)
    B.sort(reverse = True)
    ai = 0
    bi = 0
    ans = 0
    while ai < N and bi < M:
        d = A[ai] - B[bi]
        if abs(d) <= D:
            ans = A[ai] + B[bi]
            break
        if d > 0:
            ai += 1
        else:
            bi += 1
    if ans == 0:
        print(-1)
    else:
        print(ans)

def main():
    N,M,D = mi()  # type: int
    A = li()  # type: "List[int]"
    B = li()  # type: "List[int]"
    solve(N, M, D, A, B)
    return

main()
