from collections import deque

def bfs(graph, start, end, parent):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        u = queue.popleft()
        for v, capacity in enumerate(graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return visited[end]

def maximum(graph, start, end):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, start, end, parent):
        path_flow = float('inf')
        s = end
        while s != start:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = end
        while v != start:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow



def main():
    graph = [
        [0, 6, 0, 4, 0, 0, 0, 0, 0, 0],
        [6, 0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 5, 4, 0, 0, 5, 0, 0], 
        [4, 0, 5, 0, 0, 2, 0, 3, 0, 0],
        [0, 0, 4, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 3, 2, 2],
        [0, 0, 5, 3, 0, 5, 3, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 2, 7, 0, 1],
        [0, 0, 0, 0, 0, 0, 2, 0, 1, 0],
    ]
    while True:  
        try:
            start = int(input("Введите начальную точку: "))-1
            end = int(input("Введите конечную точку: "))-1
            max_flow = maximum(graph, start, end)
            break
        except:
            print("Что-то не так, попробуйте еще раз!")

    return f"Максимальный поток: {max_flow}"



if __name__ == '__main__':
    print(main())