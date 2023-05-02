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


def split(S,bits):
    ret = []
    s = 0
    p = 1
    while bits:
        if bits & 1:
            ret.append(int(S[s:p]))
            s = p
        p += 1
        bits = bits >> 1
    ret.append(int(S[s:]))
    return ret

def solve(S: int):
    l = len(S)-1
    s = 0
    for i in range(2**l):
        s_list = split(S,i)
        # if len(s_list)==1:
        #     sum += s_list[0]
        # else:
        s += sum(s_list)
    print(s)

def main():
    S = input()  # type: int
    solve(S)
    return

main()
