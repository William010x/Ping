import pygame, sys

class ScoreBoard:
    """ScoreBoard class that tracks and updates two players' scores"""

    def __init__(self, display):
        """Creates a new instance of ScoreBoard"""
        self.p1_score = 0
        self.p2_score = 0
        self.display = display
        
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
