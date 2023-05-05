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



def solve(N: int, A: "List[int]", B: "List[int]"):
    ab = [(i, a+b) for i,a,b in zip(range(N),A,B)]

    ab.sort(key=lambda x: x[1],reverse=True)

    turn_a = True
    ans = 0
    for i,_ in ab:
        if turn_a:
            ans += A[i]
        else:
            ans -= B[i]
        turn_a = not turn_a  

    print(ans)

def main():
    N = ii()  # type: int
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = mi()
    solve(N, A, B)
    return

main()
