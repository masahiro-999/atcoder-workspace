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



def solve(H: int, W: int, c: "List[List[int]]", A: "List[List[int]]"):
    count = Counter()
    for i in A:
        count += Counter(i)

    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k]+c[k][j])

    ans = 0
    for i,v in count.items():
        if i == -1:
            continue
        ans += c[i][1]*v

    print(ans)

def main():
    H,W = mi()  # type: int
    c = [li() for _ in range(9 + 1)]  # type: "List[List[int]]"
    A = [li() for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, c, A)
    return

main()
