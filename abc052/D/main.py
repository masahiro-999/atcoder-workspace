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



def solve(N: int, A: int, B: int, X: "List[int]"):
    sum = 0
    for i in range(1,N):
        sum += min((X[i]-X[i-1])*A, B)

    print(sum)

def main():
    N,A,B = mi()  # type: int
    X = li()  # type: "List[int]"
    solve(N, A, B, X)
    return

main()
