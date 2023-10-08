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


def solve(H,W,c_pos,d_pos,s):
    def dfs(i,j,c):
        table[i][j] = c
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            ii = i + dx
            jj = j + dy
            if 0 <= ii <H and 0<= jj <W and s[ii][jj]=="." and table[ii][jj] == 0:                
                dfs(ii,jj,c)

    def get_neighber_color(i,j,c):
        ret = set()
        for di in range(-2,3):
            for dj in range(-2,3):
                if not (0<= i+di< H and 0<=j+dj<W):
                    continue
                cc = table[i+di][j+dj]
                if cc!=0 and cc != c:
                    ret.add(cc)
        return ret
    
    def bfs(start,end):
        table_c[start] = 0
        q = deque()
        q.append(start)
        while q:
            p = q.popleft()
            for next_p in g[p]:
                if table_c[next_p] == -1:
                    table_c[next_p] = table_c[p]+1
                    q.append(next_p)
        return table_c[end]
     
    table = [[0]*W for _ in range(H)]
    c = 0
    for i in range(H):
        for j in range(W):
            if s[i][j] == "." and table[i][j] == 0:
                c += 1
                dfs(i,j,c)
    num_c = c
    start_c = table[c_pos[0]-1][c_pos[1]-1]   
    end_c = table[d_pos[0]-1][d_pos[1]-1]   
    g = defaultdict(list)

    for i in range(H):
        for j in range(W):
            c = table[i][j]
            if c != 0:
                c_list = get_neighber_color(i,j,c)
                for a in c_list:
                    g[c].append(a)
                    g[a].append(c)

    table_c = [-1]*(num_c+1)
    ans = bfs(start_c,end_c)
    print(ans)

def main():
    H = int(next(tokens))
    W = int(next(tokens))
    c = li()
    d = li()
    s = [input() for _ in range(H)]
    solve(H,W,c,d,s)
    return

main()
