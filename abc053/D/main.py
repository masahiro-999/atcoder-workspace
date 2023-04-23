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



def solve(N: int, A: "List[int]"):
    c = Counter(A)
    a = N-len(c)
    if a%2 == 0:
        print(len(c))
    else:
        print(len(c)-1)


def main():
    N = ii()  # type: int
    A = li()  # type: "List[int]"
    solve(N, A)
    return

main()
