import random
import os
import time

# Settings
width = 20
height = 10
alive = "🟢"
dead = "⚫"
generations = 50
delay = 0.3  # seconds

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid():
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

def print_grid(grid):
    for row in grid:
        print("".join([alive if cell else dead for cell in row]))

def count_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < height and 0 <= ny < width:
            count += grid[nx][ny]
    return count

def next_generation(grid):
    new_grid = [[0] * width for _ in range(height)]
    for x in range(height):
        for y in range(width):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1 and neighbors in (2, 3):
                new_grid[x][y] = 1
            elif grid[x][y] == 0 and neighbors == 3:
                new_grid[x][y] = 1
    return new_grid

if __name__ == "__main__":
    grid = create_grid()
    for gen in range(generations):
        clear()
        print(f"🌱 Generation {gen + 1}")
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(delay)

