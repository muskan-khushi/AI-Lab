# defining and initializing variables
gridSize = 5
dirty = 'D'
clean = 'C'
empty = 'E'
obstacle = 'O'

# function to generate a grid with clean or dirty or empty cells
def generateGrid():
    grid = []
    print("Enter the grid row by row, use 'D' for dirty, 'E' for empty, and 'O' for obstacle.")
    for i in range(gridSize):
        while True:
            row = input(f"Enter row {i + 1}: ").strip()
            if len(row) == gridSize and all(c in [dirty, empty, obstacle] for c in row):
                grid.append(list(row))
                break
            else:
                print(f"Invalid input. Please enter a row with {gridSize} characters using only 'D', 'E', or 'O'.")
    return grid

# function to display the grid
def displayGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()
    print()

# function for the vacuum cleaner's movement and cleaning
def vacuumCleaner(grid):
    x = 0 
    y = 0  
    cleanedGrid = 0  

    global obstacle, gridSize, dirty, clean

    total_dirty = sum(row.count(dirty) for row in grid)

    visited = set()

    while cleanedGrid < total_dirty:
        if grid[x][y] == dirty:
            grid[x][y] = clean
            cleanedGrid += 1
            print(f"Cleaning cell ({x},{y})")

        visited.add((x, y))

        moved = False

        # Move right
        if y + 1 < gridSize and grid[x][y + 1] != obstacle and (x, y + 1) not in visited:
            y += 1
            moved = True
        # Move left
        elif y - 1 >= 0 and grid[x][y - 1] != obstacle and (x, y - 1) not in visited:
            y -= 1
            moved = True
        # Move down
        elif x + 1 < gridSize and (x + 1, y) not in visited:
            x += 1
            if x % 2 == 0:
                y = 0  
            else:
                y = gridSize - 1  
            moved = True

        if not moved:
            # Check if there are dirty cells left and the cleaner is stuck
            remaining_dirty_cells = sum(row.count(dirty) for row in grid)
            if remaining_dirty_cells > 0:
                print("No more valid moves available. Stuck!")
                break

        displayGrid(grid)
        print(f"Total cleaned grid: {cleanedGrid}\n")

# main function
def main():
    grid = generateGrid()
    print("Initial Grid: ")
    displayGrid(grid)

    vacuumCleaner(grid)

if __name__ == "__main__":
    main()
