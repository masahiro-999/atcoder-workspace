class Scc:
    def __init__(self, n):
        self.g = defaultdict(list)
        self.g_rev = defaultdict(list)
        self.n = n

    def clear_visited(self):
        self.visited = [False] * self.n

    def rdfs(self, i):
        self.path.add(i)
        self.visited[i] = True
        for n in self.g_rev[i]:
            if n not in self.path and not self.visited[n]:
                self.rdfs(n)

    def dfs(self, s):
        self.visited[s] = 1
        for n in self.g[s]:
            if not self.visited[n]:
                self.dfs(n)
        self.order.append(s)

    def add_edge(self, a, b):
        self.g[a].append(b)
        self.g_rev[b].append(a)

    def forward_dfs(self):
        for i in range(self.n):
            if not self.visited[i]:
                self.dfs(i)

    def reverse_dfs(self):
        result = []
        for i in reversed(self.order):
            if self.visited[i]:
                continue
            self.path = set()
            self.rdfs(i)
            result.append(self.path)
        return result

    def scc(self):
        self.order = []
        self.clear_visited()
        self.forward_dfs()
        self.clear_visited()
        return self.reverse_dfs()
