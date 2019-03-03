from random import randint
from math import sin, cos, pi


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

	def bounce(self, block):
		#Rough Version (Simple brute forced method, will be improved to be more efficient)
		#Block will be a Wall class or subclass that knows about its size and position (not implemented yet)
		x_ball_range = range(x_pos - 1, x_pos + radius + 1)
		y_ball_range = range(y_pos - 1, y_pos + radius + 1)
		x_board_range = range(block.x_pos, block.x_pos + block.x_size)
		y_board_range = range(block.y_pos, block.y_pos + block.y_size)
		for x in x_ball_range:
			if x in x_block_range and (y_pos - 1 in y_block_range or y_pos + radius + 1 in y_block_range):
				self.y_vel = -self.y_vel
		for y in y_ball_range:
			if y in y_block_range and (x_pos - 1 in x_block_range or x_pos + radius + 1 in x_block_range):
				self.x_vel = -self.x_vel		
				
		