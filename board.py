from paddle import Paddle

class Board:
    def __init__(self):
        #self.ball = Ball()
        self.paddle1 = Paddle(10, 250)
        self.paddle2 = Paddle(770, 250)
        
    def move_paddle_1(self, speed):
        self.paddle1.move(speed)
        
    def move_paddle_2(self, speed):
        self.paddle2.move(speed)
    
    def move_ball(self):
        #self.ball.move()
        return 1
        
    def get_paddle_1(self):
        return self.paddle1
    
    def get_paddle_2(self):
        return self.paddle2

    #def get_ball():
        # return self.ball
    
    def draw(self, display):
        self.paddle1.draw(display)
        self.paddle2.draw(display)
    