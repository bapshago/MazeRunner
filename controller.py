import pygame
from constants import *
def event_controller(event):
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEWHEEL:
			player1.size = player1.size + event.y
			if player1.size > 25:
				player1.size = 25
			if player1.size < 5:
				player1.size = 5

		if event.type == pygame.KEYDOWN:
			timerswitch=True
			if event.key == pygame.K_DOWN:
				move_y_pos = True
			if event.key == pygame.K_UP:
				move_y_neg = True
			if event.key == pygame.K_RIGHT:
				move_x_pos = True
			if event.key == pygame.K_LEFT:
				move_x_neg = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				move_y_pos = False
			if event.key == pygame.K_UP:
				move_y_neg = False
			if event.key == pygame.K_RIGHT:
				move_x_pos = False
			if event.key == pygame.K_LEFT:
				move_x_neg = False