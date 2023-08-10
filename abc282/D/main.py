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


def solve(N: int, M: int, U: "List[int]", V: "List[int]"):
    def dfs(i,l):
        nonlocal a,b,ng,pathcount,num_node
        label[i] = l
        num_node += 1
        if l == 0:
            a += 1
        else:
            b += 1
        for next in d[i]:
            pathcount += 1
            if label[next] == -1:
                dfs(next, 1-l)
            else:
                if label[next] == l:
                    ng = True                    

    d = defaultdict(list)
    for u,v in zip(U,V):
        u -= 1
        v -= 1
        d[u].append(v)
        d[v].append(u)
    
    label = [-1]*N
    ans = 0
    ng = False
    nodes = []
    for i in range(0,N):
        if label[i] != -1:
            continue
        a = 0
        b = 0
        pathcount = 0
        num_node = 0
        dfs(i, 0)
        nodes.append(num_node)
        ans += a*b-pathcount//2
    node_acc = list(accumulate(nodes))    
    for i in range(1,len(nodes)):
        ans += node_acc[i-1] * nodes[i]
    if ng:
        ans = 0
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, M, u, v)
    return

main()
