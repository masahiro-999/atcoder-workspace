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


def solve(N: int, M: int, A: "List[int]", B: "List[int]", K: int, C: "List[int]", D: "List[int]"):
    
    def count_satisfied_conditions(cd_bit):
        n_ball = Counter()
        for i in range(K):
            if cd_bit & (1<<i):
                n_ball[C[i]] += 1
            else:
                n_ball[D[i]] += 1
        ret = 0
        for a,b in ab:
            if n_ball[a]>0 and n_ball[b]>0:
                ret += 1
        return ret


    # Ci,Diに含まれない番号を参照している条件を除く
    #　Ai,Biがいずれもset_cdに含まれているものだけにする
    set_cd = set(C)|set(D)

    ab = [(a,b) for a,b in zip(A,B) if a in set_cd and b in set_cd]

    ans = 0
    for i in range(1<<16):
        ans = max(ans, count_satisfied_conditions(i))
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    K = int(next(tokens))  # type: int
    C = [int()] * (K)  # type: "List[int]"
    D = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, A, B, K, C, D)
    return

main()
