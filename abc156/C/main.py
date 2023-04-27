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



def solve(N: int, X: "List[int]"):
    mx = inf
    maxp = max(X)
    for i in range(1,maxp+1):
        sum = 0
        for j in range(N):
            sum += (i-X[j])*(i-X[j])
        mx = min(mx, sum)

    print(mx)

def main():
    N = ii()  # type: int
    X = li()  # type: "List[int]"
    solve(N, X)
    return

main()
