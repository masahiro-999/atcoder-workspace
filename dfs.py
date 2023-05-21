    # Try to find a hamiltonian path using DFS
    visited = [False] * N
 
    def dfs(node, depth):
        visited[node] = True
        if depth == N:
            return True
        for neighbor in graph[node]:
            if not visited[neighbor] and dfs(neighbor, depth + 1):
                return True
        visited[node] = False
        return False