import random, sys, time, pygame
from pygame.locals import *

pygame.init()
WHITE = (255, 255, 255)
FONT = pygame.font.Font("resources/fonts/3Dventure.ttf", 30)

class ScoreBoard:
    """ScoreBoard class that tracks and updates two players' scores"""

    def __init__(self):
        """Creates a new instance of ScoreBoard"""
        self.p1_score = 0
        self.p2_score = 0
        
    def add_point(self, player):
        """Increases player's score by 1 point"""
        if (player == "p1"):
            self.p1_score += 1
        else:
            self.p2_score += 1
        
    def get_p1_score(self):
        """Returns self.p1_score"""
        return self.p1_score

    def get_p2_score(self):
        """Returns self.p2_score"""
        return self.p2_score

    def check_for_winner(self):
        """Returns 'p1' if self.p1_score is 7
           Returns 'p2' if self.p2_score is 7
           Returns None otherwise
        """
        if (self.p1_score == 7):
            return "p1"
        elif (self.p2_score == 7):
            return "p2"
        return None
    
    def update_board(self, display):
        """Displays up-to-date self.p1_score and self.p2_score onto self.display
        """
        self.score_display = FONT.render(str(self.p1_score) + ' : ' + str(self.p2_score), 1, WHITE)
        self.score_rect = self.score_display.get_rect()
        self.score_rect.topleft = (375, 65) 
        display.blit(self.score_display, self.score_rect)
        
