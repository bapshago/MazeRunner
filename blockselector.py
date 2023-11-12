import pygame
from constants import *

class Blockselector():
	def __init__(self, pos_x, pos_y,rectsize):
		self.x = pos_x
		self.y = pos_y
		self.size = rectsize
		self.rect = pygame.Rect([self.x,self.y,self.size,self.size])

	def update(self):
		self.rect = pygame.Rect([self.x,self.y,self.size,self.size])
