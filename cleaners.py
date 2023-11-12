import pygame
from constants import *
from gamelevel import *
from gamelevels import *

class Cleaner_asset():
	def __init__(self,asset_id,image_files,breakable,capturable,goal,velocity,boost_time,selectedlev):
		self.image_files=image_files
		self.breakable=breakable
		self.capturable=capturable
		self.goal=goal
		self.asset_id=asset_id
		self.LEVSIZE=25
		self.selectedlev=selectedlev
		self.rects=build_level_variable(self.asset_id,resetlevels(self.selectedlev),self.LEVSIZE)
		self.point_value=5
		self.load_image_files()
		self.current_image=self.processed_images[0]
		self.image_count = len(self.processed_images)
		self.image_current_count = 0
		self.velocity=velocity
		self.velocity_count=self.velocity
		self.boost_time=boost_time

	def update(self):
		pass

	def load_image_files(self):
		self.processed_images=[]
		for image in self.image_files:
			self.processed_images.append(pygame.image.load(image).convert())


	def display_level_rects(self,screen):
		if self.rects:
			for cleaners in self.rects:
				screen.blit(self.current_image,cleaners)

			if self.velocity_count == self.velocity:
				if self.image_current_count +1 < self.image_count:
					self.image_current_count = self.image_current_count + 1
				else:
					self.image_current_count = 0
				self.current_image=self.processed_images[self.image_current_count]
				self.velocity_count= 0
			else:
				self.current_image=self.processed_images[self.image_current_count]
				self.velocity_count = self.velocity_count + 1



	def build_level_rects(self,level):
		self.selectedlev=level
		self.rects=build_level_variable(self.asset_id,resetlevels(self.selectedlev),self.LEVSIZE)


		



