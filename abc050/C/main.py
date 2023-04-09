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


MOD = 1000000007

def solve(N: int, A: "List[int]"):
    ans = 0
    A.sort()
    if N %2 ==1:
        if A[0] != 0:
            return 0
        else:
            A = A[1:]

    c = Counter(A)
    for i,v in c.items():
        if v != 2:
            return 0
        
    return 2**(len(c)) % MOD

def main():
    N = ii()  # type: int
    A = li()
    ans = solve(N, A)
    print(ans)
    return

main()
