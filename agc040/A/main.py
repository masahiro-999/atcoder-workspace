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
    n = len(S)+1
    a = [0] * (n)
    c = 0
    for i in range(n-1):
        if S[i] == "<":
            c += 1
            a[i+1] = c
        else:
            c = 0
    c = 0
    for i in range(n-2, -1, -1):
        if S[i] == ">":
            c += 1
            a[i] = max(a[i], c)
        else:
            c = 0
    ans = sum(a)
    print(ans)
    
def main():
    S = input()  # type: str
    solve(S)
    return

main()
