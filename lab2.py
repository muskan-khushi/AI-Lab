# defining and initializing variables
gridSize = 5
dirty = 'D'
clean = 'C'
empty = 'E'
obstacle = 'O'

# function to generate a grid with clean, dirty, empty, or obstacle cells
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

# function to move obstacles aside
def moveObstacle(grid, x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < gridSize and 0 <= ny < gridSize and grid[nx][ny] == empty:
            grid[nx][ny] = obstacle  # Move the obstacle
            grid[x][y] = empty       # Mark the original position as empty
            print(f"Moved obstacle from ({x},{y}) to ({nx},{ny})")
            return True
    return False

# function for the vacuum cleaner's movement and cleaning
def vacuumCleaner(grid):
    x, y = 0, 0  # Starting position
    cleanedGrid = 0  
    total_dirty = sum(row.count(dirty) for row in grid)
    visited = set()

    while cleanedGrid < total_dirty:
        if grid[x][y] == dirty:
            grid[x][y] = clean
            cleanedGrid += 1
            print(f"Cleaning cell ({x},{y})")
        
        visited.add((x, y))
        moved = False

        # Check all possible movements
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < gridSize and 0 <= ny < gridSize:
                if grid[nx][ny] == obstacle:
                    if moveObstacle(grid, nx, ny):
                        continue  # Try moving again after shifting the obstacle
                if grid[nx][ny] != obstacle and (nx, ny) not in visited:
                    x, y = nx, ny
                    moved = True
                    break
        
        if not moved:
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
