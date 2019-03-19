import pygame

class Paddle:
    def __init__(self, x_pos, y_pos):
        self.__x_pos = x_pos
        self.__y_pos = y_pos
        
    def move(self, speed):
        new_pos = self.__y_pos + speed
        if (not (new_pos < 0 or new_pos > 500)):
            self.__y_pos += speed
        
    def get_x_pos(self):
        return self.__x_pos
    
    def get_y_pos(self):
        return self.__y_pos
    
    def draw(self, display):
        pygame.draw.rect(display, (255,255,255), [self.__x_pos, 
                                                  self.__y_pos, 20, 100])
        