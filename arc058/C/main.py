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



def solve(N: int, K: int, D: "List[int]"):
    keta = len(f'{N}')
    D = map(str,D) 
    dig = set(map(str,range(0,10)))
    dig = list(dig - set(D))
    dig.sort()
    ans = -1
    for j in product(dig, repeat=keta):
        value = int("".join(j))
        if value >=N:
            ans = value
            break
    if ans == -1:
        msb = dig[0]
        if msb == "0":
            msb = dig[1]
        for j in product(dig, repeat=keta):
            value = int(msb+"".join(j))
            if value >=N:
                ans = value
                break

    print(value)

def main():
    N,K = mi()  # type: int
    D = li()  # type: "List[int]"
    solve(N, K, D)
    return

main()
