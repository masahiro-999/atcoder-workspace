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

def is_even_str(s):
    n = len(s)
    if n % 2 == 1:
        return False
    return s[:n//2] == s[n//2:]

def solve(S: str):
    for i in range(len(S)-1, 1, -1):
        if is_even_str(S[:i]):
            return i
    return 0

def main():
    S = input()  # type: str
    print(solve(S))
    return

main()
