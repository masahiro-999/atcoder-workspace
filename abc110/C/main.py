import sys
from collections import deque, Counter
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
    s = Counter(S)
    s1 = [v for i,v in s.items()]
    s1.sort()
    t = Counter(T)    
    t1 = [v for i,v in t.items()]
    t1.sort()

    if s1 == t1:
        print(YES)
    else:
        print(NO)
        
def main():
    S = input()  # type: str
    T = input()  # type: str
    solve(S, T)
    return

main()
