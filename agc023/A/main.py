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


def solve(N: int, A: "List[int]"):
    d = [0]*(N+1)
    for i in range(N):
        d[i+1] = d[i]+A[i]
    c = Counter(d)
    ans = 0
    for i,val in c.items():
        ans += val*(val-1)//2
    print(ans)

def main():
    N = ii()  # type: int
    A = li()  # type: "List[int]"
    solve(N, A)
    return

main()
