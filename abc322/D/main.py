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
@dataclass
class Board:
    H: int
    W: int
    def __post_init__(self):
        self.board = [[False]*self.W for _ in range(self.H)]
    def load(self, p):
        mi_i = 4
        mx_i = 0
        mi_j = 4
        mx_j = 0
        for i in range(self.H):
            for j in range(self.W):
                if p[i][j] == "#":
                    mi_i = min(mi_i,i)
                    mx_i = max(mx_i,i)
                    mi_j = min(mi_j,j)
                    mx_j = max(mx_j,j)
                    self.put(Pos(i,j))
        self.d_pos_i = (-mi_i, self.H-mx_i)
        self.d_pos_j = (-mi_j, self.W-mx_j)

    def can_put_board(self, pos_d, dir, b):
        # b をdi,djずらし,dir回転したものを置けるか
        for p0 in self.iterate_all_pos():
            target_p = (p0+pos_d).rotate(dir)
            if b.get(p0) and self.get(target_p) == True:
                return False
        return True

    def put_board(self, pos_d, dir, b, value = True):
        # b をdi,djだけずらし,dir回転したものを置く
        for p0 in self.iterate_all_pos():
            target_p = (p0+pos_d).rotate(dir)
            if b.get(p0):
                self.put(target_p,value)
        return True

    def get(self, pos):
        return self.board[pos.i][pos.j]

    def put(self, pos, value = True):
            self.board[pos.i][pos.j] = value

    def is_all_filed(self):
        return self.H*self.W == sum([sum(self.board[i]) for i in range(self.H)])

    def d_pos_range(self,mi,mx):
        return (-mi, 3-mx+1)

    def iterate_d_pos(self):
        for di in range(self.d_pos_i[0],self.d_pos_i[1]):
            for dj in range(self.d_pos_j[0],self.d_pos_j[1]):
                yield Pos(di,dj)

    def iterate_all_pos(self):
        for i in range(self.H):
            for j in range(self.W):
                yield Pos(i,j)

def solve(p):

    def dfs(i,board):
        if i == 3:
            return True
        for p in tmplate[i].iterate_d_pos():
            for dir in range(4):
                if board.can_put_board(p,dir,tmplate[i]):
                    board.put_board(p,dir,tmplate[i])
                    # print(i,p,dir)
                    if dfs(i+1,board):
                        return True
                    board.put_board(p,dir,tmplate[i],False)
        return False

    tmplate = [Board(4,4) for _ in range(3)]
    for i in range(3):
        tmplate[i].load(p[i])

    board = Board(4,4)
    ans = dfs(0,board)
    if ans:
        ans = board.is_all_filed()
    print("Yes" if ans else "No")

def main():
    p =[[input() for _ in range(4)] for _ in range(3)]
    solve(p)
    return

if __name__ == '__main__':
    main()
