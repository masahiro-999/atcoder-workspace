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

ans = inf
def count_one(i):
    count = 0
    while i>0:
        if i & 1:
            count+= 1
        i = i>>1
    return count

def check(N,a,i):
    for n in range(N):
        if (1<<n) & i:
            for x,y in a[n]:
                x -= 1
                if ((1<<x) & i ==0) != (y==0):
                    return False
    return True

def solve(N,a):
    ans = 0
    for i in range(1<<N):
        if check(N,a,i):
            ans = max(ans, count_one(i))

    print(ans)

def main():
    N = ii()
    a = [0]*N
    for i in range(N):
        A = ii()
        a[i] = [li() for _ in range(A)]
    solve(N,a)
    return

main()
