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


MOD = 998244353

class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )
    
def keta(i):
    count = 0
    while i >0:
        count += 1
        i = i//10
    return count

def main():
    Q = ii()
    s = ModInt(1)
    keta = 1
    s_list = [1]
    top = 0
    for i in range(Q):
        i = li()
        if i[0] == 1:
            s_list.append(i[1])
            s = (s*10 +i[1])
            keta += 1

        elif i[0] == 2:
            keta -= 1
            s = s -s_list[top]*ModInt(10)**keta
            top += 1
        elif i[0] == 3:
            print(s)

main()


