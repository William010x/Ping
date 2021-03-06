from random import randint
from math import sin, cos, pi
import pygame

SHAPES = {"square": [[10,10], [-10,10], [-10,-10], [10,-10]], \
          "circle": [[0,10], [-4,9], [-6,8], [-7,7], [-8,6], [-9,4], \
                     [-10,0], [-9,-4], [-8,-6], [-7,-7], [-6,-8], [-4,-9], \
                     [0,-10], [4,-9], [6,-8], [7,-7], [8,-6], [9,-4], \
                     [10,0], [9,4], [8,6], [7,7], [6,8], [4,9]],
          "star": [[0,-12], [3, -4], [11, -4], [5, 2], [7, 10], [0,5], \
                   [-7, 10], [-5, 2], [-11, -4], [-3, -4]],
          "triangle": [[0,-8], [-10,8], [10,8]]}

class Ball(object):
	"""
	Ball constructor:
	parameters:
	x_pos / y_pos: center position for the ball (cartesian point)
	x_vel / y_vel: speed values for the ball (separated in components)
	shape: a string value which reads the dictionary SHAPES
	size: constant int multiplier value for the ball's size
	"""
	def __init__(self, x_pos, y_pos, x_vel, y_vel, shape, size):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.x_vel = x_vel
		self.y_vel = y_vel
		if (shape == "random"):
			self.points = list(SHAPES.values())[randint(0, len(SHAPES) - 1)]
		else:
		        self.points = SHAPES[shape]
		for p in self.points:
			p[0] *= size
			p[1] *= size
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
		for point in self.fake_points:
			if point[1] < 0 or point[1] > 600:
				self.y_vel = -self.y_vel
				break

	def bounce(self, block):
		x_block_min = block.get_x_pos()
		x_block_max = block.get_x_pos() + 20
		y_block_min = block.get_y_pos()	
		y_block_max = block.get_y_pos() + 100
		for point in self.fake_points:
			if point[0] <= x_block_max and \
			point[0] >= x_block_min and \
			point[1] <= y_block_max and \
			point[1] >= y_block_min:
				self.x_vel = -(self.x_vel+(self.x_vel/(2*abs(self.x_vel)))) #self.x_vel/abs(self.x_vel) gives +1 or -1 depending on value of x_vel
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