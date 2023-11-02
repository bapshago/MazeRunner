import pygame
from gamelevel import *
from collision import *
from player import *
from gamelevels import *
from cleaners import *
from constants import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([550,600])
BRICKIMG = pygame.image.load('brick_wall_25x25.png').convert()
BRICKIMG2 = pygame.image.load('black_white.png').convert()
PLAYERIMG = pygame.image.load('player.png').convert()
GAMEBLOCKS,GAMEGOAL,GAMEBLOCKBREAKABLE,GAMECLEANERS = build_level_variable(resetlevels(selectedlev),LEVSIZE)
player1=Player(PLAYER1_SETUP[0],PLAYER1_SETUP[1],PLAYER1_SETUP[2],PLAYER1_SETUP[3],PLAYER1_SETUP[4])
pygame.display.set_caption('Maze Runner - Level 1')
CLEANER_IMAGES = [pygame.image.load('cleaner.png').convert(),pygame.image.load('cleaner1.png').convert(),pygame.image.load('cleaner2.png').convert(),pygame.image.load('cleaner3.png').convert(),pygame.image.load('cleaner4.png').convert(),pygame.image.load('cleaner5.png').convert(),pygame.image.load('cleaner6.png').convert(),pygame.image.load('cleaner7.png').convert()]
#cleaner1 = Cleaner(CLEANER1_SETUP[0],CLEANER1_SETUP[1],CLEANER1_SETUP[2],CLEANER1_SETUP[3],CLEANER1_SETUP[4],CLEANER_IMAGES)

#build cleaners
def build_cleaners():
	level_cleaners=[]
	for cleaners in GAMECLEANERS:
		level_cleaners.append(Cleaner(cleaners[0],cleaners[1],cleaners[2],cleaners[3],cleaners[4],CLEANER_IMAGES))
	return level_cleaners

level_cleaners = build_cleaners()

while running:
	for event in pygame.event.get():
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

	screen.fill((SCREEN_FILL_COLOR))
	
	player1.determine_movement_vector()
	#prevents player from passing through walls
	if collision_detect(GAMEBLOCKS,player1.rect) > -1:
		player1.x,player1.y = player1.previous_positions[-2]
		player1.previous_positions[-1] = player1.previous_positions[-2]
		player1.update()
	else:
		player1.move_player(move_x_pos,move_x_neg,move_y_pos,move_y_neg)
		player1.update_previous_position((player1.x,player1.y))

	if collision_detect(GAMEBLOCKBREAKABLE,player1.rect) > -1:
		del GAMEBLOCKBREAKABLE[collision_detect(GAMEBLOCKBREAKABLE,player1.rect)]
		player1.score += 5
	
	if collision_detect_cleaners(GAMECLEANERS,player1.rect) > -1:
		player1.player_boost()

	
	#determines if player hits goal
	if collision_detect(GAMEGOAL,player1.rect) > -1:
		if len(GAMEGOAL) > 1 :
				print("Goal Hit")
				print(str(len(GAMEGOAL)))
				del GAMEGOAL[collision_detect(GAMEGOAL,player1.rect)]
				player1.score += 10
		else:
			if len(GAMEBLOCKS) > 1:
				del GAMEBLOCKS[-1]
				if len(GAMEBLOCKBREAKABLE) >1:
					del GAMEBLOCKBREAKABLE[-1]
			else:
				print("you won")
				print("Your time was: " + str(timer))
				player1.score = player1.score + int(timer)-525
				selectedlev = selectedlev + 1
				pygame.display.set_caption(caption)
				if selectedlev < LEVNUMBERS:
					GAMEBLOCKS,GAMEGOAL,GAMEBLOCKBREAKABLE,GAMECLEANERS = build_level_variable(resetlevels(selectedlev),LEVSIZE)
					level_cleaners = build_cleaners()
					timer=0
					timerswitch=False
					#player1.velocity = player1.velocity + 1
				else:
					print("you won")
					running = False

	#cleaner1.display_cleaner(screen)
	for cleaners in level_cleaners:
		cleaners.display_cleaner(screen)

	caption = str('Maze Runner - Level ' + str(selectedlev + 1) + " Score: " + str(player1.score))
	pygame.display.set_caption(caption)

	pygame.draw.rect(screen, (100,0,0),player1.rect)
	build_game_board(GAMEBLOCKS,screen,GAMEBLOCK_COLOR,BRICKIMG)
	build_game_board(GAMEGOAL,screen,GAMEGOAL_COLOR,BRICKIMG2)
	build_game_board(GAMEBLOCKBREAKABLE,screen,GAMEGOAL_COLOR,BRICKIMG)
	build_game_board(player1.build_players_lives_rects(),screen,GAMEGOAL_COLOR,PLAYERIMG)

	#timer progress bar
	if timer > 525:
		print("You Lost")
		timer = 0
		timerswitch = False
		caption = str('Maze Runner - Level ' + str(selectedlev + 1))
		pygame.display.set_caption(caption)		
		if player1.lives > 0: 
			player1.lives = player1.lives - 1
			GAMEBLOCKS,GAMEGOAL,GAMEBLOCKBREAKABLE,GAMECLEANERS = build_level_variable(resetlevels(selectedlev),LEVSIZE)
			level_cleaners = build_cleaners()
		else:
			running=False

	else:
		pygame.draw.rect(screen, GAMEGOAL_COLOR, (0, 525, timer, 50))
		pygame.draw.rect(screen, (200,200,200), (525, 525, 10, 50))
	
	pygame.display.flip()
	
	#increments timer
	if timerswitch:
		timer=timer+1*DIFFICULTY_FACTOR
		
	clock.tick(60)  # 60 FPS
pygame.quit()
