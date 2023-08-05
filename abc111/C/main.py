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


def solve(n: int, v: "List[int]"):
    a = [v[i] for i in range(n) if i % 2 == 0]
    b = [v[i] for i in range(n) if i % 2 == 1]

    counta = Counter(a)
    countb = Counter(b)

    common_a_val, common_a_num = counta.most_common()[0]
    common_b_val, common_b_num = countb.most_common()[0]

    if common_a_val != common_b_val:
        ans = n//2 - common_a_num + n//2 - common_b_num
    else:
        if len(countb.most_common()) >= 2:
            ans1 = n//2 - common_a_num + n//2 - countb.most_common()[1][1]
        else:
            ans1 = n//2 - common_a_num + n//2
        if len(counta.most_common()) >= 2:
            ans2 = n//2 - common_b_num + n//2 - counta.most_common()[1][1]
        else:
            ans2 = n//2 - common_b_num + n//2
        ans = min(ans1, ans2)
    print(ans)

def main():
    n = int(next(tokens))  # type: int
    v = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, v)
    return

main()
