import pygame

class Cleaner():
	def __init__(self, pos_x, pos_y,rectsize,velocity,animation_speed,cleaner_images):
		self.x = pos_x
		self.y = pos_y
		self.size = rectsize
		self.rect = pygame.Rect([self.x,self.y,self.size,self.size])
		self.movelist = []
		self.velocity = velocity
		self.velocity_count = 0
		self.previous_positions = [(0,0),(0,0)]
		self.animation_speed = animation_speed
		self.animation_speed_count = 0
		self.cleaner_images = cleaner_images
		self.current_image = 0


	def move_cleaner(self,move_x_pos,move_x_neg,move_y_pos,move_y_neg):
		if move_x_pos and self.x < SCREENX-self.size:
			self.x = self.x + self.velocity
		if move_x_neg and self.x > 0:
			self.x = self.x - self.velocity
		if move_y_pos and self.y < SCREENY-self.size:
			self.y = self.y + self.velocity
		if move_y_neg and self.y > 0:
			self.y = self.y - self.velocity
		self.update()
		self.update_previous_position((self.x,self.y))

	def update(self):
		self.rect = pygame.Rect([self.x,self.y,self.size,self.size])

	def update_previous_position(self,newposition):
		if not self.previous_positions[-1] == newposition:
			if len(self.previous_positions) < 20:
				self.previous_positions.append(newposition)
			else:
				del self.previous_positions[0]
				self.previous_positions.append(newposition)


	def display_cleaner(self,screen):
		self.update()
		if self.current_image > len(self.cleaner_images)-1:
			self.current_image = 0
		screen.blit(self.cleaner_images[self.current_image],(self.x,self.y))
		if self.animation_speed_count == 0:
			self.current_image=self.current_image + 1
			self.animation_speed_count = self.animation_speed
		self.animation_speed_count  = self.animation_speed_count  - 1
		

		




