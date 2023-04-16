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

def solve(N: int, S: str):
    if S.find("o") ==-1:
        ans = NO
    else:
        if S.find("x") ==-1:
            ans = YES
        else:
            ans = NO
    print(ans)
    
def main():
    N = ii()  # type: int
    S = input()  # type: str
    solve(N, S)
    return

main()
