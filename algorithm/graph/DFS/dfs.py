def dfs(graph, start):
    visited, need_visit = [], []

    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                need_visit.extend(graph[node])

    return visited

# bfs와의 차이는 단지 pop(0)이냐 pop()이냐의 차이만 있음

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'G', 'H', 'I'],
    'D': ['B', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
    'G': ['C'],
    'H': ['C'],
    'I': ['C', 'J'],
    'J': ['I']
}

print(dfs(graph, 'A'))