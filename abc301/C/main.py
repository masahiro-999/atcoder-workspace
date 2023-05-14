import sys
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1


YES = "Yes"
NO = "No"

def solve(S: str, T: str):
    s = list(S)
    t = list(T)
    s.sort()
    t.sort()
    s_at = 0
    for i in range(len(s)):
        if s[i] != "@":
            s_at = i
            s = s[i:]
            break
    else:
        s_at = len(s)
        s = ""

    for i in range(len(t)):
        if t[i] != "@":
            t_at = i
            t = t[i:]
            break
    else:
        t_at = len(t)
        t = ""

    ans = YES
    a = 0
    b = 0
    s_at1 = 0
    t_at1 = 0
    while True:
        if a == len(s) and b == len(t) and s_at-s_at1 == t_at-t_at1:
            break            
        if a < len(s) and b < len(t) and s[a] == t[b]:
            a += 1
            b += 1
            continue
        if a < len(s) and s[a] in ["a","t","c","o","d","e","r"] and t_at > t_at1:
            a += 1
            t_at1 += 1
            continue
        if b < len(t) and t[b] in ["a","t","c","o","d","e","r"] and s_at > s_at1:
            b += 1
            s_at1 +=1
            continue
        print(NO)
        return
    
    print(YES)

def main():
    S = input()  # type: str
    T = input()  # type: str
    solve(S, T)
    return

main()
