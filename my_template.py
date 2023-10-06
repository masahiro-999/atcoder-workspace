import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate,permutations,combinations
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

{% if mod %}
MOD = {{ mod }}
{% endif %}
{% if yes_str %}
YES = "{{ yes_str }}"
{% endif %}
{% if no_str %}
NO = "{{ no_str }}"
{% endif %}

{% if prediction_success %}
def solve({{ formal_arguments }}):
{% else %}
def solve():
{% endif %}

def main():
    {% if prediction_success %}
    {{input_part}}
    solve({{ actual_arguments }})
    {% else %}
    solve()
    {% endif %}
    return

main()