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


MOD = 2

def getsum(b,step):
    i = step+step
    sum = 0
    while i-1 <len(b):
        sum += b[i-1]
        i+= step
    return sum

def solve(N: int, a: "List[int]"):
    b = [0] * N
    for i in range(N,0, -1):
        b[i-1] = (a[i-1] + getsum(b,i))%2

    ans = [i+1 for i,v in enumerate(b) if v>0]
    print(len(ans))
    if len(ans)>0:
        print(*ans)

def main():
    N = ii()  # type: int
    a = li()
    solve(N, a)
    return

main()
