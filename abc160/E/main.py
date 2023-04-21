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



def solve(X: int, Y: int, A: int, B: int, C: int, p: "List[int]", q: "List[int]", r: "List[int]"):
    p.sort(reverse=True)
    q.sort(reverse=True)
    a = p[:X] + q[:Y] +r
    a.sort(reverse=True)
    print(sum(a[:X+Y]))

def main():
    X,Y,A,B,C = mi()  # type: int
    p = li()  # type: "List[int]"
    q = li()  # type: "List[int]"
    r = li()  # type: "List[int]"
    solve(X, Y, A, B, C, p, q, r)
    return

main()
