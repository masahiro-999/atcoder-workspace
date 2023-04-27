import sys
from collections import deque, Counter, defaultdict
from itertools import product
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1



def solve(S: str, T: str):
    c = 0
    for a,b in zip(S,T):
        if a==b:
            c+=1
    print(c)

def main():
    S = input()  # type: str
    T = input()  # type: str
    solve(S, T)
    return

main()
