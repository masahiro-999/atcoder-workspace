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



def solve(N: int, a: "List[int]"):
    i = 1
    ans = 0
    used = set()
    while True:
        used.add(i)
        next = a[i-1]
        ans += 1
        if next in used or next == i:
            ans = -1
            break
        if next == 2:
            break
        i = next
    print(ans)

def main():
    N = ii()  # type: int
    a = [ii() for _ in range(N)]  # type: "List[int]"
    solve(N, a)
    return

main()
