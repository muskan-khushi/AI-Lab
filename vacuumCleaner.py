# defining and initializing variables
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

def displayGrid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def simpleReflexVacuum(grid):
    # Simple reflex agent moves row by row
    for i in range(len(grid)):
        # Move left to right if even row, right to left if odd row
        row = grid[i]
        cells = range(len(row)) if i % 2 == 0 else range(len(row)-1, -1, -1)
        
        for j in cells:
            print(f"Agent at position ({i},{j})")
            # React to current cell state
            if grid[i][j] == dirty:
                print(f"Dirty cell found! Cleaning ({i},{j})")
                grid[i][j] = clean
            else:
                print(f"Cell ({i},{j}) is already clean")
            displayGrid(grid)

def modelBasedReflexVacuum(grid):
    print("Model-based agent maintains internal state of environment")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(f"Agent at position ({i},{j})")
            if grid[i][j] == dirty:
                print(f"Dirty cell found in model! Cleaning ({i},{j})")
                grid[i][j] = clean
            else:
                print(f"Model shows cell ({i},{j}) is clean")
            displayGrid(grid)

def goalBasedReflexVacuum(grid):
    dirt_count = sum(row.count(dirty) for row in grid)
    cleaned = 0
    print(f"Goal-based agent identified {dirt_count} dirty cells to clean")
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(f"Agent at position ({i},{j})")
            if grid[i][j] == dirty:
                print(f"Cleaning dirty cell ({i},{j})")
                grid[i][j] = clean
                cleaned += 1
                print(f"Progress: {cleaned}/{dirt_count} cells cleaned")
            else:
                print(f"Cell ({i},{j}) is clean")
            displayGrid(grid)
    
    print("Goal achieved: All dirty locations cleaned!")

def main():
    # Generate fresh grid for each agent
    print("\nInitial Grid:")
    initial_grid = generateGrid()
    displayGrid(initial_grid)
    
    print("\nUsing Simple Reflex Agent:")
    simple_grid = generateGrid()
    simpleReflexVacuum(simple_grid)
    
    print("\nUsing Model-Based Reflex Agent:")
    model_grid = generateGrid()
    modelBasedReflexVacuum(model_grid)
    
    print("\nUsing Goal-Based Reflex Agent:")
    goal_grid = generateGrid()
    goalBasedReflexVacuum(goal_grid)

if __name__ == "__main__":
    main()