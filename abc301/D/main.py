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



def solve(S: str, N: int):
    s_min = int(S.replace("?", "0"), 2)
    if s_min > N:
        print(-1)
        return

    s_max = int(S.replace("?","1"),2)
    if s_max <= N:
        print(s_max)
        return
    ans = s_min
    for i in range(len(S)):
        if S[i] != "?":
            continue
        tmp = ans + (1<<(len(S)-i-1))                        
        if tmp <= N:
            ans = tmp

    print(ans)


def main():
    S = input()  # type: str
    N = ii()  # type: int
    solve(S, N)
    return

main()
