from collections import deque


def bfs(graph, start):
    path = []
    queue = deque([start])

    while queue:
        v = queue.popleft()
        if v not in path:
            path.append(v)
            queue.extend(graph[v])

    return path


if __name__ == '__main__':
    graph = {'A': ['B', 'C', 'D'],
             'B': ['E'],
             'C': ['F', 'G'],
             'D': ['H'],
             'E': ['I'],
             'F': ['J'],
             'G': [],
             'H': [],
             'I': [],
             'J': []}

    print('bfs: ', bfs(graph, 'A'))
