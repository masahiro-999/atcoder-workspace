import sys
from collections import deque, Counter, defaultdict
from itertools import product
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1



def solve(N: int, M: int, ab: "List[int]"):

    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        for next in g[n]:
            dfs(next)

    ans = 0
    for i in range(M):
        g = defaultdict(list)
        for j, (a,b) in enumerate(ab):
            if i != j:
                g[a].append(b)
                g[b].append(a)

        visited = set()
        dfs(1)
        notvisited = set(range(1,N+1))- visited
        if notvisited:
            ans += 1
    print(ans)

def main():
    N,M = mi()  # type: int
    ab = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        ab[i] = li()
    solve(N, M, ab)
    return

main()
