
# Alpha-Beta Pruning Algorithm

# Binary game tree with multiple candidate moves
tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

nodes_evaluated = 0
branches_pruned = 0

def alpha_beta(node, depth, alpha, beta, maximizing):
    global nodes_evaluated, branches_pruned

    # Leaf node
    if isinstance(node, int):
        nodes_evaluated += 1
        return node

    if maximizing:
        best = float("-inf")

        for i, child in enumerate(node):
            value = alpha_beta(
                child, depth + 1, alpha, beta, False
            )
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                branches_pruned += len(node) - i - 1
                print("Pruned remaining branches at depth", depth)
                break

        return best

    else:
        best = float("inf")

        for i, child in enumerate(node):
            value = alpha_beta(
                child, depth + 1, alpha, beta, True
            )
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                branches_pruned += len(node) - i - 1
                print("Pruned remaining branches at depth", depth)
                break

        return best

# Evaluate each root move
alpha = float("-inf")
beta = float("inf")

left_value = alpha_beta(tree[0], 1, alpha, beta, True)
alpha = max(alpha, left_value)

right_value = alpha_beta(tree[1], 1, alpha, beta, True)

if left_value >= right_value:
    best_move = "Left"
    best_value = left_value
else:
    best_move = "Right"
    best_value = right_value

print("\nLeft move value:", left_value)
print("Right move value:", right_value)
print("Best move:", best_move)
print("Best utility value:", best_value)
print("Nodes evaluated:", nodes_evaluated)
print("Branches pruned:", branches_pruned)
