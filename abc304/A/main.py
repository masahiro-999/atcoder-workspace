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



def solve(N: int, S: "List[str]", A: "List[int]"):
    mina = inf
    for i in range(N):
        if mina > A[i]:
            mina = A[i]
            start = i
    for i in range(N):
        print(S[(start+i)%N])

def main():
    n = ii()  # type: int
    S = [str()] * (n)  # type: "List[str]"
    A = [int()] * (n)  # type: "List[int]"
    for i in range(n):
        S[i], a = input().split()
        A[i] = int(a)
    solve(n, S, A)
    return

main()
