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

def ask(i):
  print(i,flush=True)
  s = input()
  if s == 'Vacant':
    exit()
  return s == 'Female'

def solve(N: str):
    base = ask(0)
    s = 0
    e = N
    while True:
        h = (s+e)//2
        ans = ask(h)

        if (h%2 ==0) == (ans==base):
            s = h
        else:
            e = h

def main():
    N = ii()
    solve(N)
    return

main()
