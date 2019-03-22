import pygame, sys, time
from board import Board
from menu import Menu

#Initialize Menu Object
menu = Menu()
menu.display_menu()
#End of Menu Object

pygame.init()
display = pygame.display.set_mode((800, 600))
icon = pygame.image.load("resources/images/icon.png")
pygame.display.set_caption('Ping!')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
FONT = pygame.font.Font("resources/fonts/3Dventure.ttf", 100)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PADDLE_SPEED = 5

def goal(board):
    '''Checks if ball scored and updates points accordingly'''
    if (board.get_ball().x_pos <= 0):
        board.get_scoreboard().add_point("p2")
        board.get_paddle_1().reset()
        board.get_paddle_2().reset()
        display.fill(BLACK)
        board.draw(display)
        pygame.display.update()
        winner = board.get_scoreboard().check_for_winner()
        if (winner == "p2"):
            display_victory("p2")
        elif (winner == None):
            board.get_ball().launch(1)
    elif (board.get_ball().x_pos >= 800):
        board.get_scoreboard().add_point("p1")
        board.get_paddle_1().reset()
        board.get_paddle_2().reset()        
        display.fill(BLACK)
        board.draw(display)        
        pygame.display.update()
        winner = board.get_scoreboard().check_for_winner()
        if (winner == "p1"):
            display_victory("p1")
        elif (winner == None):
            board.get_ball().launch(0)  

def display_victory(winner):
    '''Shows which player won and sends players back to main menu'''
    text = winner + " won "
    text_surf = FONT.render(text, True, WHITE)
    text_rect = text_surf.get_rect()
    text_rect.topleft = (250, 200)
    display.blit(text_surf, text_rect)   
    #print("display victory called")
    pygame.display.update()
    time.sleep(5)
    menu.display_menu()
    game_loop()
    
def game_loop():
    '''Starts the actual game and re-intializes all game values'''
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
        goal(board)
        board.ball.bounce(board.get_paddle_1())
        board.ball.bounce(board.get_paddle_2())
        display.fill(BLACK)
        board.draw(display)
        pygame.display.update()
        clock.tick(60)
    
game_loop()
pygame.quit()
sys.exit()
