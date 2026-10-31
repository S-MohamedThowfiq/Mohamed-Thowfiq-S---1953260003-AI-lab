
from collections import deque

CAPACITY_A = 4
CAPACITY_B = 3

def get_next_states(a, b):
    states = []

    # Fill either container
    states.append(((CAPACITY_A, b), "Fill 4L container"))
    states.append(((a, CAPACITY_B), "Fill 3L container"))

    # Empty either container
    states.append(((0, b), "Empty 4L container"))
    states.append(((a, 0), "Empty 3L container"))

    # Transfer water from 4L to 3L
    transfer = min(a, CAPACITY_B - b)
    states.append(((a - transfer, b + transfer),
                   "Pour 4L into 3L"))

    # Transfer water from 3L to 4L
    transfer = min(b, CAPACITY_A - a)
    states.append(((a + transfer, b - transfer),
                   "Pour 3L into 4L"))

    return states


def water_jug_bfs():
    start = (0, 0)
    queue = deque([start])

    visited = {start}
    parent = {start: (None, "Start")}

    goal = None

    while queue:
        state = queue.popleft()
        a, b = state

        if a == 2:
            goal = state
            break

        for next_state, action in get_next_states(a, b):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (state, action)
                queue.append(next_state)

    if goal is None:
        print("No solution found.")
        return

    # Reconstruct the solution
    solution = []
    current = goal

    while current is not None:
        previous, action = parent[current]
        solution.append((current, action))
        current = previous

    solution.reverse()

    print("Water Jug Solution:")
    for state, action in solution:
        print(f"{action}: 4L = {state[0]}L, "
              f"3L = {state[1]}L")

    print("Goal achieved: Exactly 2 litres in the 4L container.")
    print("Unique states visited:", len(visited))


water_jug_bfs()
