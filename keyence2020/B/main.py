import sys
from collections import deque, Counter, defaultdict
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1



def solve(N: int, X: "List[int]", L: "List[int]"):
    XL = [(x-l, x+l) for x,l in zip(X, L)]
    XL.sort(key=lambda x: x[1])

    ans = 0
    e_min = -inf
    for s, e in XL:
        if s >= e_min:
            ans += 1
            e_min = e
    print(ans)

def main():
    N = ii()  # type: int
    X = [int()] * (N)  # type: "List[int]"
    L = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i], L[i] = li()
    solve(N, X, L)
    return

main()
