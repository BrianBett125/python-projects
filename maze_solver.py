import random
import time

WIDTH = 20
HEIGHT = 10

# Maze cell states
WALL = "#"
PATH = " "
VISITED = "."

# Create a grid full of walls
maze = [[WALL for _ in range(WIDTH * 2 + 1)] for _ in range(HEIGHT * 2 + 1)]

# Directions (N, S, E, W)
DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def print_maze():
    for row in maze:
        print("".join(row))
    print()

def carve_passages(cx, cy):
    directions = DIRS[:]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
            if maze[nx * 2 + 1][ny * 2 + 1] == WALL:
                # Remove wall between current and next cell
                maze[cx * 2 + 1 + dx][cy * 2 + 1 + dy] = PATH
                maze[nx * 2 + 1][ny * 2 + 1] = PATH
                carve_passages(nx, ny)

def solve_maze(x, y, end_x, end_y):
    if x == end_x and y == end_y:
        return True

    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if maze[nx][ny] == PATH:
            maze[nx][ny] = VISITED
            if solve_maze(nx, ny, end_x, end_y):
                return True
            maze[nx][ny] = PATH  # Backtrack

    return False

def main():
    # Initialize maze
    maze[1][1] = PATH
    carve_passages(0, 0)

    # Mark entry and exit
    maze[1][0] = PATH  # Entry
    maze[HEIGHT * 2 - 1][WIDTH * 2] = PATH  # Exit

    print("🔨 Generating Maze...\n")
    print_maze()
    time.sleep(1)

    print("🧠 Solving Maze...\n")
    solve_maze(1, 1, HEIGHT * 2 - 1, WIDTH * 2 - 1)

    maze[1][0] = "S"  # Start
    maze[HEIGHT * 2 - 1][WIDTH * 2] = "E"  # End

    print_maze()

if __name__ == "__main__":
    main()

