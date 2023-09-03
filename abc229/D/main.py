import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect, bisect_left, bisect_right
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

def solve1(S: str, K: int):
    #先頭からの.の数
    acc_s_dot = [0] + list(accumulate([1 if s == '.' else 0 for s in S]))
    
    # acc_s_dot[l] - acc_s_dot[r] =Kとなる最大のrを求める
    # 尺取り法
    l = 0
    r = 0
    ans = 0
    while l < len(acc_s_dot):
        while r < len(acc_s_dot) and acc_s_dot[r] - acc_s_dot[l] <= K:
            ans = max(ans, r - l)
            r += 1
        l += 1
    print(ans)
    return ans

def solve(S: str, K: int):
    #先頭からの.の数
    acc_s_dot = [0] + list(accumulate([1 if s == '.' else 0 for s in S]))
    
    # acc_s_dot[l] - acc_s_dot[r] =Kとなる最大のrを求める
    # 二分探査で求める
    def f(start, l):
        if l == len(acc_s_dot):
            return False
        return acc_s_dot[l] - acc_s_dot[start] <= K
    
    ans = 0
    for start in range(len(acc_s_dot)):
        l = start
        r = len(acc_s_dot)
        while r - l > 1:
            m = (l + r) // 2
            if f(start, m):
                l = m
            else:
                r = m
        ans = max(ans, l - start)
    print(ans)
    return ans



def main():
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(S, K)
    return

if __name__ == '__main__':
    main()
