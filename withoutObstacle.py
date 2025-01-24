gridSize = 5
dirty = 'D'
clean = 'C'
empty = 'E'

# Function to generate a random 2D grid with dirty spots
def generateGrid():
    grid = []
    print("Enter the grid row by row, use 'D' for dirty and 'E' for empty.")
    for i in range(gridSize):
        while True:
            row = input(f"Enter row {i + 1}: ").strip()
            if len(row) == gridSize and all(c in [dirty, empty] for c in row):
                grid.append(list(row))
                break
            else:
                print(f"Invalid input. Please enter a row with {gridSize} characters using only 'D', ' ', or 'O'.")
    return grid

# Function to display the grid
def displayGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()
    print()

# Function to simulate the vacuum cleaner's movement
def vacuumCleaner(grid):
    x = 0
    y = 0
    cleanedGrid = 0
    moveRight = True

    while cleanedGrid < gridSize * gridSize:
        if grid[x][y] == dirty:
            grid[x][y] = clean
            print(f"Cleaning cell ({x},{y})")
            cleanedGrid += 1

        # Stop if all cells are cleaned
        if cleanedGrid == gridSize * gridSize:
            break

        # Move right to left, or left to right
        if moveRight:
            if y + 1 < gridSize:  # Move right until the end of the row
                y += 1
            else:
                x += 1  # Move down to the next row
                moveRight = False  # Change direction
        else:
            if y - 1 >= 0:  # Move left until the start of the row
                y -= 1
            else:
                x += 1  # Move down to the next row
                moveRight = True  # Change direction

        # Ensure we don't go out of bounds when moving to the next row
        if x >= gridSize:
            break  # Stop if we've reached the last row

        displayGrid(grid)
        print(f"Total cleaned grid: {cleanedGrid}\n")

    # Display the final grid state after cleaning
    print("Final Grid after cleaning:")
    displayGrid(grid)


# Main function
def main():
    grid = generateGrid()
    print("Initial Grid: ")
    displayGrid(grid)

    vacuumCleaner(grid)

# Run the program
if __name__ == "__main__":
    main()
