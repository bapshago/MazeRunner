from gamelevel import *
import pygame

def collision_detect(gameblocks,player):
	if pygame.Rect.collidelist(player,gameblocks) == -1:
		return -1
	return pygame.Rect.collidelist(player,gameblocks)

def collision_detect_cleaners(cleaners,player):
	rects_to_check=[]
	for cleaner in cleaners:
		rects_to_check.append(pygame.Rect(cleaner[0], cleaner[1], 25, 25))
	if pygame.Rect.collidelist(player,rects_to_check) == -1:
		return -1
	return pygame.Rect.collidelist(player,rects_to_check)

