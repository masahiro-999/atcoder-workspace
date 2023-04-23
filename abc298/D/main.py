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


MOD = 998244353

def keta(i):
    count = 0
    while i >0:
        count += 1
        i = i//10
    return count

def main():
    Q = ii()
    s = 1
    keta = 1
    for i in range(Q):
        i = li()
        if i[0] == 1:
            s = s*10 +i[1]
            keta += 1
        elif i[0] == 2:
            keta -= 1
            s = s %(10**keta)
        elif i[0] == 3:
            print(s % MOD)

main()
