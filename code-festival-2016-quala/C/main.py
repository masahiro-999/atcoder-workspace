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



def solve(s: str, K: int):
    a = [ord(x)-97 for x in s]
    for i in range(len(a)):
        d = 26-a[i]
        if a[i] !=0 and d <=K:
            K-=d
            a[i] = 0
        if K ==0:
            break
    if K >0:
        a[-1] = (a[-1]+K)%26
    ans = "".join([chr(x+97) for x in a])
    print(ans)

def main():
    s = input()  # type: str
    K = ii()  # type: int
    solve(s, K)
    return

main()
