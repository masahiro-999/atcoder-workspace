import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1


YES = "POSSIBLE"
NO = "IMPOSSIBLE"

def solve(N: int, K: int, A: "List[int]"):
    g = A[0]
    maxnum = max(A)
    for i in A[1:]:
        g = math.gcd(g,i)
    
    if K <= maxnum and K % g == 0:
        print(YES)
    else:
        print(NO)

def main():
    N, K = mi()  # type: int
    A = li()
    solve(N, K, A)
    return

main()
