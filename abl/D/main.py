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

class SegTree:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
    def add(self,k,x):
        k += self.num
        self.tree[k] += x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    def update(self,k,x):
        k += self.num
        self.tree[k] = x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    def query(self,l,r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res

def solve(N: int, K: int, A: "List[int]"):
    mx_a = max(A)
    st = SegTree([0]*(mx_a+1), max, 0)
    for a in A:
        mx = st.query(max(0,a-K),min(mx_a+1,a+K+1))
        st.update(a,mx+1)
    ans = st.query(0,mx_a+1)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)
    return

main()
