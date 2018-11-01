import collections

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        visit(vertex)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def visit(n):
    print(n)

if __name__ == '__main__':
        graph = {'A': set(['C', 'B']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A']),
         'D': set(['B']),
         'E': set(['B'])}
        
        bfs(graph, 'A')