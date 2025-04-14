import pygame

pygame.init()

# Constants
CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

# Colors
BLUE = (0, 0, 225)
WHITE = (255, 255, 255)
PINK = (255, 182, 193)

# Initialize screen
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Eraser Effect in Python")

# Create grid
grid = []
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

# Create eraser
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

# Game loop variables
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw grid
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)
        else:
            pygame.draw.rect(screen, WHITE, rect)  # Erased area

    grid = new_grid  # Update grid after loop

    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

    # Eraser movement with mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)
    
    pygame.draw.rect(screen, PINK, eraser)  # Draw eraser

    pygame.display.flip()
    clock.tick(60)  # Maintain smooth frame rate

pygame.quit()

