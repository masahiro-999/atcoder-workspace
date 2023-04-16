import sys
from collections import deque, Counter, defaultdict
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1

def solve(N,Q,q):
    box =[list() for _ in range(N)]
    card =defaultdict(set)
    for i in q:
        if i[0] == 1:
            box[i[2]-1].append(i[1])
            card[i[1]].add(i[2])
        elif i[0] == 2:
            box[i[1]-1].sort()
            print(*box[i[1]-1])
        elif i[0] == 3:
            a = list(card[i[1]])
            a.sort()
            print(*a)



def main():
    N = ii()
    Q = ii()
    q = [li() for _ in range(Q)]
    solve(N,Q,q)
    return

main()
