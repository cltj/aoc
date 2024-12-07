import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    multirange,
    range,
    search,
    tail_call,
)

import numpy as np
from colorama import Fore, Style, init
from collections import Counter
import pygame
import time
import os

# Initialize colorama
init(autoreset=True)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
DIRECTION_WORDS = {(0, 1): "RIGHT", (1, 0): "DOWN", (0, -1): "LEFT", (-1, 0): "UP"}


def parse_raw(input: str) -> np.ndarray:
    return np.array([list(line) for line in input.splitlines()])


def add_grid_edges(grid: np.ndarray) -> np.ndarray:
    vertical = len(grid) + 2
    horizontal = len(grid[0]) + 2

    # Create a new grid with the required dimensions
    new_grid = np.full((vertical, horizontal), "/")

    # Copy the original grid into the new grid, leaving a border of '/'
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i + 1][j + 1] = grid[i][j]

    return new_grid


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return i, j


def get_next_direction(current_direction: tuple[int, int]) -> tuple[int, int]:
    current_index = DIRECTIONS.index(current_direction)
    next_index = (current_index + 1) % len(DIRECTIONS)
    return DIRECTIONS[next_index]


def walk(
    grid: np.ndarray, start: tuple[int, int], screen, max_steps: int = None
) -> np.ndarray:
    i, j = start
    direction = (-1, 0)  # Start by moving up
    steps = 0
    while max_steps is None or steps < max_steps:
        next_i, next_j = i + direction[0], j + direction[1]
        # print(
        #     f"Current position: ({i}, {j}), direction: {DIRECTION_WORDS[direction]}, next position: ({next_i}, {next_j})"
        # )
        if grid[next_i][next_j] == "#":
            direction = get_next_direction(direction)
            # print(
            #     f"Encountered {Fore.YELLOW}#{Style.RESET_ALL}, changing direction to: {DIRECTION_WORDS[direction]}"
            # )
        else:
            grid[i][j] = "X"
            i, j = next_i, next_j
            steps += 1
        if grid[i][j] == "/":  # Stop if we reach the edge
            break
        render_grid(grid, (i, j), screen)
        pygame.time.wait(5)  # Add a delay of 500 milliseconds between each step
    grid[i][j] = "@"  # Mark the current position with '@'
    render_grid(grid, (i, j), screen)  # Render the final position
    return grid, (i, j)


def render_grid(grid: np.ndarray, current_position: tuple[int, int], screen):
    cell_size = 20
    screen.fill((0, 0, 0))  # Fill the screen with black

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            color = (255, 255, 255) if cell == "." else (0, 0, 0)
            if cell == "@":
                color = (0, 0, 255)  # Blue for current position
            elif cell == "X":
                color = (0, 255, 0)  # Green for walked path
            elif cell == "#":
                color = (255, 255, 0)  # Yellow for obstacles
            elif cell == "/":
                color = (255, 0, 0)  # Red for edges
            pygame.draw.rect(
                screen, color, (j * cell_size, i * cell_size, cell_size, cell_size)
            )
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        pygame.Rect(
            current_position[1] * cell_size,
            current_position[0] * cell_size,
            cell_size,
            cell_size,
        ),
    )
    # pygame.display.flip()


def count_steps(grid: np.ndarray) -> int:
    return Counter(grid.flatten())["X"]


# Fetch data using aoc_helper
raw = aoc_helper.fetch(6, 2024)
data = parse_raw(raw)
boxed_grid = add_grid_edges(data)

# Disable sound in pygame
os.environ["SDL_AUDIODRIVER"] = "dummy"

# Initialize pygame
pygame.init()

# Create a window
cell_size = 20
width, height = len(boxed_grid[0]) * cell_size, len(boxed_grid) * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grid Visualization")
print("Pygame window initialized")

# Main loop to keep the window open and render each step
running = True
i, j = find_start(boxed_grid)
direction = (-1, 0)  # Start by moving up
steps = 0
max_steps = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if max_steps is None or steps < max_steps:
        next_i, next_j = i + direction[0], j + direction[1]
        if boxed_grid[next_i][next_j] == "#":
            direction = get_next_direction(direction)
        else:
            boxed_grid[i][j] = "X"
            i, j = next_i, next_j
            steps += 1
        if boxed_grid[i][j] == "/":  # Stop if we reach the edge
            running = False
        render_grid(boxed_grid, (i, j), screen)
        pygame.time.wait(500)  # Add a delay of 500 milliseconds between each step
    else:
        boxed_grid[i][j] = "@"
        render_grid(boxed_grid, (i, j), screen)
        running = False

    pygame.display.update()

print(count_steps(boxed_grid))
pygame.quit()
print("Pygame window closed")
