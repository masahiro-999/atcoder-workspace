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

choice = []

def create_choice(n_list, n_set):
    if n_set == set():
        choice.append(n_list)
        return
    tmp = n_set.copy()
    for i in n_set:
        tmp.remove(i)   
        create_choice(n_list + [i], tmp)
        tmp.add(i)

def is_gakkari(a_value, open_flag):
    x = [a for a, flag in zip(a_value, open_flag) if flag]
    return len (x) ==2 and x[0] == x[1]

def solve(a):
    def open_pos(p):
        i,j = (p-1)//3, (p-1)%3
        open_flag[i][j] = True
        return


    def check(p):
        nonlocal num_open_row, num_open_col, num_open_ij, num_open_ji
        i,j = (p-1)//3, (p-1)%3
        num_open_row[i] += 1
        num_open_col[j] += 1
        if i == j:
            num_open_ij += 1
        if i == 2-j:
            num_open_ji += 1
        if num_open_row[i] == 2 and is_gakkari(a[i], open_flag[i]):
            return True
        if num_open_col[j] == 2 and is_gakkari([a[i][j] for i in range(3)], [open_flag[i][j] for i in range(3)]):
            return True
        if i == j and num_open_ij == 2 and is_gakkari([a[ij][ij] for ij in range(3)], [open_flag[ij][ij] for ij in range(3)]):
            return True
        if i == 2-j and num_open_ji == 2 and is_gakkari([a[ji][2-ji] for ji in range(3)], [open_flag[ji][2-ji] for ji in range(3)]):
            return True
        return False
            
    create_choice([], set(range(1,10)))
    c_gakkari = 0
    for c_list in choice:
        open_flag = [[False] * 3 for _ in range(3)]
        num_open_row = [0] * 3
        num_open_col = [0] * 3
        num_open_ji = 0
        num_open_ij = 0
        for c in c_list:
            open_pos(c)
            if check(c):
                c_gakkari += 1
                break
    ans = c_gakkari / len(choice)
    print (1-ans)

def main():
    a = [li() for _ in range(3)]
    solve(a)
    return

if __name__ == '__main__':
    main()
