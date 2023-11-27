import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect
from heapq import heapify, heappop, heappush
from random import randrange

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

valuemax = 10
def create_sample(n,m):
    a = [randrange(-valuemax,valuemax+1) for _ in range(n+1)]
    a[n] = randrange(1,valuemax)
    if randrange(0,2) == 0:
        a[n] = -a[n]
    b = [randrange(-valuemax,valuemax+1) for _ in range(m+1)]
    b[m] = randrange(1,valuemax)
    if randrange(0,2) == 0:
        b[m] = -b[m]

    c = [0]*(n+m+1)
    for i in range(n+1):
        for j in range(m+1):
            c[i+j] += a[i]*b[j]
    
    f = open("in_3.txt", "w")
    f.write(f'{n} {m}\n')
    f.write(" ".join(map(str,a))+"\n")
    f.write(" ".join(map(str,c))+"\n")
    f.close()
    f = open("out_3.txt", "w")
    f.write(" ".join(map(str,b))+"\n")
    
def solve(N: int, M: int, A: "List[int]", C: "List[int]"):
    def get_ab(n):
        for i in range(N+1):
            if 0 <= n-i <= M:    
                yield(i, n-i)

    def get_b(n):
        ab_list = list(get_ab(n))
        a_list = [a for a,b in get_ab(n)]
        b_list = [b for a,b in get_ab(n)]
        min_b = min(b_list)
        ab_min_b = [(a,b) for a,b in ab_list if b == min_b]
        ab_not_min_b = [(a,b) for a,b in ab_list if b != min_b]

        ret = C[n] 
        for a,b in ab_not_min_b:
            ret -= A[a]*B[b]
        ret //= A[ab_min_b[0][0]]        
        return ret

    B = [0]*(M+1)
    for i in range(M+1):
        b = get_b(N+M-i)
        B[M-i] = b


    print(*B)

    
def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N + 1)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N + M + 1)]  # type: "List[int]"
    solve(N, M, A, C)
    return

# create_sample(2,3)
main()
