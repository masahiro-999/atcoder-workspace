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



def solve(s: str):
    num_a = 0
    c = 0
    i = 0
    while i < len(s):
        if s[i] == "A":
            num_a += 1
            i+= 1
            continue
        if s[i:i+2]=="BC":
            c += num_a
            i+= 2
            continue
        else:
            num_a = 0
            i+=1
    print(c)

def main():
    s = input()  # type: str
    solve(s)
    return

main()
