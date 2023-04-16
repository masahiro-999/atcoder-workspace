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



def solve(X: str):
    buf = []
    for i in X:
        if buf and buf[-1] == "S" and i=="T":
            buf.pop()
            continue 
        buf.append(i)
    print(len(buf))

def main():
    X = input()  # type: str
    solve(X)
    return

main()
