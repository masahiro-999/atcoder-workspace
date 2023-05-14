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



def solve(N: int, A: "List[int]"):
    ans = []
    ans.append(A[0])
    prev = A[0]
    for i in A[1:]:
        if abs(i-prev) > 1:
            if i>prev:
                for x in range(prev+1,i):
                    ans.append(x)
            else:
                for x in range(prev-1, i, -1):
                    ans.append(x)
        ans.append(i)
        prev = i

    print(*ans)

def main():
    N = ii()  # type: int
    A = li()
    solve(N, A)
    return

main()
