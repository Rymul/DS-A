from collections import deque

# Has Path

# DFS iterative

def has_path(graph, src, dst):
    stack = [ src ]
    while stack:
        current = stack.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False


# DFS recursive

def recursive_has_path(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if recursive_has_path(graph, neighbor, dst) is True:
            return True
    return False

# BFS

def bfs_has_path(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True    
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False
