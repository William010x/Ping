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
		#TODO: lanuch method 
		pass

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
				
		