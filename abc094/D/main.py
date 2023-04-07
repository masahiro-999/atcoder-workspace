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



def solve(n: int, a: "List[int]"):
    a.sort()
    x = a[-1]
    b = a[:-1]
    b.sort(key=lambda i:min(i,x-i))
    y = b[-1]
    print(x,y)

def main():
    n = ii()  # type: int
    a = li()
    solve(n, a)
    return

main()
