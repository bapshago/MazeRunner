import pygame
from constants import *


class Selectorblock():
	def __init__(self, pos_x, pos_y,rectsize,image_file,asset_id):
		self.x = pos_x
		self.y = pos_y
		self.size = rectsize
		self.rect = pygame.Rect([self.x,self.y,self.size,self.size])
		self.image_file = image_file
		self.img=pygame.image.load(self.image_file).convert()
		self.asset_id=asset_id

	def update(self):
		self.rect = pygame.Rect([self.x,self.y,self.size,self.size])

	def display(self,screen):
		screen.blit(self.img,self.rect)
