import pygame
from constants import *
from gamelevel import *
from gamelevels import *

class Game_asset():
	def __init__(self,asset_id,image_file,breakable,capturable,goal,selectedlev):
		self.image_file=image_file
		self.image=pygame.image.load(self.image_file).convert()
		self.breakable=breakable
		self.capturable=capturable
		self.goal=goal
		self.asset_id=asset_id
		self.LEVSIZE=25
		self.selectedlev=selectedlev
		self.rects=build_level_variable(self.asset_id,resetlevels(self.selectedlev),self.LEVSIZE)
		self.point_value=5

	def update(self):
		pass

	def add_asset(self,x_pos,y_pos):
		self.rect.append(pygame.Rect([x_pos,y_pos,self.LEVSIZE,self.LEVSIZE]))

	def display_level_rects(self,screen):
		if self.rects:
			for gameblock in self.rects:
				screen.blit(self.image,gameblock)

	def build_level_rects(self,level):
		self.selectedlev=level
		self.rects=build_level_variable(self.asset_id,resetlevels(self.selectedlev),self.LEVSIZE)


		



