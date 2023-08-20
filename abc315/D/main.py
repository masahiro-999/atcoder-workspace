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


def solve(H,W,C):
    row_active = set(range(H))
    col_active = set(range(W))
    row = [Counter(r) for r in C]
    col = [Counter([C[i][j] for i in range(H)]) for j in range(W)]
    row_kind = [len(x) for x in row]
    col_kind = [len(x) for x in col]
    row_size = [W] * H
    col_size = [H] * W
    while True:
        row_deleting = []
        col_deleting = []
        for i in row_active:
            if row_kind[i] == 1 and row_size[i] > 1:
                row_kind[i] = 0
                row_deleting.append(i)
        for j in col_active:
            if col_kind[j] == 1 and col_size[j] > 1:
                col_kind[j] = 0
                col_deleting.append(j)
        for i in row_deleting:
            row_active.remove(i)
            for j in col_active:
                col_size[j] -= 1
                del_word = C[i][j]
                col[j][del_word] -= 1
                if col[j][del_word] == 0:
                    col_kind[j] -= 1
        for j in col_deleting:
            col_active.remove(j)
            for i in row_active:
                row_size[i] -= 1
                del_word = C[i][j]
                row[i][del_word] -= 1
                if row[i][del_word] == 0:
                    row_kind[i] -= 1

        if row_deleting == [] and col_deleting ==[]:
            break

    ans = 0
    for i in row_active:
        ans += sum(row[i].values())
    print(ans)

def main():
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    C = [input() for _ in range(H)]
    
    solve(H,W,C)
    return

main()
