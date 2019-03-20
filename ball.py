from random import randint
from math import sin, cos, pi
import pygame


class Ball(object):
	"""docstring for Ball"""
	#TODO: Finish docstring for Ball class
	def __init__(self, x_pos, y_pos, x_vel, y_vel, points):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.x_vel = x_vel
		self.y_vel = y_vel
		self.points = points
		self.__reset_fake_points()
		self.launch(1)

	def launch(self, direction):
		"""
		The launch method, when called, picks a random angle and then sets the x and y velocity so it travels in that direction at a combined speed of 10.
		If the direction variable is set to 1, it will launch towards the left player. If not, it will launch towards the right player.
		"""
		self.x_pos = 400
		self.y_pos = 300
		self.__reset_fake_points()
		angle = randint(10,60)
		angle = (angle/180)*pi #convert to rad

		x_sign = 1
		y_sign = 1
		if randint(0,1) == 1:	#50% chance of going up or down
			y_sign *= -1

		if direction == 1:
			x_sign *= -1

		self.x_vel = int(5*cos(angle)*x_sign)
		self.y_vel = int(5*sin(angle)*y_sign)

	def move(self, scoreboard):
		#Runs every game tick to move the ball
		#Using physics big 5 equations where a = 0 and t = 1 as an unknown unit
		# x = x_0 + vt + 1/2 a t^2
		self.x_pos += self.x_vel * 1
		self.y_pos += self.y_vel * 1
		self.__reset_fake_points()	
		if self.y_pos < 0 or self.y_pos > 600:
			self.y_vel = -self.y_vel

	def bounce(self, block):
		x_block_range = range(block.get_x_pos(), block.get_x_pos() + 20)
		y_block_range = range(block.get_y_pos(), block.get_y_pos() + 100)		
		for point in self.fake_points:
			if point[0] in x_block_range and point[1] in y_block_range:
				self.x_vel = -self.x_vel
				break
				
	def draw(self, screen):
		#pygame.draw.circle(screen, (255,255,255), (self.x_pos, self.y_pos), self.radius)
		pygame.draw.polygon(screen, (255,255,255), self.fake_points)
		
	def __reset_fake_points(self):
		self.fake_points = []
		for point in self.points:
			f_point = point[:]
			f_point[0] += self.x_pos
			f_point[1] += self.y_pos
			self.fake_points.append(f_point)		