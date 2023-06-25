import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
tokens = (i for line in iter(input, "") for i in line.split())

YES = "Yes"
NO = "No"

def solve(H_A: int, W_A: int, A: "List[str]", H_B: int, W_B: int, B: "List[str]", H_X: int, W_X: int, X: "List[str]"):
    def in_area_x(i,j):
        return 0<= i < H_X and 0 <= j < W_X
        
    def copy_to_xx(xx, offset_i, offset_j, T, H, W):
        # xxにTの黒部分をTrueにする。範囲外をTrueにしようとした場合Falseを返す
        for i in range(H):
            for j in range(W):
                if T[i][j] == "#":
                    x_i = i + offset_i
                    x_j = j + offset_j
                    if not in_area_x(x_i, x_j):
                        return False
                    xx[x_i][x_j] = True
        return True

    def check_xx(xx):
        for i in range(H_X):
            for j in range(W_X):
                if (xx[i][j] == True) != (X[i][j]=="#"):
                    return False
        return True

    for offset_a_i in range(-H_A+1,H_X):
        for offset_a_j in range(-W_A+1,W_X):
            xx = [[False]*W_X for _ in range(H_X)]
            if copy_to_xx(xx,offset_a_i, offset_a_j, A, H_A, W_A) == False:
                continue
            for offset_b_i in range(-H_B+1,H_X):
                for offset_b_j in range(-W_B+1,W_X):
                    xx2 = [x[:] for x in xx]
                    if copy_to_xx(xx2,offset_b_i, offset_b_j, B, H_B, W_B) == False:
                        continue
                    if check_xx(xx2):
                        return YES

    return NO

def main():
    H_A = int(next(tokens))  # type: int
    W_A = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(H_A)]  # type: "List[str]"
    H_B = int(next(tokens))  # type: int
    W_B = int(next(tokens))  # type: int
    B = [next(tokens) for _ in range(H_B)]  # type: "List[str]"
    H_X = int(next(tokens))  # type: int
    W_X = int(next(tokens))  # type: int
    X = [next(tokens) for _ in range(H_X)]  # type: "List[str]"
    print(solve(H_A, W_A, A, H_B, W_B, B, H_X, W_X, X))
    return

main()
