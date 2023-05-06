import sys
from collections import deque, Counter, defaultdict
from itertools import product
sys.setrecursionlimit(5 * 10 ** 5)
# from pypyjit import set_param
# set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1



def solve(N: int):

    num_max = 1000000
    prime_table=[1]*(num_max+1)
    prime_table[0] = 0
    prime_table[1] = 0
    for i in range(2, num_max+1):
        k = i*2
        while k <= num_max:
            prime_table[k] = 0
            k += i
    p = []
    for i,val in enumerate(prime_table):
        if val:
            p.append(i)

    count = 0
    for i,a in enumerate(p):    
        for j,b in enumerate(p[i+1:]):
            for k,c in enumerate(p[i+j+2:]):
                if a*a*b*c*c <=N:
                    count += 1
                    # print(a , b , c)
                else:
                    break
            if a*a*b*b*b >=N:
                break
        if a*a*a*a*a >=N:
            break
        
    print(count)        


def main():
    N = ii()  # type: int
    solve(N)
    return

main()
