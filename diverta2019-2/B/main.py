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

def solve(N: int, x: "List[int]", y: "List[int]"):

    if N == 1:
        print(1)
    else:
        d = []
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                d.append((dx,dy))
        c = Counter(d).most_common(1)
        max_c = c[0][1]

        print(N-max_c)

def main():
    N = ii()  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i], y[i] = mi()
    solve(N, x, y)
    return

main()
