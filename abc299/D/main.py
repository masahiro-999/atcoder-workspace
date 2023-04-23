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



def solve(N: int):
    e = N
    s = 1
    while True:
        if e-s <= 1:
            break
        h = (e+s)//2
        print(f"? {h}", flush=True)
        ret =ii()
        if ret ==0:
            s = h
        else:
            e = h
    print(f'! {s}')

def main():
    N = ii()  # type: int
    solve(N)
    return

main()
