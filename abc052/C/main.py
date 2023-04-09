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


MOD = 1000000007

def devide(n):
    ret = defaultdict(int)
    i = 2
    while n > 1:
        if n % i ==0:
            n //= i
            ret[i] += 1
        else:
            i += 1
    return ret

def solve(N: int):
    t = defaultdict(int)
    for i in range(1,N+1):
        ret = devide(i)
        for k,v in ret.items():
            t[k] += v

    ans = 1
    for i,v in t.items():
        if i == 1:
            continue
        ans = (ans * (v+1)) % MOD
    
    print(ans)

def main():
    N = ii()  # type: int
    solve(N)
    return

main()
