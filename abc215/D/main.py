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

def get_prime_list(num_max):
    prime_table=[1]*(num_max+1)
    prime_table[0] = 0
    prime_table[1] = 0
    for i in range(2, num_max+1):
        k = i*2
        while k <= num_max:
            prime_table[k] = 0
            k += i
    return [i for i in range(2,num_max+1) if prime_table[i]]

def solve(N: int, M: int, A: "List[int]"):

    max_A = max(A)
    A_flat = [0]*(max_A+1)
    for a in A:
        A_flat[a] = 1       

    num_max = 100000

    prime = get_prime_list(num_max)
    prime_in_a = []
    for p in prime:
        n = p
        while n <= max_A:
            if A_flat[n]:
                prime_in_a.append(p)
                break
            n += p

    ans_table = [0]*(M+1)
    ans_table[0] = 1

    for p in prime_in_a:
        n = p
        while n <= M:
            ans_table[n] = 1
            n += p
    ans = [i for i in range(1,M+1) if ans_table[i]==0]
    print(len(ans))
    for a in ans:
        print(a)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)
    return

if __name__ == '__main__':
    main()
