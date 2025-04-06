import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
PLAYER_WIDTH = 75
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5
COIN_RADIUS = 15
TARGET_SCORE = 5  # Score needed to win

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Font setup for score and messages
font = pygame.font.SysFont(None, 36)

# Function to spawn a new coin ensuring it does not overlap with players
def spawn_coin(player1, player2):
    while True:
        coin_x = random.randint(COIN_RADIUS, SCREEN_WIDTH - COIN_RADIUS)
        coin_y = random.randint(COIN_RADIUS, SCREEN_HEIGHT - COIN_RADIUS)
        coin_rect = pygame.Rect(coin_x - COIN_RADIUS, coin_y - COIN_RADIUS, COIN_RADIUS * 2, COIN_RADIUS * 2)
        
        if not player1.colliderect(coin_rect) and not player2.colliderect(coin_rect):
            return coin_rect

# Function to reset the game state
def reset_game():
    global player1, player2, coin, score1, score2
    player1 = pygame.Rect(300, 200, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = pygame.Rect(400, 200, PLAYER_WIDTH, PLAYER_HEIGHT)
    coin = pygame.Rect(-100, -100, COIN_RADIUS * 2, COIN_RADIUS * 2)  # Start with coin off-screen
    score1 = 0
    score2 = 0

# Function to display a message and wait for user input
def display_message(message, wait_time=2000):
    screen.fill((0, 0, 0))
    msg = font.render(message, True, (255, 255, 255))
    screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(wait_time)

# Main game loop
def main_game_loop():
    global player1, player2, coin, score1, score2
    reset_game()  # Initialize game state
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)  # 60 FPS

        # Fill screen with black color
        screen.fill((0, 0, 0))

        # Draw the players
        pygame.draw.rect(screen, (200, 0, 0), player1)  # Player 1: Red
        pygame.draw.rect(screen, (0, 0, 200), player2)  # Player 2: Blue

        # Spawn a coin if there isn't one
        if coin.left < 0:  # Check if coin is off-screen
            coin = spawn_coin(player1, player2)

        # Check for collision between player1 and coin
        if player1.colliderect(coin):
            coin = pygame.Rect(-100, -100, COIN_RADIUS * 2, COIN_RADIUS * 2)  # Move coin off-screen
            score1 += 1  # Increase Player 1's score

        # Check for collision between player2 and coin
        if player2.colliderect(coin):
            coin = pygame.Rect(-100, -100, COIN_RADIUS * 2, COIN_RADIUS * 2)  # Move coin off-screen
            score2 += 1  # Increase Player 2's score

        # Draw the coin if it has been initialized
        if coin.left >= 0:
            pygame.draw.circle(screen, (255, 215, 0), coin.center, COIN_RADIUS)

        # Get keys
        key = pygame.key.get_pressed()

        # Player 1 movement (Arrow keys) with boundary checks
        if key[pygame.K_UP] and player1.top - PLAYER_SPEED > 0:
            player1.move_ip(0, -PLAYER_SPEED)
        if key[pygame.K_DOWN] and player1.bottom + PLAYER_SPEED < SCREEN_HEIGHT:
            player1.move_ip(0, PLAYER_SPEED)
        if key[pygame.K_LEFT] and player1.left - PLAYER_SPEED > 0:
            player1.move_ip(-PLAYER_SPEED, 0)
        if key[pygame.K_RIGHT] and player1.right + PLAYER_SPEED < SCREEN_WIDTH:
            player1.move_ip(PLAYER_SPEED, 0)

        # Player 2 movement (WASD keys) with boundary checks
        if key[pygame.K_w] and player2.top - PLAYER_SPEED > 0:
            player2.move_ip(0, -PLAYER_SPEED)
        if key[pygame.K_s] and player2.bottom + PLAYER_SPEED < SCREEN_HEIGHT:
            player2.move_ip(0, PLAYER_SPEED)
        if key[pygame.K_a] and player2.left - PLAYER_SPEED > 0:
            player2.move_ip(-PLAYER_SPEED, 0)
        if key[pygame.K_d] and player2.right + PLAYER_SPEED < SCREEN_WIDTH:
            player2.move_ip(PLAYER_SPEED, 0)

        # Ensure players do not overlap
        if player1.colliderect(player2):
            # Adjust positions if overlap is detected
            if player1.right > player2.left and player1.left < player2.right:
                if player1.centerx < player2.centerx:
                    player1.right = player2.left
                else:
                    player1.left = player2.right
            if player1.bottom > player2.top and player1.top < player2.bottom:
                if player1.centery < player2.centery:
                    player1.bottom = player2.top
                else:
                    player1.top = player2.bottom

        # Display scores
        score_text1 = font.render(f'Player 1 Score: {score1}', True, (255, 255, 255))
        score_text2 = font.render(f'Player 2 Score: {score2}', True, (255, 255, 255))
        screen.blit(score_text1, (10, 10))
        screen.blit(score_text2, (10, 40))

        # Check for win condition
        if score1 >= TARGET_SCORE:
            display_message('Player 1 Wins!')
            return  # End game loop and return to main menu
        elif score2 >= TARGET_SCORE:
            display_message('Player 2 Wins!')
            return  # End game loop and return to main menu

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update display
        pygame.display.update()

# Main loop to handle game restarts
def main():
    while True:
        main_game_loop()  # Start the game
        
        # Ask if players want to play again
        screen.fill((0, 0, 0))
        play_again_text = font.render('Play Again? (Y/N)', True, (255, 255, 255))
        screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.update()

        # Wait for user input
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        waiting_for_input = False
                    elif event.key == pygame.K_n:





































                        
                        pygame.quit()
                        return

if __name__ == "__main__":
    main()
