import pygame
import sys

# Maze definition
maze = [
    ['S','0','1','0'],
    ['1','0','1','0'],
    ['0','0','0','G']
]

ROWS, COLS = len(maze), len(maze[0])
TILE = 60  # Size of each square in pixels

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Start
RED = (255, 0, 0)    # Goal
BLUE = (0, 0, 255)   # Player

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((COLS * TILE, ROWS * TILE))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

# Find start position
player_pos = None
for i in range(ROWS):
    for j in range(COLS):
        if maze[i][j] == 'S':
            player_pos = [i, j]
            break
    if player_pos:
        break

if player_pos is None:
    raise ValueError("No starting position 'S' found in the maze!")

# Draw the maze
def draw_maze():
    for i in range(ROWS):
        for j in range(COLS):
            rect = pygame.Rect(j*TILE, i*TILE, TILE, TILE)
            if maze[i][j] == '1':
                pygame.draw.rect(screen, BLACK, rect)
            elif maze[i][j] == 'S':
                pygame.draw.rect(screen, GREEN, rect)
            elif maze[i][j] == 'G':
                pygame.draw.rect(screen, RED, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)  # Grid lines
    # Draw player
    pygame.draw.rect(screen, BLUE, pygame.Rect(player_pos[1]*TILE, player_pos[0]*TILE, TILE, TILE))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            x, y = player_pos
            if event.key == pygame.K_UP and x > 0 and maze[x-1][y] != '1':
                player_pos[0] -= 1
            elif event.key == pygame.K_DOWN and x < ROWS-1 and maze[x+1][y] != '1':
                player_pos[0] += 1
            elif event.key == pygame.K_LEFT and y > 0 and maze[x][y-1] != '1':
                player_pos[1] -= 1
            elif event.key == pygame.K_RIGHT and y < COLS-1 and maze[x][y+1] != '1':
                player_pos[1] += 1

    screen.fill(WHITE)
    draw_maze()
    pygame.display.flip()
    clock.tick(60)

    # Check win
    if maze[player_pos[0]][player_pos[1]] == 'G':
        print("You reached the goal! You won!")
        pygame.quit()
        sys.exit()
