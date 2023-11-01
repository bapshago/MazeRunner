import pygame
import time
import math
from constants import *

class Player():
	def __init__(self, pos_x, pos_y,rectsize,velocity,lives):
		self.x = pos_x
		self.y = pos_y
		self.size = rectsize
		self.rect = pygame.Rect([self.x,self.y,self.size,self.size])
		self.movelist = []
		self.velocity = velocity
		self.velocity_set = velocity
		self.vector_degrees = 0
		self.previous_positions = [(0,0),(0,0)]
		self.lives=lives
		self.boost_time = 0
		self.boost = False
		self.boost_time_set = 10


	def move_player(self,move_x_pos,move_x_neg,move_y_pos,move_y_neg):
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
		if self.boost and self.boost_time > 0:
			self.velocity = self.velocity + 1
			self.boost_time = self.boost_time -1
			print(self.boost_time)

		else:
			self.boost = False
			self.velocity = self.velocity_set


	def determine_movement_vector(self):
		currentmouse = pygame.mouse.get_pos()
		v1 = pygame.math.Vector2(currentmouse[0], currentmouse[1])
		v2 = pygame.math.Vector2(self.x, self.y)
		self.vector_degrees = v1.angle_to(v2)
	
	def update_previous_position(self,newposition):
		if not self.previous_positions[-1] == newposition:
			if len(self.previous_positions) < 20:
				self.previous_positions.append(newposition)
			else:
				del self.previous_positions[0]
				self.previous_positions.append(newposition)

	def find_player_speed(self):
		dx = self.previous_positions[-1][0] - self.previous_positions[-2][0]
		dy = self.previous_positions[-1][1] - self.previous_positions[-2][1]
		speed = math.sqrt(dx*dx + dy*dy)
		return speed

	def build_players_lives_rects(self):
		player_life_count = self.lives
		player_lives_rects = []
		while player_life_count > 0:
			player_lives_rects.append([25*player_life_count-25,SCREENY-25])
			player_life_count = player_life_count - 1
		return player_lives_rects

	def player_boost(self):
		self.boost = True
		self.boost_time = self.boost_time_set
	


		



