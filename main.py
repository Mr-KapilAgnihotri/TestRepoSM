
### 2. `main.py`

"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""
def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)


# Helper function to perform topological sort
def topological_sort(graph):
    n = len(graph)
    topo_sort = []
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        for neighbor, _ in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        topo_sort.append(node)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    topo_sort.reverse()
    return topo_sort


# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    n = len(graph)
    # Initialize distances to all nodes as negative infinity
    dist = [-float('inf')] * n
    
    # Set the distance of the starting nodes (nodes with no incoming edges) to 0
    for node in topo_order:
        if dist[node] == -float('inf'):
            dist[node] = 0
    
    # Process nodes in topological order
    for u in topo_order:
        if dist[u] != -float('inf'):
            for v, weight in graph[u]:
                if dist[u] + weight > dist[v]:
                    dist[v] = dist[u] + weight

    # Return the maximum distance found
    return max(dist)

