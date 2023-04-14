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



def solve(s: str):
    ss = [i for i in s if i !="x"]
    half = len(ss)//2
    if ss[:half] == ss[-1:-half-1:-1]:
        p = 0
        q = 0
        r = s[::-1]+"X"
        s = s+"X"
        ans = 0
        N = len(s)
        while p < N or q <N:
            if s[p] == r[q]:
                p +=1
                q +=1
                continue
            if s[p] =="x":
                p += 1
                ans += 1
                continue
            if r[q] =="x":
                q += 1
                ans += 1
                continue
            print("error")
    else:
        ans = -1
    print(ans//2)

def main():
    s = input()  # type: str
    solve(s)
    return

main()
