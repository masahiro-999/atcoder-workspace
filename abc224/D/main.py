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


def solve(M: int, u_list: "List[int]", v_list: "List[int]", p: "List[int]"):
    def bfs():
        current_p = [1,2,3,4,5,6,7,8] # 1-8の数字がいる点の番号　index0が1の位置
        if current_p == p:
            return 0
        free = 9 # 9が空き
        count = 0
        q = deque()
        q.append((current_p, free, count))
        visited = set()
        visited.add(tuple(current_p))
        while q:
            current_p, free, count = q.popleft()
            for next_free in d[free]:
                i = current_p.index(next_free)
                next_p = current_p[:]
                next_p[i] = free
                if tuple(next_p) in visited:
                    continue
                if next_p == p:
                    return count + 1
                q.append((next_p, next_free, count + 1))
                visited.add(tuple(next_p))
        return -1
    
    d = defaultdict(list)
    for u,v in zip(u_list, v_list):
        d[u].append(v)
        d[v].append(u)

    ans = bfs()
    print(ans)

def main():
    M = int(next(tokens))  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    p = [int(next(tokens)) for _ in range(8)]  # type: "List[int]"
    solve(M, u, v, p)
    return

main()
