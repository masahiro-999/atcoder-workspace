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



def solve(S: str):
    first_b = S.find("B")
    if first_b == -1:
        return 0
    S = S[first_b:]
    d = [0]*len(S)
    s = 0
    for i in range(len(S)-1, -1, -1):
        if S[i] == "W":
            s += 1
        d[i] = s

    ans = 0
    for i in range(len(S)):
        if S[i] == "B":
            ans += d[i]

    return ans

def main():
    S = input()  # type: str
    print(solve(S))
    return

main()
