
# Minimax Algorithm

nodes_evaluated = 0

# Game tree: parent node -> child nodes
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Terminal values of leaf nodes
terminal_values = {
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 9
}


def minimax(node, depth, maximizing):
    global nodes_evaluated

    # Stop when a terminal node is reached
    if depth == 2 or not game_tree[node]:
        nodes_evaluated += 1
        value = terminal_values[node]
        print("Terminal value:", value)
        return value

    if maximizing:
        best = float("-inf")

        for child in game_tree[node]:
            value = minimax(child, depth + 1, False)
            best = max(best, value)

        return best

    else:
        best = float("inf")

        for child in game_tree[node]:
            value = minimax(child, depth + 1, True)
            best = min(best, value)

        return best


# Start the algorithm
best_value = minimax('A', 0, True)

print("\nBest value:", best_value)
print("Nodes evaluated:", nodes_evaluated)
