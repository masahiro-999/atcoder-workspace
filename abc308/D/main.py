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

MOD = 5
YES = "Yes"
NO = "No"

def solve(H: int, W: int, S: "List[str]"):
    
    s = ["s","n","u","k","e"]
    visited = [[0]*W for _ in range(H)]

    def dfs(i,j,d):
        # set_param('max_unroll_recursion=-1') を実行しないとTLEとなる。
        # 以下のif文をdfsを呼び出す前に移動させれば、上記の対応は不要
        if S[i][j] != s[d%5] or visited[i][j] != 0:
            return False
        if i == H-1 and j == W-1:
            return True
        visited[i][j] = 1
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni = i + di
            nj = j + dj
            if 0<= ni < H and 0 <= nj < W:
                if dfs(ni, nj, d+1):
                    return True
        return False

    if dfs(0,0,0):
        print(YES)
    else:
        print(NO)



def main():
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)
    return

main()
