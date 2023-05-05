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

{% endif %}

def main():
    {% if prediction_success %}
    {{input_part}}
    solve({{ actual_arguments }})
    {% else %}
    // Failed to predict input format
    {% endif %}
    return

main()