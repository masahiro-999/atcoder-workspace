import sys
from collections import deque, Counter, defaultdict
from itertools import product, accumulate, permutations,combinations
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1

def solve(n: int):
    ans = n*(n-1)//2
    print(ans)

def main():
    N = ii()  # type: int
    solve(N)
    return

main()
