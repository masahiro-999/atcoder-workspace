import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate,permutations,combinations
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

MOD = 998244353

def solve(N: int, K: int, L: "List[int]", R: "List[int]"):
    acc_t = [0]*(N+1)
    acc_t[1] = 1
    for i in range(2,N+1):
            tmp = 0
            for l,r in zip(L,R):
                s = i-r
                t = i-l
                sum_s_t = acc_t[max(0,t)] - acc_t[max(0,s-1)]
                tmp += sum_s_t % MOD
            acc_t[i] = (acc_t[i-1]+tmp)%MOD
    ans = acc_t[N] - acc_t[N-1]
    ans %= MOD
    print(ans)

def solve1(N: int, K: int, L: "List[int]", R: "List[int]"):
    @lru_cache()
    def f(n):
        # if n in num_set:
        #     return 1
        ret = 0
        for s in num_set:
            d = n - s
            if d == 0:
                ret += 1
            elif d > 0:
                ret += f(d)
                ret %= MOD
        return ret            

    num_set = set()
    for l,r in zip(L,R):
        for i in range(l,r+1):
            num_set.add(i)
    ans = f(N-1)
    print(ans)
def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    L = [int()] * (K)  # type: "List[int]"
    R = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, K, L, R)
    return

if __name__ == "__main__":
    main()
