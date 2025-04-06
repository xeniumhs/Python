import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooting Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up player
player_width, player_height = 50, 60
player_x, player_y = WIDTH // 2, HEIGHT - player_height - 10
player_vel = 5

# Set up bullet
bullet_width, bullet_height = 5, 10
bullets = []
bullet_vel = 7

# Set up target
target_width, target_height = 50, 50
targets = []
target_vel = 2
target_spawn_time = 30  # Frames between target spawns

# Main game loop
run = True
clock = pygame.time.Clock()

def draw_window():
    win.fill(BLACK)
    
    # Draw player
    pygame.draw.rect(win, WHITE, (player_x, player_y, player_width, player_height))
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(win, RED, bullet)
    
    # Draw targets
    for target in targets:
        pygame.draw.rect(win, WHITE, target)
    
    pygame.display.update()

while run:
    clock.tick(60)  # 60 FPS
    
    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Get keys
    keys = pygame.key.get_pressed()
    
    # Player movement
    if keys[pygame.K_LEFT] and player_x - player_vel > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x + player_width + player_vel < WIDTH:
        player_x += player_vel
    
    # Bullet movement
    for bullet in bullets:
        bullet.y -= bullet_vel
        if bullet.y < 0:
            bullets.remove(bullet)
    
    # Target movement
    for target in targets:
        target.y += target_vel
        if target.y > HEIGHT:
            targets.remove(target)
    
    # Bullet collision with target
    for bullet in bullets:
        for target in targets:
            if bullet.colliderect(target):
                bullets.remove(bullet)
                targets.remove(target)
                break
    
    # Shoot bullet
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit number of bullets
            bullet = pygame.Rect(player_x + player_width // 2 - bullet_width // 2, player_y, bullet_width, bullet_height)
            bullets.append(bullet)
    
    # Spawn targets
    if random.randint(1, target_spawn_time) == 1:
        target_x = random.randint(0, WIDTH - target_width)
        target = pygame.Rect(target_x, 0, target_width, target_height)
        targets.append(target)
    
    draw_window()

pygame.quit()
