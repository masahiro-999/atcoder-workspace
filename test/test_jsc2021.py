import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import time
import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd,sin,cos,tan,asin,acos,atan2,exp,log,log10
from collections import deque, Counter, defaultdict
from itertools import product, accumulate
from functools import reduce,lru_cache
from bisect import bisect, bisect_left, bisect_right
from heapq import heapify, heappop, heappush

import random
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from jsc2021.D.main import solve,solve1

def test_solve():

    for j in range(4,8):
        ret = []
        for i in range(1,9):
            ans = solve(i,j)
            assert ans == solve1(i,j)
            ret.append(ans)
        print(ret)
        
