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



def solve(K: int, T: int, a: "List[int]"):
    a.sort(reverse=True)
    maxa = a[0]

    ans = max(0,maxa - (K-maxa) -1)

    print(ans)


def main():
    K, T = mi()  # type: int
    a = li()
    solve(K, T, a)
    return

main()
