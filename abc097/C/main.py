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



def solve(s: str, K: int):
    s_list = list(set(list(s)))
    s_list.sort()
    mx_len = len(s)
    def dfs(ss,c):
        if len(ss)> mx_len:
            return (ss,c)
        if ss not in s:
            return (ss,c)
        c -= 1
        if c == 0:
            return (ss, c)
        for a in s_list:
            ans,c = dfs(ss+a, c)
            if c == 0:
                return (ans, c)
        return (ss, c)
    ans,c = dfs("",K+1)
    print(ans)

def main():
    s = input()  # type: str
    K = ii()  # type: int
    solve(s, K)
    return

main()
