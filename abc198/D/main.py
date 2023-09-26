import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate, permutations
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


def solve(S: "List[str]"):
    def check(p):
        n1 = create_num(p, S[0])
        n2 = create_num(p, S[1])
        n3 = create_num(p, S[2])
        if n1+n2 == n3:
            return n1,n2,n3
        else:
            return None,None,None
    def create_num(p, str):
        n = 0
        for s in str:
            i = char_table[s]
            n *= 10
            n += p[i]
        return n
    def is_top_i_zero(p):
        for i in top_i:
            if p[i] == 0:
                return True
        return False

    # Sに含まれる文字種を数える
    char_set = set()
    for s in S:
        char_set |= set(s)
    kind_of_char = len(char_set)
    if kind_of_char > 10:
        print("UNSOLVABLE")
        return

    char_list =[s for s in char_set]

    char_table = {}
    for i,c in enumerate(char_list):
        char_table [c] = i

    top_i = [char_table[s[0]] for s in S]
    # 全探索
    for p in permutations(range(0,10),kind_of_char):
        if is_top_i_zero(p):
            continue
        n1,n2,n3 = check(p)
        if n1 is not None:
            print(n1)
            print(n2)
            print(n3)
            return
    print("UNSOLVABLE")
    return
        
def main():
    S = [next(tokens) for _ in range(3)]  # type: "List[str]"
    solve(S)
    return

main()
