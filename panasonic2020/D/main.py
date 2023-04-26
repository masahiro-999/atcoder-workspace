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



def solve(N: int):
    def getstr(headstr):
        i=ord("a")
        while chr(i) in headstr:
            i += 1
        s = set(headstr)
        s.add(chr(i))
        ret = []
        for s1 in s:
            ret.append(headstr+s1)
        return ret
    
    q = deque()

    q.append("a")

    while q:
        a = q.popleft()
        if len(a) == N:
            print(a)
        else:
            for str in getstr(a):
                q.append(str)

def main():
    N = ii()  # type: int
    solve(N)
    return

main()
