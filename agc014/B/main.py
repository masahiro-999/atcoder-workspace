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


YES = "YES"
NO = "NO"

def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    d = Counter(a+b)
    ans = YES
    for k,v in d.items():
        if v % 2 != 0:
            ans = NO
            break
    print(ans)

def main():
    N,M = mi()  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i],b[i] = mi()
    solve(N, M, a, b)
    return

main()
