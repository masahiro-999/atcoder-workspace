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



def solve(N: int, a: "List[int]"):
    ans = "second"
    for i in a:
        if i %2 ==1:
            ans = "first"
            break
    print(ans)

def main():
    N = ii()  # type: int
    a = [ii() for _ in range(N)]  # type: "List[int]"
    solve(N, a)
    return

main()
