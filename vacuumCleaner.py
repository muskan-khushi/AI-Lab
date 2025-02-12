# Defining and initializing variables
dirty = 'D'
clean = 'C'

def generateGrid():
    return [
        ['C', 'C', 'C', 'C', 'C'],
        ['C', 'C', 'D', 'C', 'C'],
        ['C', 'D', 'C', 'C', 'C'],
        ['D', 'C', 'C', 'C', 'C'],
        ['C', 'C', 'D', 'C', 'C']
    ]

def displayGrid(grid, label=""):
    if label:
        print(f"\n{label}")
    for row in grid:
        print(" ".join(row))
    print()

def simpleReflexVacuum(grid):
    print("Simple Reflex Agent Cleaning...")
    cleaned_positions = []
    for i in range(len(grid)):
        cells = range(len(grid[i])) if i % 2 == 0 else range(len(grid[i]) - 1, -1, -1)
        for j in cells:
            if grid[i][j] == dirty:
                grid[i][j] = clean
                cleaned_positions.append((i, j))
    print(f"Cleaned: {cleaned_positions}")
    displayGrid(grid, "Final Grid (Simple Reflex)")

def modelBasedReflexVacuum(grid):
    print("Model-Based Agent Cleaning...")
    cleaned_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == dirty:
                grid[i][j] = clean
                cleaned_positions.append((i, j))
    print(f"Cleaned: {cleaned_positions}")
    displayGrid(grid, "Final Grid (Model-Based Reflex)")

def goalBasedReflexVacuum(grid):
    print("Goal-Based Agent Cleaning...")
    dirt_count = sum(row.count(dirty) for row in grid)
    cleaned_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == dirty:
                grid[i][j] = clean
                cleaned_positions.append((i, j))
    print(f"Cleaned: {cleaned_positions} | Goal Achieved: {len(cleaned_positions)}/{dirt_count} dirty cells")
    displayGrid(grid, "Final Grid (Goal-Based Reflex)")

def main():
    initial_grid = generateGrid()
    displayGrid(initial_grid, "Initial Grid")

    simple_grid = generateGrid()
    simpleReflexVacuum(simple_grid)

    model_grid = generateGrid()
    modelBasedReflexVacuum(model_grid)

    goal_grid = generateGrid()
    goalBasedReflexVacuum(goal_grid)

if __name__ == "__main__":
    main()
