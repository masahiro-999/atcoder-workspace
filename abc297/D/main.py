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



def solve(A: int, B: int):
    ans = 0
    while A!= B:
        if A>B:
            if A % B != 0:
                ans += A//B
                A = A % B
            else:
                ans += (A//B)-1
                A =B 
        else:
            if B % A != 0:
                ans += B//A
                B = B % A
            else:
                ans += B//A-1
                B =A

    print(ans)


def main():
    A, B = mi()  # type: int
    solve(A, B)
    return

main()
