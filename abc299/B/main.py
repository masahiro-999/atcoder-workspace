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



def solve(N: int, T: int, C: "List[int]", R: "List[int]"):
    ans = -1
    ans_max = -1
    for i in range(N):
        if C[i] == T:
            if ans_max < R[i]:
                ans_max = R[i]
                ans = i
    if ans == -1:
        T = C[0]
        for i in range(N):
            if C[i] == T:
                if ans_max < R[i]:
                    ans_max = R[i]
                    ans = i
    print(ans+1)


def main():
    N, T = mi()  # type: int
    C = li()  # type: "List[int]"
    R = li()  # type: "List[int]"
    solve(N, T, C, R)
    return

main()
