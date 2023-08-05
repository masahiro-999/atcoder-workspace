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


def solve(N: int, P: int):
    def div_n(p,x):
        c = 0
        while p % x == 0:
            p = p // x
            c += 1
        return (p,c)

    num_max = 1000000
    prime_table=[1]*(num_max+1)
    prime_table[0] = 0
    prime_table[1] = 0
    for i in range(2, num_max+1):
        k = i*2
        while k <= num_max:
            prime_table[k] = 0
            k += i
    p_list = [x for x in range(num_max) if prime_table[x]>0]

    c = Counter()

    for i in p_list:
        P,n = div_n(P,i)
        c[i] = n
    if P > 1:
        c[P] = 1
    c =[k**(v//N) for k,v in c.items() if v>=N]
    ans = reduce(lambda x,y:x*y, c, 1)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve(N, P)
    return

main()
