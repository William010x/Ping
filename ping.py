import pygame, sys, time
from board import Board

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Ping!')
clock = pygame.time.Clock()
FONT = pygame.font.Font('freesansbold.ttf', 100)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PADDLE_SPEED = 5

def goal(ball, scoreboard, board):
    if (ball.x_pos <= 0):
        scoreboard.add_point("p2")
        display.fill(BLACK)
        board.draw(display)
        pygame.display.update()
        winner = scoreboard.check_for_winner()
        if (winner == "p2"):
            display_victory("p2")
        elif (winner == None):
            ball.launch(1)
    elif (ball.x_pos >= 800):
        scoreboard.add_point("p1")
        display.fill(BLACK)
        board.draw(display)        
        pygame.display.update()
        winner = scoreboard.check_for_winner()
        if (winner == "p1"):
            display_victory("p1")
        elif (winner == None):
            ball.launch(0)  

def display_victory(winner):
    text = winner + " won "
    text_surf = FONT.render(text, True, WHITE)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (250, 200)
    display.blit(text_surf, text_rect)   
    print("display victory called")
    pygame.display.update()
    time.sleep(5)
    game_loop()
    
def game_loop():
    # Initialize game data
    board = Board()
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
            
        board.move_paddle_1(paddle_1_change)
        board.move_paddle_2(paddle_2_change)
        board.move_ball()
        goal(board.get_ball(), board.get_scoreboard(), board)
        board.ball.bounce(board.get_paddle_1())
        board.ball.bounce(board.get_paddle_2())
        display.fill(BLACK)
        board.draw(display)
        pygame.display.update()
        clock.tick(60)
    
game_loop()
pygame.quit()
sys.exit()
