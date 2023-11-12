import pygame
import pathfinding
from gamelevel import *
from collision import *
from player import *
from gamelevels import *
from cleaners import *
from constants import *
from mazenpc import *
from gameasset import *


#initiate Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREENX,SCREENY])
custom_level=False
#inital build of game assets


assets=[]
npc_assets=[]
cleaner_assets=[]
player1=""
def level_start(selectedlev,LEVELS,LEVELS_NPC):
	global player1
	for asset_to_load in GAME_ASSETS:
		assets.append(Game_asset(asset_to_load[0],asset_to_load[1],asset_to_load[2],asset_to_load[3],asset_to_load[4],selectedlev))

	for npc in NPC_ASSETS:
		npc_assets.append(Npc(npc[0],npc[1],npc[2],npc[3],npc[4],LEVELS,LEVELS_NPC))

	for cleaners in CLEANER_ASSETS:
		print(cleaners[1])
		cleaner_assets.append(Cleaner_asset(cleaners[0],cleaners[1],cleaners[2],cleaners[3],cleaners[4],cleaners[5],cleaners[6],selectedlev))

	player1=Player(PLAYER1_SETUP[0],PLAYER1_SETUP[1],PLAYER1_SETUP[2],PLAYER1_SETUP[3],PLAYER1_SETUP[4],PLAYER1_SETUP[5])

def clearboard():
	for asset in assets:
		if len(asset.rect) > 0: 
			del asset.rect[-1]
	return

intro_trigger = True

def startscreen(intro_trigger,status="start",score=0):
	mouse_rect=pygame.Rect(0,0,1,1)
	while intro_trigger:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouse_position = event.pos
					mouse_rect=pygame.Rect(mouse_position[0],mouse_position[1],1,1)
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					level_start(0,LEVELS[0],LEVELS_NPC[0])
					intro_trigger = False
					return False
				if event.key == pygame.K_c:
					custlev,cust_lev_npc=get_custom_level(100)
					level_start(100,custlev,cust_lev_npc)
					return False

		screen.fill((SCREEN_FILL_COLOR))
		show_custom_level_rects(screen)
		custom_level_rects = build_custom_level_count_rects()
		if not pygame.Rect.collidelist(mouse_rect,custom_level_rects) == -1:
				custom_level_number=int(pygame.Rect.collidelist(mouse_rect,custom_level_rects))+100
				print(custom_level_number)
				custlev,cust_lev_npc=get_custom_level(custom_level_number)
				level_start(custom_level_number,custlev,cust_lev_npc)
				return False


		if status=="start":
			caption = str('Maze Runner - Press space bar to start')
		if status=="loss":
			caption = str('Maze Runner - You lost! - '+ str(score) +' -  Press space bar to start')
		if status=="win":
			caption = str('Maze Runner - You won! - '+ str(score) +' - Press space bar to start')
		pygame.display.set_caption(caption)	
		pygame.display.flip()
		clock.tick(60)  # 60 FPS

while running:
	intro_trigger = startscreen(intro_trigger)
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
	
	#player asset interaction control
	for cleaner in cleaner_assets:
		if collision_detect(cleaner.rects,player1.rect) > -1:
			player1.player_boost(cleaner.boost_time)

	for asset in assets:
		if not asset.breakable: 
			if collision_detect(asset.rects,player1.rect) > -1:
				player1.x,player1.y = player1.previous_positions[-2]
				player1.previous_positions[-1] = player1.previous_positions[-2]
				player1.update()
			else:
				collision_stop=False

		if asset.breakable and not asset.goal:
			if collision_detect(asset.rects,player1.rect) > -1:
				del asset.rects[collision_detect(asset.rects,player1.rect)]
				player1.score += asset.point_value

		if asset.goal:
			if collision_detect(asset.rects,player1.rect) > -1:
				print("test")
				if len(asset.rects) > 1 :
					print("Goal Hit")
					print(str(len(asset.rects)))
					del asset.rects[collision_detect(asset.rects,player1.rect)]
					player1.score += asset.point_value
				else:
					print("you won the level")
					print("Your time was: " + str(timer))
					player1.score = player1.score + 525 - int(timer)
					selectedlev = selectedlev + 1
					print(selectedlev)
					print(LEVNUMBERS)
					pygame.display.set_caption(caption)
					if selectedlev < LEVNUMBERS:
						for asset in assets:
							asset.build_level_rects(selectedlev)
						for cleaner in cleaner_assets:
							cleaner.build_level_rects(selectedlev)
						for npc in npc_assets:
							npc.paths_list=LEVELS_NPC[selectedlev]
							npc.levelmap=LEVELS[selectedlev]
							npc.pathscount=0
						timer=0
						timerswitch=False
					else:
						print("you won")
						startscreen(True,status="win",score=player1.score)
						player1.lives = PLAYER1_SETUP[4]
						player1.score=0
						selectedlev=0
						for asset in assets:
							asset.build_level_rects(selectedlev)
						for cleaner in cleaner_assets:
							cleaner.build_level_rects(selectedlev)
						for npc in npc_assets:
							npc.paths_list=LEVELS_NPC[selectedlev]
							npc.levelmap=LEVELS[selectedlev]
							npc.pathscount=0
						timer=0
						timerswitch=False

	if not collision_stop:
		player1.move_player(move_x_pos,move_x_neg,move_y_pos,move_y_neg)
		player1.update_previous_position((player1.x,player1.y))

	caption = str('Maze Runner - Level ' + str(selectedlev + 1) + " Score: " + str(player1.score))
	pygame.display.set_caption(caption)

	pygame.draw.rect(screen, (100,0,0),player1.rect)

	#timer progress bar
	if timer > 525:
		print("You Lost")
		timer = 0
		timerswitch = False
		caption = str('Maze Runner - Level ' + str(selectedlev + 1))
		pygame.display.set_caption(caption)		
		if player1.lives > 0: 
			player1.lives = player1.lives - 1
			player1.build_players_lives_rects()
			for asset in assets:
				asset.build_level_rects(selectedlev)
			for cleaner in cleaner_assets:
				cleaner.build_level_rects(selectedlev)
			for npc in npc_assets:
							npc.paths_list=LEVELS_NPC[selectedlev]
							npc.levelmap=LEVELS[selectedlev]
							npc.pathscount=0


		else:
			startscreen(True,status="loss",score=player1.score)
			player1.lives = PLAYER1_SETUP[4]
			player1.score=0
			selectedlev=0
			for asset in assets:
				asset.build_level_rects(selectedlev)
			for cleaner in cleaner_assets:
				cleaner.build_level_rects(selectedlev)
			for npc in npc_assets:
							npc.paths_list=LEVELS_NPC[selectedlev]
							npc.levelmap=LEVELS[selectedlev]
							npc.pathscount=0
			timerswitch=False


	else:
		pygame.draw.rect(screen, GAMEGOAL_COLOR, (0, 525, timer, 50))
		pygame.draw.rect(screen, (200,200,200), (525, 525, 10, 50))
	
	for asset in assets:
		asset.display_level_rects(screen)

	for cleaners in cleaner_assets:
		cleaners.display_level_rects(screen)

	player1.show_players_lives(screen)
	
	for npc in npc_assets:
		npc.automove(screen)
		npc_penalty = pygame.Rect.colliderect(npc.rect,player1.rect)
		if npc_penalty:
			player1.score=player1.score - npc.penalty

	pygame.display.flip()
	
	#increments timer
	if timerswitch:
		timer=timer+1*DIFFICULTY_FACTOR
		
	clock.tick(60)  # 60 FPS

pygame.quit()
