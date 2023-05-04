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



def solve(H: int, W: int, A: int, B: int):
    ans = ""
    s0 = "1"*A+"0"*(W-A)+"\n"
    s1 = "0"*A+"1"*(W-A)+"\n"
    ans += s0*B
    ans += s1*(H-B)
    print(ans)

def main():
    H,W,A,B = mi()  # type: int
    solve(H, W, A, B)
    return

main()
