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



def solve(N: int, S: str):
    ans = 0
    for i in range(N):
        s1 = S[:i]
        s2 = S[i:]
        set1 = set([x for x in s1])
        set2 = set([x for x in s2])
        ans = max(ans, len(set1 & set2))

    print(ans)
    
def main():
    N = ii()  # type: int
    S = input()  # type: str
    solve(N, S)
    return

main()
