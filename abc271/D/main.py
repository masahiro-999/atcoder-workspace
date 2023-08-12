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

YES = "Yes"
NO = "No"

def solve(N: int, S: int, A: "List[int]", B: "List[int]"):
    min_list = [min(a,b) for a,b in zip(A,B)]
    c = [abs(a-b) for a,b in zip(A,B)]
    sum_of_min = sum(min_list)
    if sum_of_min > S or sum_of_min + sum(c) < S:
        print(NO)
        return 
    target =  S - sum_of_min
    if target == 0:
        print(YES)
        print("H"*N)
        return
    d = [[[] for _ in range(target+1)] for _ in range(N)]
    d[0][target - c[0]].append(0)
    for i in range(1,N):
        for j in reversed(range(0,target+1)):
            if d[i][j] == []:
                d[i][j] = d[i-1][j][:]
            if j >= c[i] and d[i-1][j-c[i]] == []:
                if d[i-1][j] != [] or j ==target:
                    d[i][j-c[i]] = d[i-1][j][:]
                    d[i][j-c[i]].append(i)
    ans = set(d[N-1][0])
    if not ans:
        print(NO)
        return
    result = ["H" if (A[i]>B[i]) == (i in ans) else "T"  for i in range(N)]
    ret = 0
    for i,w in enumerate(result):
        ret += A[i] if w == "H" else B[i]
    print(YES)
    print("".join(result))
    # print(ret)

def main():
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, S, a, b)
    return

main()
