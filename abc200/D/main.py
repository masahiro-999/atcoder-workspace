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

MOD = 200
YES = "Yes"
NO = "No"

def trace_back_to_head(dp, A, start_i, target_i, dp_value_limit=0):
    # dpのstart_iから先頭まで遡って見つける
    ans = []
    i = start_i
    while i > 0:
        if dp[i][target_i]>dp_value_limit and dp[i-1][(target_i-A[i-1])%MOD]>dp_value_limit:
            ans.append(i)
            target_i = (target_i - A[i-1]) % MOD
            i -= 1
        elif dp[i][target_i]>dp_value_limit and dp[i-1][target_i]>dp_value_limit:
            i -= 1
        else:
            break
    return (ans, i, target_i)

def solv_200(N: int, A: "List[int]", i):
    c = range(1,N+1)
    b = [j for j in range(1,N+1) if j != i] 
    print(YES)
    print(len(b), *b)
    print(len(c), *c)
    return

def solve(N: int, A: "List[int]"):
    for i,a in enumerate(A):
        if a%MOD == 0:
            solv_200(N,A,i+1)
            return
    
    # dp[i][j] = i番目までの整数の中からいくつか選んで総和を200で割った余りがjになるような選び方が何通りあるか
    dp = [[0] * MOD for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(MOD):
            dp[i + 1][j] = min(2, dp[i + 1][j] + dp[i][j])
            dp[i + 1][(j + A[i]) % MOD] = min(2,dp[i + 1][(j + A[i]) % MOD] + dp[i][j])
    # 二通り以上の選び方を見つける
    target_i = -1
    for i in range(1,MOD):
        if dp[N][i] >= 2:
            target_i = i
            break
    if target_i == -1:
        print(NO)
        return
    # 二通り以上の選び方がある場合、その選び方を見つける
    # dpの値が、2以上を維持している区間を見つける
    ans_common, last_i, target_i = trace_back_to_head(dp, A, N, target_i,1)
    # 1に別れた後の選び方を見つける
    ans_1,_,_ = trace_back_to_head(dp, A, last_i-1, target_i)
    ans_2,_,_ = trace_back_to_head(dp, A, last_i-1, (target_i - A[last_i-1]) % MOD)

    ans_1 = ans_common + ans_1
    ans_2 = ans_common +[last_i]+ ans_2

    print(YES)
    print(len(ans_1), *ans_1[::-1])
    print(len(ans_2), *ans_2[::-1])
    return

def main():
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)
    return

if __name__ == '__main__':
    main()
