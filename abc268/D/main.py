import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate, permutations, combinations
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

def create_space_list(l,n):
    def gen_space(space_list,l,n):
        nonlocal result
        if n == 0:
            result.append(space_list[:])
            return
        for i in range(0,l-(n-1)):
            gen_space(space_list+[i+1], l-(i+1), n-1)

    result = []
    gen_space([],l,n)
    return result

def solve(N: int, M: int, S: "List[str]", T: "List[str]"):

    def check_x(x):
        return len(x) >= 3 and x not in T

    t = set(T)

    if N == 1:
        return S[0] if check_x(S[0]) else -1

    l = sum([len(s) for s in S])
    
    for s_list in permutations(S,N):
        n_space = 16 - l
        if n_space < N-1:
            return -1
        else:
            for space_list in create_space_list(n_space,N-1):
                x = s_list[0]
                for s,space in zip(s_list[1:], space_list):
                    x += "_"*space + s
                if x not in t:
                    return x
    return -1

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    T = [next(tokens) for _ in range(M)]  # type: "List[str]"
    print(solve(N, M, S, T))
    return

main()
