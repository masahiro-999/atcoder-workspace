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

from itertools import accumulate

def solve(N: int, K: int, S: str):
    d = []
    c = 1
    if S[0] == "0":
        d.append(0)
    for i in range(1,N):
        if S[i-1] == S[i]:
            c += 1
        else:
            d.append(c)
            c = 1
    d.append(c)
    if S[-1] == "0":
        d.append(0)

    dsum = [0] + list(accumulate(d))

    w = 2*K+1
    if len(dsum) <= w:
        ans = N
    else:
        ans = 0
        i = 0
        for i in range(0, len(dsum) - w +1,2):
            s = dsum[i+w] - dsum[i]
            ans = max(ans, s)
    print(ans)
    
def main():
    N,K = mi()  # type: int
    S = input()  # type: str
    solve(N, K, S)
    return

main()
