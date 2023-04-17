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



def solve(K: int):
    if K <10:
        return K
    K -= 9
    prev_buf = [i for i in range(1,10)]
    while True:
        buf = []
        for a in prev_buf:
            tail = a%10
            for i in [-1,0,1]:
                if 0<= tail+i <=9:
                    buf.append(a*10+tail+i)
                    K -= 1
                    if K == 0:
                        return a*10+tail+i
        prev_buf = buf
def main():
    K = ii()  # type: int
    ans = solve(K)
    print(ans)
    return

main()
