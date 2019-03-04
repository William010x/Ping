import pygame, sys

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Ping!')
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PADDLE_SPEED = 5

def game_loop():
    # Initialize game data
    # board = Board()
    paddle_1_change = 0
    paddle_2_change = 0
    crashed = False
    
    while not crashed: # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                sys.exit()
                
            ########### PADDLE MOVEMENT ###########
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    paddle_2_change = -PADDLE_SPEED
                elif event.key == pygame.K_DOWN:
                    paddle_2_change = PADDLE_SPEED
                elif event.key == pygame.K_w:
                    paddle_1_change = -PADDLE_SPEED
                elif event.key == pygame.K_s:
                    paddle_1_change = PADDLE_SPEED
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_2_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_1_change = 0
            ########### PADDLE MOVEMENT ###########
            
        # board.move_paddle_1(paddle_1_change)
        # board.move_paddle_2(paddle_2_change)
        # board.move_ball()
        display.fill(BLACK)
        # board.draw()
        
        pygame.display.update()
        clock.tick(60)
    
game_loop()
pygame.quit()
sys.exit()
