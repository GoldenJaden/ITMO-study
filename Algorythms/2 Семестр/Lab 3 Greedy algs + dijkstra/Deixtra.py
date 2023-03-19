class Graph():
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

nodes = ["Полтавская ул.", "Лиговский проспект", "Невский проспект",
         "Ул. Жуковского", "Ул. Марата", "Свечной пер.", "Гончарная ул.", "Ул. Маяковского"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Лиговский проспект"]["Невский проспект"] = 332
init_graph["Лиговский проспект"]["Ул. Жуковского"] = 1200
init_graph["Лиговский проспект"]["Свечной пер."] = 764
init_graph["Свечной пер."]["Ул. Марата"] = 528
init_graph["Ул. Марата"]["Невский проспект"] = 858
init_graph["Невский проспект"]["Гончарная ул."] = 284
init_graph["Невский проспект"]["Ул. Маяковского"] = 638
init_graph["Невский проспект"]["Полтавская ул."] = 642
init_graph["Полтавская ул."]["Гончарная ул."] = 359
init_graph["Ул. Жуковского"]["Ул. Маяковского"] = 238

print(init_graph["Лиговский проспект"])


graph = Graph(nodes, init_graph)
start = "Свечной пер."
destination = "Полтавская ул."

def Dijkstra(graph):
    unvisited_nodes = graph.get_nodes()
    min_paths = {}
    for node in unvisited_nodes:
        min_paths[node] = float('inf')
    min_paths[start] = 0
    current_node = start
    while unvisited_nodes:
        trails = graph.get_outgoing_edges(current_node)
        for node in trails:
            if node in unvisited_nodes:
                if min_paths[node] == float('inf'):
                    min_paths[node] = min_paths[current_node] + graph.value(current_node, node)
                else:
                    min_paths[node] = min(min_paths[node], min_paths[current_node] + graph.value(current_node, node))
        unvisited_nodes.remove(current_node)
        if not unvisited_nodes:
            break
        candidates = {node: min_paths[node] for node in unvisited_nodes}
        current_node = min(candidates, key=candidates.get)
    return min_paths

p = Dijkstra(graph)
answer = p[destination]
print(p)
print(answer)



