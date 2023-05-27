import sys
from collections import deque, Counter, defaultdict
from itertools import product, accumulate, combinations
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1



def solve(N: int, M: int, a_list: "List[List[int]]"):
    c = {}
    for x in combinations(range(1,N+1), 2):
        c[x] = True
    for i in range(M):
        for j in range(N-1):
            x = a_list[i][j]
            y = a_list[i][j+1]
            if x > y:
                x,y = y,x
            c[(x,y)]= False
    ans = 0
    for k,v in c.items():
        if v == True:
            ans += 1
    
    print(ans)



def main():
    N, M = mi()  # type: int
    a = [li() for _ in range(M)]  # type: "List[List[int]]"
    solve(N, M, a)
    return

main()
