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



def solve(N: int, M: int, d):
    d.sort()
    pp = -1
    for i, v in enumerate(d):
        p = v[0]
        if pp != p:
            x = 1
            pp = p
        d[i][3] = x
        x += 1
    d.sort(key = lambda x: x[2])

    for p,_,_,x in d:
        print(f'{p:06d}{x:06d}')

def main():
    N, M = mi()  # type: int
    d = []
    for i in range(M):
        p,y = mi()
        d.append([p,y,i,0])
    solve(N, M, d)
    return

main()
