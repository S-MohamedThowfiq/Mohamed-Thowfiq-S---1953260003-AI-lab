
import heapq

# Weighted graph: neighbor and travel cost
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 2, 'E': 5},
    'C': {'A': 3, 'D': 3, 'E': 4},
    'D': {'B': 2, 'C': 3, 'E': 2},
    'E': {'B': 5, 'C': 4, 'D': 2, 'F': 3},
    'F': {'E': 3}
}

# Heuristic estimates provided in the document
h = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 0
}


def a_star(graph, start, goal, h):
    # Priority queue entries: (f score, g score, node)
    open_list = [(h[start], 0, start)]

    g_cost = {start: 0}
    parent = {start: None}
    expanded = []
    closed = set()

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current in closed:
            continue

        closed.add(current)
        expanded.append(current)

        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            return path, g_cost[goal], expanded

        for neighbor, cost in graph[current].items():
            new_g = g_cost[current] + cost

            if new_g < g_cost.get(neighbor, float('inf')):
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                new_f = new_g + h[neighbor]

                heapq.heappush(
                    open_list, (new_f, new_g, neighbor)
                )

    return None, float('inf'), expanded


start = input("Enter starting location: ").upper()
goal = input("Enter destination: ").upper()

if start not in graph or goal not in graph:
    print("Invalid location!")
else:
    path, total_cost, expanded = a_star(
        graph, start, goal, h
    )

    print("Node expansion order:", expanded)

    if path:
        print("Optimal route:", " -> ".join(path))
        print("Total path cost:", total_cost)
    else:
        print("No route found.")
