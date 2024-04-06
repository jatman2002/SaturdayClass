graph = {
    "A": [["B", 3], ["C", 6], ["D", 1]],
    "B": [["A", 3], ["C", 4], ["D", 8], ["E", 3]],
    "C": [["A", 6], ["B", 4], ["D", 2], ["E", 5], ["S", 10]],
    "D": [["A", 1], ["B", 8], ["C", 2], ["E", 4], ["S", 7]],
    "E": [["B", 3], ["C", 5], ["D", 4], ["S", 2]],
    "S": [["C", 10], ["D", 7], ["E", 2]]
}

visited = []

to_visit = {}
to_visit_nodes = []

def dijkstra(current_node):

    visited.append(current_node)
    to_visit_nodes.remove(current_node)

    edges = graph[current_node] 
    for edge in edges:
        if edge[0] in visited:
            continue
        if edge[0] in to_visit.keys():
            new_value = to_visit[current_node] + edge[1]
            old_value = to_visit[edge[0]]
            to_visit[edge[0]] = min(old_value, new_value)
        else:
            to_visit[edge[0]] = to_visit[current_node] + edge[1]
            to_visit_nodes.append(edge[0])

    if len(to_visit_nodes) == 0:
        return

    min_number = float('inf')
    node_to_look_at = ''
    for node in to_visit_nodes:
        value = to_visit[node]
        if value < min_number:
            min_number = value
            node_to_look_at = node
    print(node_to_look_at)

    dijkstra(node_to_look_at)

to_visit['A'] = 0
to_visit_nodes.append('A')
dijkstra('A')

print(to_visit)
print(visited)
