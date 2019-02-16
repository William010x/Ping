import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Ping!')

crashed = False

########### EVENTS ###########


##############################

while not crashed: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            crashed = True
            pygame.quit()
            sys.exit()
        
        ########### PADDLE MOVEMENT ###########
        elif event.type == pygame.KEYDOWN:
            pygame.quit()
            if event.key == pygame.K_UP:
                # TODO: Move paddle 2 up
                pass
            elif event.key == pygame.K_DOWN:
                # TODO: Move paddle 2 down
                pass
            elif event.key == pygame.K_w:
                # TODO: Move paddle 1 up
                pass
            elif event.key == pygame.K_s:
                # TODO: Move paddle 1 down
                pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                # TODO: Stop moving paddle 2
                pass
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                # TODO: Stop moving paddle 1
                pass
        ########### PADDLE MOVEMENT ###########
        
    pygame.display.update()
    