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

def xor(a):
    str_a = format(a,'b')
    l = len(str_a)
    ret = 0
    for i in range(l-1):
        p = 1 <<(l-i-1)
        if str_a[i] == "0":
            continue
        if a % 2 == 0:
            ret += p 
    if a%4 in [1,2]:
        ret += 1
    return ret



def solve(A: int, B: int):
    ans = xor(A-1) ^ xor(B)
    print(ans)

def main():
    A,B = mi()  # type: int
    solve(A, B)
    return

main()
