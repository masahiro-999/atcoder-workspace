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

def solve(S: str):
    a = S.find("B")
    b= S.rfind("B")
    if not(a%2 ==0 and b%2 == 1 or a%2 ==1 and b%2 == 0):
        ans = NO
    else:
        x = S.find("R")
        y= S.rfind("R")
        z= S.rfind("K")
        if x < z < y:
            ans = YES
        else:
            ans = NO

    print(ans)


def main():
    S = input()  # type: str
    solve(S)
    return

main()
