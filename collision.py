from gamelevel import *
import pygame

def collision_detect(gameblocks,player):
	if pygame.Rect.collidelist(player,gameblocks) == -1:
		return -1
	return pygame.Rect.collidelist(player,gameblocks)
