from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

# DFS (Recursive)
def dfs(v, visited):
    visited.add(v)
    print(v, end=" ")
    for n in graph[v]:
        if n not in visited:
            dfs(n, visited)

# BFS
def bfs(start):
    visited = set([start])
    q = deque([start])
    while q:
        v = q.popleft()
        print(v, end=" ")
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                q.append(n)

dfs(0, set())
print()
bfs(0)