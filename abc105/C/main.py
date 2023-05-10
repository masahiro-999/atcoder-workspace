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



def solve(N: int):
    if N == 0:
        print("0")
        return
    if N > 0:
        t = False
    else:
        t = True
        N = -N
    ans = ""
    while N >0:
        if N & 1:
            b = "1"
            if t:
                N += 2
        else:
            b = "0"
        t = not t
        N = N >> 1
        ans = b + ans
    print(ans)
    
def main():
    N = ii()  # type: int
    solve(N)
    return

main()
