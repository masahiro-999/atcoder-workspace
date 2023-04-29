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



def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    d = [(i,0) for i in A] 
    d += [(i,1) for i in B]
    d += [(i,2) for i in C]

    d.sort(key=lambda x: x[0], reverse=True)

    table =[0]*3

    for i,kind in d:
        table[kind] += 1 if kind==2 else table[kind+1]
    ans = table[0]

    print(ans)

def main():
    N = ii()  # type: int
    A = li()  # type: "List[int]"
    B = li()  # type: "List[int]"
    C = li()  # type: "List[int]"
    solve(N, A, B, C)
    return

main()
