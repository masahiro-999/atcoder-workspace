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


YES = "Yes"
NO = "No"

def solve(N: int, a: "List[int]", b: "List[int]"):
    n = sum(b) - sum(a)
    c1 = 0
    c2 = 0
    for a1,b1 in zip(a,b):
        if a1 > b1:
            c1 += a1-b1
        elif a1 < b1:
            c2 += (b1-a1)//2
    if n >= c1+c2:
        print(YES)
    else:
        print(NO)
                

def main():
    N = ii()  # type: int
    a = li()  # type: "List[int]"
    b = li()  # type: "List[int]"
    solve(N, a, b)
    return

main()
