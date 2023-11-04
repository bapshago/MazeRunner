import pygame
from constants import *

def build_level_variable(inputs,LEVSIZE):
	gameblocks_output=[]
	gameblocks_output2=[]
	gameblocks_output3=[]
	gameblocks_output4=[]
	counterrow=0
	counteritem=0
	for row in inputs:
		for gameblock in row:
			if gameblock == 1:
				gameblocks_output.append(pygame.Rect([(25*counteritem),(25*counterrow),LEVSIZE,LEVSIZE]))
			if gameblock == 2:
				gameblocks_output2.append(pygame.Rect([(25*counteritem),(25*counterrow),LEVSIZE,LEVSIZE]))
			if gameblock == 3:
				gameblocks_output3.append(pygame.Rect([(25*counteritem),(25*counterrow),LEVSIZE,LEVSIZE]))
			if gameblock == 4:
				gameblocks_output4.append([(25*counteritem),(25*counterrow),25,3,6])
			counteritem=counteritem+1
		counterrow=counterrow+1
		counteritem=0
	return gameblocks_output,gameblocks_output2,gameblocks_output3,gameblocks_output4


def build_game_board(gameblocks,screen,color,IMG):
	for gameblock in gameblocks:
		screen.blit(IMG,gameblock)

def build_game_blocks_solid(gameblocks,screen,color,IMG):
	for gameblock in gameblocks:
		pygame.draw.rect(screen, color, gameblock)
