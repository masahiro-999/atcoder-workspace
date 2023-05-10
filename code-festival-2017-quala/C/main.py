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


YES = "Yes"
NO = "No"

def solve(H,W,a):
    c = Counter()
    for i in a:
        c.update(i)

    single = 0
    if H%2 == 1 and W%2 == 1:
        single = 1

    count_single = 0
    for k,v in c.items():
        if v % 2 == 1:
            count_single += 1

    count_quad = 0
    for k,v in c.items():
        count_quad += v // 4

    if count_single != single:
        print(NO)
        return

    if count_quad >= (H//2)*(W//2):
        print(YES)
    else:
        print(NO)




def main():
    H,W = mi()
    a = [input() for _ in range(H)]
    solve(H,W,a)
    return

main()
