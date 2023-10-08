import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10,isqrt
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

# 素数のリストを作る
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, floor(sqrt(n)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def solve(T, c_list):
    primes_list = primes(isqrt(10**9))

    def check(N):
        x = N
        p_list = []
        for p in primes_list:
            n = 0
            while x % p == 0:
                x //= p
                n += 1
            if n > 0:
                p_list.append((p,n))
        if x > 1:
            p_list.append((x,1))

        return len(p_list)>1
    
    for c in c_list:
        if check(c):
            print(YES)
        else:    
            print(NO)


def main():
    T = int(next(tokens))
    c = [ii() for _ in range(T)]

    solve(T,c)
    return

main()
