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



def solve(N: int, A: "List[int]", B: "List[int]"):
    g = [[] for _ in range(N)]

    for i,a,b in zip(range(len(A)),A,B):
        a -= 1
        b -= 1
        g[a].append((b,i))
        g[b].append((a,i))
    
    c = [0]*(N-1)
    def set_color(x, prev):
        n_c = 1
        for next,i in g[x]:
            if i !=prev:
                if prev != -1 and n_c == c[prev]:
                    n_c += 1
                c[i] = n_c
                n_c += 1
                set_color(next, i)
    set_color(A[0]-1,-1)
    K = max(c)
    print(K)
    print(*c, sep="\n")

def main():
    N = ii()  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i],b[i] = mi()
    solve(N, a, b)
    return

main()
