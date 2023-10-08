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


def solve(N: int, K: int, P: "List[int]", C: "List[int]"):
    def nodes_list(s):
        i = s
        ret = [i]
        while True:
            i = P[i]
            if i ==s:
                return ret
            ret.append(i)

    P = [p-1 for p in P]
    result = [-inf]*N
    for s in range(N):
        if result[s] != -inf:
            continue
        nodes = nodes_list(s)
        cycle = len(nodes)
        for _ in range(cycle):
            score_list = [C[i] for i in nodes+nodes]
            cycle_total = sum(score_list[:cycle])
            if cycle_total < 0 or K < cycle:
                scan_range = range(min(cycle,K))
                subtotal = 0
            else:
                K1 = K % cycle
                scan_range = range(K1+cycle)
                subtotal = cycle_total * (K//cycle-1)
            mx = -inf
            for i in scan_range:
                subtotal += score_list[i]
                mx = max(mx, subtotal)
            result[nodes[0]] = mx
            nodes[:] = nodes[-1:]+nodes[0:-1]
        ans = max(result)
    print(ans)

def main():
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, P, C)
    return

if __name__ == '__main__':
    main()
