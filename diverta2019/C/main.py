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

def count(s):
    nab = 0
    for i in range(len(s)-1):
        if s[i:i+2] == "AB":
            nab += 1
    if s[-1] == "A":
        a = 1
    else:
        a = 0
    if s[0] == "B":
        b = 1
    else:
        b = 0
    if a and b:
        ab = 1
        a = 0
        b = 0
    else:
        ab = 0
    return nab, ab, a, b

def solve(N: int, s: "List[str]"):
    sum_nab = 0
    sum_ab = 0
    sum_a = 0
    sum_b = 0
    for i in s:
        nab, ab, a, b = count(i)
        sum_nab += nab
        sum_ab += ab
        sum_a += a
        sum_b += b
    if sum_ab == 0:
        ans = sum_nab + min(sum_a,sum_b)
    else:
        if sum_a + sum_b > 0:
            ans = sum_nab + min(sum_a,sum_b) + sum_ab
        else:
            ans = sum_nab + sum_ab - 1

    print(ans)

def main():
    N = ii()  # type: int
    s = [input() for _ in range(N)]  # type: "List[str]"
    solve(N, s)
    return

main()
