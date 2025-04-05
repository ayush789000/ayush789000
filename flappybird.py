import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 500, 600
PLAYER_SIZE = 50
BLOCK_SIZE = 50
SPEED = 5
BLOCK_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# Player Setup
player = pygame.Rect(WIDTH // 2, HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SIZE)

# Block List
blocks = []

# Clock
clock = pygame.time.Clock()

# Main Loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= SPEED
    if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
        player.x += SPEED
    
    # Spawn Blocks Randomly
    if random.randint(1, 30) == 1:
        blocks.append(pygame.Rect(random.randint(0, WIDTH - BLOCK_SIZE), 0, BLOCK_SIZE, BLOCK_SIZE))
    
    # Move Blocks
    for block in blocks[:]:
        block.y += BLOCK_SPEED
        if block.y > HEIGHT:
            blocks.remove(block)
        
        # Collision Detection
        if player.colliderect(block):
            running = False  # Game Over
    
    # Draw Player
    pygame.draw.rect(screen, BLACK, player)
    
    # Draw Blocks
    for block in blocks:
        pygame.draw.rect(screen, RED, block)
    
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()