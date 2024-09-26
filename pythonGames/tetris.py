import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
FPS = 1

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Tetris shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 0], [0, 1, 1]],  # S
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

SHAPE_COLORS = [CYAN, YELLOW, RED, GREEN, BLUE, ORANGE, MAGENTA]

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tetris')

# Clock
clock = pygame.time.Clock()

# Function to draw the grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

# Function to draw a block
def draw_block(x, y, color):
    pygame.draw.rect(screen, color, pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Function to check collision
def check_collision(grid, shape, offset):
    x, y = offset
    for row_index, row in enumerate(shape):
        for col_index, cell in enumerate(row):
            if cell:
                grid_x = x + col_index
                grid_y = y + row_index
                if grid_x < 0 or grid_x >= GRID_WIDTH or grid_y >= GRID_HEIGHT:
                    return True
                if grid_y >= 0 and grid[grid_y][grid_x]:
                    return True
    return False

# Function to clear lines
def clear_lines(grid):
    lines_to_clear = [i for i, row in enumerate(grid) if all(row)]
    for i in lines_to_clear:
        del grid[i]
        grid.insert(0, [0] * GRID_WIDTH)
    return len(lines_to_clear)

# Function to rotate a shape
def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

# Main game loop
def main():
    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    current_shape = random.choice(SHAPES)
    current_color = random.choice(SHAPE_COLORS)
    shape_x, shape_y = GRID_WIDTH // 2, 0
    drop_speed = 1
    game_over = False

    while not game_over:
        screen.fill(BLACK)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(grid, current_shape, (shape_x - 1, shape_y)):
                        shape_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(grid, current_shape, (shape_x + 1, shape_y)):
                        shape_x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(grid, current_shape, (shape_x, shape_y + 1)):
                        shape_y += 1
                elif event.key == pygame.K_UP:
                    rotated_shape = rotate(current_shape)
                    if not check_collision(grid, rotated_shape, (shape_x, shape_y)):
                        current_shape = rotated_shape

        if not check_collision(grid, current_shape, (shape_x, shape_y + 1)):
            shape_y += 1
        else:
            for row_index, row in enumerate(current_shape):
                for col_index, cell in enumerate(row):
                    if cell:
                        grid[shape_y + row_index][shape_x + col_index] = current_color
            current_shape = random.choice(SHAPES)
            current_color = random.choice(SHAPE_COLORS)
            shape_x, shape_y = GRID_WIDTH // 2, 0
            if check_collision(grid, current_shape, (shape_x, shape_y)):
                game_over = True

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    draw_block(x, y, cell)

        # Draw current shape
        for row_index, row in enumerate(current_shape):
            for col_index, cell in enumerate(row):
                if cell:
                    draw_block(shape_x + col_index, shape_y + row_index, current_color)

        lines_cleared = clear_lines(grid)
        if lines_cleared:
            print(f"Lines cleared: {lines_cleared}")

        pygame.display.flip()
        clock.tick(FPS)

    print("Game Over!")
    pygame.quit()

if __name__ == "__main__":
    main()
