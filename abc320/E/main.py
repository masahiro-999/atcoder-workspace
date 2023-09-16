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


def solve(N: int, M: int, T: "List[int]", W: "List[int]", S: "List[int]"):
    ans = [0]*N
    person_queue = list(range(N))
    heapify(person_queue)
    time_list = []
    heapify(time_list)
    for t, w, s in sorted(zip(T, W, S)):
        while time_list and t >= time_list[0][0]:
            _, person = heappop(time_list)
            heappush(person_queue, person)
        try:
            person = heappop(person_queue)
        except IndexError:
            continue
        ans[person] += w
        heappush(time_list, (t+s, person))
    print(*ans, sep="\n")

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    T = [int()] * (M)  # type: "List[int]"
    W = [int()] * (M)  # type: "List[int]"
    S = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        T[i] = int(next(tokens))
        W[i] = int(next(tokens))
        S[i] = int(next(tokens))
    solve(N, M, T, W, S)
    return

main()
