import sys
from collections import deque, Counter, defaultdict
from itertools import product
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1

def solve(N: int, A: "List[int]"):
    A.sort()
    q = deque(A)
    r = q.pop()
    l = q.popleft()
    ans = abs(l-r)
    while q:
        next = []
        next.append((abs(q[0]-l), 0, q[0], r))
        next.append((abs(q[0]-r), 0, l, q[0]))
        next.append((abs(q[-1]-l), -1, q[-1], r))
        next.append((abs(q[-1]-r), -1, l, q[-1]))
        next.sort(key=lambda x:x[0], reverse=True)
        ans += next[0][0]
        if next[0][1] ==0:
            q.popleft()
        else:                    
            q.pop()
        l = next[0][2]                    
        r = next[0][3]                    

    print(ans)


def main():
    N = ii()  # type: int
    A =[ii() for _ in range(N)]

    solve(N, A)
    return

main()
