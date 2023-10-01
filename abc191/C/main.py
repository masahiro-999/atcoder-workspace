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

from dataclasses import dataclass


@dataclass(slots=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i+other.i,self.j+other.j)
    def rotate(self,dir):
        if dir == 0:
            return Pos(self.i,self.j)
        elif dir == 1:
            return Pos(self.j,3-self.i)
        elif dir == 2:
            return Pos(3-self.i,3-self.j)
        elif dir == 3:
            return Pos(3-self.j,self.i)

    def next_pos(self, dir):
        dirtable = {0:Pos(-1,0), 1:Pos(0,1), 2:Pos(1,0), 3:Pos(0,-1)}
        return self + dirtable[dir%4]

@dataclass
class Board:
    H: int
    W: int
    def __post_init__(self):
        self.board = [[False]*self.W for _ in range(self.H)]
        self.dir = 0
    def load(self, p):
        for i in range(self.H):
            for j in range(self.W):
                if p[i][j] == "#":
                    self.put(Pos(i,j))

    def goto_start_pos(self):
        for p in self.iterate_all_pos():
            if self.get(p):
                self.p = p
                break
        self.dir = 1
        return (self.p,self.dir)

    def go(self):
        while True:
            # print(self.p,self.dir)
            p = self.p.next_pos(self.dir)
            if not self.get(p):
                # 直進できない
                self.dir = (self.dir+1)%4
                break
            # 進む
            self.p = p
            p = self.p.next_pos((self.dir-1)%4)
            if self.get(p):
                # 左に曲がる
                self.dir = (self.dir-1)%4
                break
        return(self.p,self.dir)

    def get(self, pos):
        return self.board[pos.i][pos.j]

    def put(self, pos, value = True):
            self.board[pos.i][pos.j] = value

    def is_all_filed(self):
        return self.H*self.W == sum([sum(self.board[i]) for i in range(self.H)])

    def d_pos_range(self,mi,mx):
        return (-mi, 3-mx+1)

    def iterate_all_pos(self):
        for i in range(self.H):
            for j in range(self.W):
                yield Pos(i,j)


def solve(H,W,s):
    b = Board(H,W)
    b.load(s)
    ans = 1
    start_p, start_dir = b.goto_start_pos()
    while (start_p, start_dir) != b.go():
        ans += 1
    print(ans)

def main():
    H = int(next(tokens))
    W = int(next(tokens))
    s = [input() for _ in range(H)]
    solve(H,W,s)
    return

main()
