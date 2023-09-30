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

from enum import Enum
from dataclasses import dataclass

bt = Enum("board_type",["AH","HW","B"])

@dataclass(slots=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i+other.i,self.j+other.j)

@dataclass
class Board:
    H: int
    W: int
    def __post_init__(self):
        self.board = [[0]*self.W for _ in range(self.H)]

    def get(self, pos):
        if 0<= pos.i < self.H and 0 <= pos.j < self.W:
            return self.board[pos.i][pos.j]
        else:
            # 範囲外は置かれた状態
            return True

    def put(self, pos, value = True):
        self.board[pos.i][pos.j] = value

    def can_put(self, t : bt, pos: Pos):
        if self.get(pos):
            return False
        if t == bt.AH:
            if self.get(pos+Pos(1,0)):
                return False
        elif t == bt.HW:
            if self.get(pos+Pos(0,1)):
                return False
        return True

    def put_board(self, t: bt, pos: Pos):
        if not self.can_put(t, pos):
            return False
        self.put(pos)
        if t == bt.AH:
            self.put(pos+Pos(1,0))
        elif t == bt.HW:
            self.put(pos+Pos(0,1))
        return True

    def remove_board(self, t: bt, pos: Pos):
        self.put(pos, False)
        if t == bt.AH:
            self.put(pos+Pos(1,0), False)
        elif t == bt.HW:
            self.put(pos+Pos(0,1), False)
        return True

    def nextpos(self):
        for i in range(self.H):
            for j in range(self.W):
                if not self.get(Pos(i,j)):
                    return Pos(i,j)
        return None

def solve(H: int, W: int, A: int, B: int):

    board = Board(H,W)
    ans = 0
    def dfs(pos: Pos,a,b):
        nonlocal ans
        if a == 0 and b == 0:
            ans += 1
            return
        for t in bt:
            if t == bt.B:
                if b == 0:
                    continue
                else:
                    next_a = a
                    next_b = b - 1
            else:
                if a == 0:
                    continue
                else:
                    next_a = a - 1
                    next_b = b
            if board.put_board(t,pos):
                # tが置けた場合
                next_pos = board.nextpos()
                dfs(next_pos, next_a, next_b)
                board.remove_board(t,pos)
    dfs(Pos(0,0), A, B)
    print(ans)

def main():
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(H, W, A, B)
    return

main()
