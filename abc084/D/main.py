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



def solve(Q: int, l: "List[int]", r: "List[int]"):
    num_min = 1
    num_max = 100000
    prime_table=[1]*(num_max+1)
    prime_table[0] = 0
    prime_table[1] = 0
    for i in range(2, num_max+1):
        k = i*2
        while k <= num_max:
            prime_table[k] = 0
            k += i
    sum = 0
    num_2017 = [0]*(num_max+1)
    for i in range(1,num_max,2):
        if prime_table[i] and prime_table[(i+1)//2]:
            sum += 1
        num_2017[i] = sum

    for a,b in zip(l,r):
        if a == 1:
            ans = num_2017[b]
        else:
            ans = num_2017[b] - num_2017[a-2] 
        print(ans)

def main():
    Q = ii()  # type: int
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i], r[i] = li()
    solve(Q, l, r)
    return

main()
