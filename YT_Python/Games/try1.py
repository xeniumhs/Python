#game window
#game loop
#event handler
import pygame
pygame.init()
SCREEN_WIDTH=800
SCREEN_HEIGHT=480

screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = pygame.Rect((300,200,75,50))
run=True
while run:

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(200,0,0),player)

    key= pygame.key.get_pressed()
    if key[pygame.K_UP]==True:
       player.move_ip(0,-1)
    elif key[pygame.K_DOWN]==True:
       player.move_ip(0,1)
    elif key[pygame.K_RIGHT]==True:
       player.move_ip(1,0)
    elif key[pygame.K_LEFT]==True:
       player.move_ip(-1,0)
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        run=False

    pygame.display.update()

pygame.quit()