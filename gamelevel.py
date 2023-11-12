import pygame
from constants import *

def build_level_variable(asset_number,inputs,LEVSIZE):
	gameblocks_output=[]
	counterrow=0
	counteritem=0
	for row in inputs:
		for gameblock in row:
			if gameblock == asset_number:
				gameblocks_output.append(pygame.Rect([(25*counteritem),(25*counterrow),LEVSIZE,LEVSIZE]))
			counteritem=counteritem+1
		counterrow=counterrow+1
		counteritem=0
	return gameblocks_output

def build_game_board(gameblocks,screen,color,IMG):
	for gameblock in gameblocks:
		screen.blit(IMG,gameblock)

def build_game_blocks_solid(gameblocks,screen,color,IMG):
	for gameblock in gameblocks:
		pygame.draw.rect(screen, color, gameblock)

