from dataclasses import dataclass, field
import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = input
II = lambda: int(I())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))

@dataclass
class TrieNode:
    children: dict = field(default_factory=lambda: defaultdict(TrieNode))
    is_x_terminal: bool = False
    count_y: int = 0

trie_tree = TrieNode()

def add_x(S):
    node = trie_tree
    for s in S:
        node = node.children[s]
        if node.is_x_terminal:
            # 既に追加済みの場合は処理不要
            return 0
    node.is_x_terminal = True
    ret = node.count_y
    add_count_y(S,-ret)
    return ret

def add_y(S):
    node = trie_tree
    for s in S:
        node = node.children[s]
        if node.is_x_terminal:
            # Prefixが一致するXが既にある場合追加しない
            return 0
    add_count_y(S, 1)
    return 1

def add_count_y(S,val):
    """Trie木の根からSの間の全てのノードにcount_yにvalを足す"""
    node = trie_tree
    for s in S:
        node = node.children[s]
        node.count_y += val

Q =II()
ans = 0
for _ in range(Q):
    t,s = LI()
    if t == "1":
        ans -= add_x(s)
    else:
        ans += add_y(s)
    print(ans)
