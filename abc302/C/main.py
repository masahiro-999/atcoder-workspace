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

def cmp(s1,s2):
    count = 0
    for a,b in zip(s1,s2):
        if a!=b :
            count += 1
    return count == 1
    
def solve(N: int, M: int, S: "List[str]"):
    t = [[] for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            if cmp(S[i], S[j]):
                t[i].append(j)
                t[j].append(i)
    st = 0
    count = 0
    for i in range(N):
        if len(t[i])  ==1:
            st += 1
        if len(t[i]) >0:
            count += 1
    if count ==N and st <=2:
        print(YES)
    else:
        print(NO)


def main():
    N, M = mi()  # type: int
    S = [input() for _ in range(N)]  # type: "List[str]"
    solve(N, M, S)
    return

main()


# nice
# rice
# race
# case
# cast
# fast
# fact
# face


