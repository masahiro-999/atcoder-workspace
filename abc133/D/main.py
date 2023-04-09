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



def solve(N: int, A: "List[int]"):
    s = sum(A)
    s1 =2*sum([x for i,x in enumerate(A) if i <N and i%2 ==1])
    b = [0] * N
    b[0] = s -s1
    for i in range(1,N):
        b[i] = (A[i-1]-b[i-1]//2)*2
    print(*b)

def main():
    N = ii()  # type: int
    A = li()
    solve(N, A)
    return

main()
