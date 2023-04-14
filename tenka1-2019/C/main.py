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



def solve(N: int, S: str):

    d1 = [0]*(N+1)
    for i in range(1,N+1):
        d1[i] = d1[i-1]+ (S[i-1]=="#")

    d2 = [0]*(N+1)
    for i in range(N-1,-1,-1):
        d2[i] = d2[i+1]+ (S[i]==".")

    ans = min(map(sum, zip(d1,d2)))
    print(ans)

def main():
    N = ii()  # type: int
    S = input()  # type: str
    solve(N, S)
    return

main()
