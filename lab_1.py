import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]
    
    
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = graph.get_nodes()
 
    shortest_path = {}
    previous_nodes = {}
 

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes: 
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        unvisited_nodes.remove(current_min_node)

    
    return previous_nodes, shortest_path
def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)
    
    print(f"Найден маршрут длинной {shortest_path[target_node]} единиц.")
    print(" -> ".join(reversed(path)))


def main():

    nodes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    
    init_graph = {}
    for node in nodes:
        init_graph[node] = {}
        
    init_graph["1"]["2"] = 6
    init_graph["1"]["4"] = 4
    init_graph["2"]["3"] = 3
    init_graph["3"]["5"] = 4
    init_graph["3"]["4"] = 5
    init_graph["3"]["8"] = 4
    init_graph["4"]["6"] = 2
    init_graph["4"]["8"] = 3
    init_graph["5"]["7"] = 4
    init_graph["6"]["8"] = 5
    init_graph["7"]["10"] = 2
    init_graph["7"]["8"] = 3
    init_graph["7"]["9"] = 5
    init_graph["8"]["9"] = 7
    init_graph["9"]["10"] = 1
    graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="9")
    return print_result(previous_nodes, shortest_path, start_node="9", target_node="1")
    




if __name__ == "__main__":
    main()
