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


def solve(N: int, M: int, S: "List[str]"):
    def go_next(pos,d):
        nonlocal ans
        (i,j) = pos
        while S[i][j] == ".":
            ans.add((i,j))
            pi = i
            pj = j
            i = i + dir[d][0]
            j = j + dir[d][1]
        return(pi,pj)

    def bfs(pos):
        q = deque()
        visited = defaultdict(bool)
        q.append(pos)
        visited[pos] = True
        while q:
            pos = q.popleft()
            for d in range(4):
                next_pos = go_next(pos, d)
                if pos != next_pos and visited[next_pos] == False:
                    visited[next_pos] = True
                    q.append(next_pos)

    ans = set()                
    dir =[(-1,0),(0,-1),(1,0),(0,1)]
    bfs((1,1))
    print(len(ans))                  

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, M, S)
    return

main()
