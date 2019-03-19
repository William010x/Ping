from random import randint
from math import sin, cos, pi
import pygame


class Ball(object):
	"""docstring for Ball"""
	#TODO: Finish docstring for Ball class
	def __init__(self, x_pos, y_pos, x_vel, y_vel, radius):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.x_vel = x_vel
		self.y_vel = y_vel
		self.radius = radius

	def launch(self, direction):
		"""
		The launch method, when called, picks a random angle and then sets the x and y velocity so it travels in that direction at a combined speed of 10.
		If the direction variable is set to 1, it will launch towards the left player. If not, it will launch towards the right player.
		"""
		angle = randint(10,60)
		angle = (angle/180)*pi #convert to rad
		
		x_sign, y_sign = 1
		if randint(0,1) == 1:	#50% chance of going up or down
			y_sign *= -1

		if direction == 1:
			x_sign *= -1

		x_vel = 10*cos(angle)*x_sign
		y_vel = 10*sin(angle)*y_sign

	def move(self):
		#Runs every game tick to move the ball
		#Using physics big 5 equations where a = 0 and t = 1 as an unknown unit
		# x = x_0 + vt + 1/2 a t^2
		self.x_pos += self.x_vel * 1
		self.y_pos += self.y_vel * 1	

	def bounce(self, block):
		#Rough Version (Simple brute forced method, will be improved to be more efficient)
		#Block will be a Wall class or subclass that knows about its size and position (not implemented yet)
		x_ball_range = range(self.x_pos - 1, self.x_pos + self.radius + 1)
		y_ball_range = range(self.y_pos - 1, self.y_pos + self.radius + 1)
		x_block_range = range(block.get_x_pos(), block.get_x_pos() + 20)
		y_block_range = range(block.get_y_pos(), block.get_y_pos() + 100)
		for x in x_ball_range:
			if x in x_block_range and (self.y_pos - 1 in y_block_range or self.y_pos + self.radius + 1 in y_block_range):
				self.x_vel = -self.x_vel
		'''for y in y_ball_range:
			if y in y_block_range and (self.x_pos - 1 in x_block_range or self.x_pos + self.radius + 1 in x_block_range):
				self.y_vel = -self.y_vel'''
				
				
	def draw(self, screen):
		pygame.draw.circle(screen, (255,255,255), (self.x_pos, self.y_pos), self.radius)