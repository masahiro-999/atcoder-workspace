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

YES = "Yes"
NO = "No"

def solve(N: int, P: int, Q: int, R: int, A: "List[int]"):
    def is_ok(x,w):
        value_y = b[x]+P
        for y in b_table[value_y]:
            if x < y < w:
                value_z = b[y]+Q
                for z in b_table[value_z]:
                    if y < z < w:
                        return True
        return False

    b = list(accumulate([0]+A))

    b_table = defaultdict(list)
    for i,value in enumerate(b):
        b_table[value].append(i)

    acc_values = b_table.keys()
    set_acc_values = set(acc_values)
    PQR = P+Q+R
    xw_list = []
    for i in set_acc_values:
        if i+PQR in set_acc_values:
            xw_list += list(product(b_table[i],b_table[i+PQR]))

    for x,w in xw_list:
        if w < x:
            continue
        if is_ok(x,w):
            print(YES)
            return
    print(NO)
    return

def main():
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q, R, A)
    return

main()
