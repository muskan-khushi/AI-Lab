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
    x, y = 0, 0  # Fixed starting position
    if grid[x][y] == dirty:
        print(f"Cleaning ({x},{y})")
        grid[x][y] = clean
    displayGrid(grid)

def modelBasedReflexVacuum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == dirty:
                print(f"Cleaning ({i},{j})")
                grid[i][j] = clean
    displayGrid(grid)

def goalBasedReflexVacuum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == dirty:
                print(f"Cleaning ({i},{j})")
                grid[i][j] = clean
    print("All dirty locations cleaned!")
    displayGrid(grid)

def main():
    grid = generateGrid()
    
    print("\nInitial Grid:")
    displayGrid(grid)
    
    print("\nUsing Simple Reflex Agent:")
    simpleReflexVacuum(grid)
    
    print("\nUsing Model-Based Reflex Agent:")
    modelBasedReflexVacuum(grid)
    
    print("\nUsing Goal-Based Reflex Agent:")
    goalBasedReflexVacuum(grid)

if __name__ == "__main__":
    main()
