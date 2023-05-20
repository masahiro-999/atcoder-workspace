import sys
from collections import deque, Counter, defaultdict
from itertools import product, accumulate, permutations
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

    for p in permutations(range(N)):
        ans = YES
        for i in range(1,N):
            i1 = p[i-1]
            i2 = p[i]
            if not cmp(S[i1],S[i2]):
                ans = NO
                break
        if ans == YES:
            break
    print(ans)

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


