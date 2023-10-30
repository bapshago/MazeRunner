import pygame
from gamelevel import *
from collision import *
from player import *
from gamelevels import *
from constants import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([550,600])
BRICKIMG = pygame.image.load('brick_wall_25x25.png').convert()
BRICKIMG2 = pygame.image.load('black_white.png').convert()
PLAYERIMG = pygame.image.load('player.png').convert()
GAMEBLOCKS,GAMEGOAL = build_level_variable(resetlevels(selectedlev),LEVSIZE)
player1=Player(PLAYER1_SETUP[0],PLAYER1_SETUP[1],PLAYER1_SETUP[2],PLAYER1_SETUP[3],PLAYER1_SETUP[4])
pygame.display.set_caption('Maze Runner - Level 1')

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
	
	#determines if player hits goal
	if collision_detect(GAMEGOAL,player1.rect) > -1:
		if len(GAMEGOAL) > 1 :
				print("Goal Hit")
				print(str(len(GAMEGOAL)))
				del GAMEGOAL[collision_detect(GAMEGOAL,player1.rect)]
		else:
			if len(GAMEBLOCKS) > 1:
				del GAMEBLOCKS[-1]
			else:
				print("you won")
				print("Your time was: " + str(timer))
				selectedlev = selectedlev + 1
				caption = str('Maze Runner - Level ' + str(selectedlev + 1))
				pygame.display.set_caption(caption)
				if selectedlev < 4:
					GAMEBLOCKS,GAMEGOAL = build_level_variable(resetlevels(selectedlev),LEVSIZE)
					timer=0
					timerswitch=False
					#player1.velocity = player1.velocity + 1
				else:
					print("you won")
					running = False

	pygame.draw.rect(screen, (100,0,0),player1.rect)
	build_game_board(GAMEBLOCKS,screen,GAMEBLOCK_COLOR,BRICKIMG)
	build_game_board(GAMEGOAL,screen,GAMEGOAL_COLOR,BRICKIMG2)
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
			GAMEBLOCKS,GAMEGOAL = build_level_variable(resetlevels(selectedlev),LEVSIZE)
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
