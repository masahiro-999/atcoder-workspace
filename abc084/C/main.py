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



def solve(N: int, C: "List[int]", S: "List[int]", F: "List[int]"):
    
    def get_waittime(C,S,F):
        t = 0
        for i in range(len(C)):
            if t < S[i]:
                t = S[i]
                t += C[i]
            else:
                t = (t + F[i]-1)//F[i] * F[i]
                t += C[i]
        return t


    for i in range(N-1):
        print(get_waittime(C[i:], S[i:], F[i:]))
    print(0)        

def main():
    N = ii()  # type: int
    C = [int()] * (N - 1)  # type: "List[int]"
    S = [int()] * (N - 1)  # type: "List[int]"
    F = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        C[i], S[i], F[i] = li()
    solve(N, C, S, F)
    return

main()
