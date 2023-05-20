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

def f(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3*x+1

def solve(s: int):
    a = set()
    ans = 1
    while s not in a:
        ans += 1
        a.add(s)
        s = f(s)
    print(ans)
    
def main():
    s = ii()  # type: int
    solve(s)
    return

main()
