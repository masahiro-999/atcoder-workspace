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


def replace(s):
    for i in range(len(s)-1):
        if s[i:i+2]=="TT":
           s = s[:i] + "PC" + s[i+2:]
    return s

def solve(H: int, W: int, S: "List[str]"):
    for s in S:
        s = replace(s)
        print(s)


def main():
    H, W = mi()  # type: int
    S = [input() for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)
    return

main()
