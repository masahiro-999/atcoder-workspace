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



def solve(N: int):
    ans = 0
    c = Counter()
    for i in range(1,N+1):
        s = f'{i}'
        c[(int(s[0]),int(s[-1]))] += 1

    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            ans += c[(i,j)] * c[(j,i)]

    print(ans)

def main():
    N = ii()  # type: int
    solve(N)
    return

main()
