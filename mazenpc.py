import pygame
import time
import math
from constants import *
from npcpaths import *

class Npc():
	def __init__(self, pos_x, pos_y,rectsize,velocity,img,levelmap):
		self.x = pos_x
		self.y = pos_y
		self.size = rectsize
		self.rect = pygame.Rect([self.x,self.y,self.size,self.size])
		self.movelist = []
		self.velocity = velocity
		self.img = img
		self.paths =[]
		self.paths_list =[]
		self.steps_for_path = []
		self.pathscount=0
		self.levelmap=levelmap

	def build_routes(self):
		if self.paths==[]:
			self.paths=self.paths_list[0]
		self.steps_for_path = find_route(self.paths[0][0],self.paths[0][1],self.paths[1][0],self.paths[1][1],self.levelmap)

	def automove(self):
		move_position_target_x=self.steps_for_path[0][0] * 25
		move_position_target_y=self.steps_for_path[0][1] * 25

		if move_position_target_x > self.x:
			self.x = self.x + self.velocity
		if move_position_target_x < self.x:
			self.x = self.x - self.velocity
		if move_position_target_y > self.y:
			self.y = self.y + self.velocity
		if move_position_target_y < self.y:
			self.y = self.y - self.velocity
		if move_position_target_y == self.y and move_position_target_x == self.x:
			if len(self.steps_for_path)==1:
				if self.pathscount == len(self.paths_list)-1:
					self.pathscount=0
				else:
					self.pathscount = self.pathscount+1
				self.paths = self.paths_list[self.pathscount]
				self.build_routes()
			else:
				del self.steps_for_path[0]
		self.update()

	def update(self):
		self.rect = pygame.Rect([self.x,self.y,self.size,self.size])

	def display(self,screen):
		self.update
		screen.blit(self.img,self.rect)
