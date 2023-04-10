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



def solve(N: int, H: int, a: "List[int]", b: "List[int]"):
    maxa = max(a)
    d = 0
    b.sort(reverse=True)
    b = filter(lambda x: x >maxa, b)
    ans = 0
    for b1 in b:
        d += b1
        ans += 1
        if d >= H:
            break
    if d < H:
        ans += (H-d+maxa-1)//maxa
    print(ans)

def main():
    N, H = mi()  # type: int
    a = [0]*N
    b = [0]*N
    for i in range(N):
        a1, b1 = li()
        a[i] = a1
        b[i] = b1
    solve(N, H, a, b)
    return

main()
