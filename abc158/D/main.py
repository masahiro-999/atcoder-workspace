import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
try:
    from pypyjit import set_param
    set_param('max_unroll_recursion=-1')
except ModuleNotFoundError:
    pass
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())


def solve(s,q,q_list):
    is_forward = True
    top = []
    bottom = []
    for i in q_list:
        if i[0]=="1":
            is_forward = not is_forward
        else:
            # i[0] == 2
            if (i[1] == "1") == is_forward:
                top.append(i[2])
            else:
                bottom.append(i[2])
    ans = "".join(top[::-1]) + s + "".join(bottom)
    if not is_forward:
        ans = ans[::-1]
    print(ans)

def main():
    s = input()
    q = ii()
    q_list = [input().split() for _ in range(q)]
    solve(s,q,q_list)
    return

main()
