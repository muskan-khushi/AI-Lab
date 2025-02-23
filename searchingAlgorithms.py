from queue import PriorityQueue

# Sample graph representation (Adjacency list with costs)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values for informed search algorithms
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 6,
    'G': 0  # Goal has heuristic 0
}


#UNIFORMED SEARCH
# Depth-Limited Search (DLS)
def dls(graph, node, goal, depth, path):
    if depth == 0:
        return None
    path.append(node)
    if node == goal:
        return path
    for neighbor, _ in graph[node]:
        if neighbor not in path:
            result = dls(graph, neighbor, goal, depth - 1, path[:])
            if result:
                return result
    return None

# Iterative Deepening Depth-First Search (IDDFS)
def iddfs(graph, start, goal):
    depth = 0
    print("\n--- Iterative Deepening Depth-First Search (IDDFS) ---")
    while True:
        print(f"Searching at depth {depth}...")
        result = dls(graph, start, goal, depth, [])
        if result:
            print(f"Goal '{goal}' found at depth {depth}!")
            return result
        depth += 1


#INFORMED SEARCH
# Best-First Search (Greedy Search)
def best_first_search(graph, start, goal, heuristic):
    print("\n--- Best-First Search (Greedy Search) ---")
    pq = PriorityQueue()
    pq.put((heuristic[start], [start]))  # Priority based on heuristic
    visited = set()

    while not pq.empty():
        _, path = pq.get()
        node = path[-1]

        if node in visited:
            continue
        visited.add(node)

        print(f"Expanding node '{node}' with heuristic {heuristic[node]}")

        if node == goal:
            print(f"Goal '{goal}' reached!")
            return path

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                pq.put((heuristic[neighbor], new_path))

    print("Goal not reachable!")
    return None

# A* Search Algorithm
def a_star(graph, start, goal, heuristic):
    print("\n--- A* Search Algorithm ---")
    pq = PriorityQueue()
    pq.put((0 + heuristic[start], 0, [start]))  # (f = g + h, g, path)
    visited = {}

    while not pq.empty():
        f, g, path = pq.get()
        node = path[-1]

        if node in visited and visited[node] <= g:
            continue
        visited[node] = g

        print(f"Expanding node '{node}': g={g}, h={heuristic[node]}, f={f}")

        if node == goal:
            print(f"Goal '{goal}' reached with total cost {g}!")
            return path

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_path = path + [neighbor]
            pq.put((new_g + heuristic[neighbor], new_g, new_path))

    print("Goal not reachable!")
    return None

# Run and print results
iddfs_path = iddfs(graph, 'A', 'G')
best_first_path = best_first_search(graph, 'A', 'G', heuristic)
a_star_path = a_star(graph, 'A', 'G', heuristic)

# Run DLS with the depth where IDDFS found the goal
depth_limit = 4
print("\n--- Depth-Limited Search (DLS) ---")
dls_path = dls(graph, 'A', 'G', depth_limit, [])
if dls_path:
    print(f"Goal 'G' found within depth {depth_limit}!")
else:
    print(f"Goal 'G' not found within depth {depth_limit}.")

# Final summary of results
print("\n--- Final Results Summary ---")
print(f"DLS Path Found (Depth {depth_limit}): {dls_path}")
print(f"IDDFS Path Found: {iddfs_path}")
print(f"Best-First Search Path Found: {best_first_path}")
print(f"A* Search Path Found: {a_star_path}")