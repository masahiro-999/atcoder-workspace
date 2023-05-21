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

def solve(N, Q, q_list):
    ans = N
    t = [set() for _ in range(N)]
    for q in q_list:
        if q[0] == 1:
            if len(t[q[1]-1]) == 0:
                ans -= 1
            if len(t[q[2]-1]) == 0:
                ans -= 1
            t[q[1]-1].add(q[2])
            t[q[2]-1].add(q[1])
        else:
            if len(t[q[1]-1]):
                ans += 1
                for i in t[q[1]-1]:
                    t[i-1].remove(q[1])
                    if len(t[i-1]) == 0:
                        ans += 1
                t[q[1]-1] = set()

        print(ans)

def main():
    N,Q = mi()  # type: int
    q = [li() for _ in range(Q)]  # type: int
    solve(N, Q, q)
    return

main()
