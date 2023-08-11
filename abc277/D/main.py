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

MOD = 1

def solve(N: int, M: int, A: "List[int]"):
    def fill_score(x):
        if score[x] != -1:
            return
        score[x] = x*c[x]
        next_x = (x+1)%M
        if next_x in exist_numbers_set:
            if score[next_x] == -1:
                fill_score(next_x)
            score[x] += score[next_x]
    c = Counter(A)
    exist_numbers = sorted(c.keys())
    exist_numbers_set = set(exist_numbers)
    exist_numbers_low = [x for x in exist_numbers if x < M]
    exist_numbers_high = [x for x in exist_numbers if x >= M]

    score = defaultdict(lambda : -1)
    kireme = -1
    for i,value in enumerate(exist_numbers_low):
        if i != value:
            kireme = i
            break
    if kireme == -1:
        sum_m = sum([i*c[i] for i in range(M)])
        for i in range(M):
            score[i] = sum_m
    else:
        for x in exist_numbers_low[kireme:]+exist_numbers_low[:kireme]:
            fill_score(x)
    for x in exist_numbers_high:
        fill_score(x)

    max_score = max((score.values()))

    ans = sum(A) - max_score
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)
    return

def create_file():
    N = 200000
    M = 200000
    f = open("in_5.txt", "w")
    f.write(f'{N} {M}\n')
    a = [str(i) for i in range(N)]
    f.write(" ".join(a))

# create_file()
main()

