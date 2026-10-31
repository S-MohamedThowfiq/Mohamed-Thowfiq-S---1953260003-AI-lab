

graph = {
    'Data': ['Preprocessing'],
    'Preprocessing': ['Training', 'Validation'],
    'Training': ['Evaluation'],
    'Validation': ['Evaluation'],
    'Evaluation': ['Deployment'],
    'Deployment': ['Monitoring'],
    'Monitoring': ['Training']
}

def dfs(graph, start, goal):
    visited = set()
    traversal = []
    parent = {start: None}
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        traversal.append(node)

        if node == goal:
            break

        # Reverse to preserve adjacency-list order
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = node
                stack.append(neighbor)

    # Reconstruct the path if the goal was reached
    if goal not in visited:
        path = None
    else:
        path = []
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

    return traversal, path


start = input("Enter starting task: ")
goal = input("Enter target task: ")

if start not in graph or goal not in graph:
    print("Invalid task name!")
else:
    traversal, path = dfs(graph, start, goal)

    print("DFS traversal:", traversal)

    if path:
        print("Target is reachable.")
        print("Valid path:", " -> ".join(path))
    else:
        print("Target is not reachable.")
