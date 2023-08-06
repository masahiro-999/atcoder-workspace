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

from dataclasses import dataclass

@dataclass
class Board:
    H: int
    W: int
    S: list

    def get_neighbor_pos(self, pos):
        i,j = pos
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni = i + di
            nj = j + dj
            if 0<= ni < self.H and 0 <= nj < self.W:
                yield (ni,nj)
    def get(self, pos):
        i,j = pos
        return self.S[i][j]

def solve(H: int, W: int, S: "List[str]"):
    
    s = ["s","n","u","k","e"]
    visited = defaultdict(bool)

    board = Board(H,W,S)

    def dfs(pos,d):
        if pos == (H-1,W-1):
            return True
        for next_pos in board.get_neighbor_pos(pos):
            if not visited[next_pos] and board.get(next_pos) == s[(d+1)%5]:
                visited[next_pos] = True
                if dfs(next_pos, d+1):
                    return True
        return False

    if dfs((0,0),0):
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
