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


YES = "Yes"
NO = "No"

def solve(N: int, S: str, T: str):
    ans = YES
    for s,t in zip(S,T):
        if s == t or ((s in ["1", "l"]) and (t in ["1", "l"])) or ((s in ["0", "o"]) and (t in ["0", "o"])): 
            continue
        else:
            ans = NO
            break
    print(ans)

def main():
    N = ii()  # type: int
    S = input()  # type: str
    T = input()  # type: str
    solve(N, S, T)
    return

main()
