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
from blockselector import *
from selectorblocks import *


#initiate Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREENX,SCREENY])
custom_level=False

#inital build of game and builder assets
bassets=[]
bnpc_assets=[]
bcleaner_assets=[]
selector_blocks=[]
block_to_insert=[]
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

def build_level_start(selectedlev,LEVELS,LEVELS_NPC):
	#selectedlev=8
	global bassets
	global bcleaner_assets
	global bnpc_assets
	global selector_blocks
	selector_blockcount=0
	for asset_to_load in GAME_ASSETS:
		bassets.append(Game_asset(asset_to_load[0],asset_to_load[1],asset_to_load[2],asset_to_load[3],asset_to_load[4],selectedlev))
		selector_blocks.append(Selectorblock(25*selector_blockcount,550,LEVSIZE,asset_to_load[1],asset_to_load[0]))
		selector_blockcount=selector_blockcount+1
	bnpc_assets=[]
	for npc in NPC_ASSETS:
		bnpc_assets.append(Npc(npc[0],npc[1],npc[2],npc[3],npc[4],LEVELS,LEVELS_NPC))
		selector_blocks.append(Selectorblock(25*selector_blockcount,550,LEVSIZE,npc[4],npc[3]))
		selector_blockcount=selector_blockcount+1

	bcleaner_assets=[]
	for cleaners in CLEANER_ASSETS:
		bcleaner_assets.append(Cleaner_asset(cleaners[0],cleaners[1],cleaners[2],cleaners[3],cleaners[4],cleaners[5],cleaners[6],selectedlev))
		selector_blocks.append(Selectorblock(25*selector_blockcount,550,LEVSIZE,cleaners[1][1],cleaners[0]))
		selector_blockcount=selector_blockcount+1
	return selector_blocks

def clearboard():
	for asset in assets:
		if len(asset.rect) > 0: 
			del asset.rect[-1]
	return

def block_change(pos,block_to_in):
	global bassets
	global bcleaner_assets
	global bblock_to_insert
	global selector_blocks
	global block_to_insert
	savebtn_rect=pygame.Rect(0,575,25,25)

	updateblock=Blockselector(0,0,1)
	updateblock.x=pos[0]
	updateblock.y=pos[1]
	updateblock.update()
	print(updateblock.rect)
	for blocks in selector_blocks:
		print(blocks.asset_id)
	print(block_to_in)

	if updateblock.x < 500 and updateblock.y < 500:
		if not block_to_in==5:
			asset_counter=0
			for asset in bassets:
				if collision_detect(asset.rects,updateblock.rect) > -1:
					rect_to_move=bassets[asset_counter].rects[collision_detect(asset.rects,updateblock.rect)]
					del bassets[asset_counter].rects[collision_detect(asset.rects,updateblock.rect)]
					asset_counter_del=asset_counter
				asset_counter=asset_counter+1
			cleaner_counter=0
			for cleaners in bcleaner_assets:
				if collision_detect(cleaners.rects,updateblock.rect) > -1:
					rect_to_move=bcleaner_assets[cleaner_counter].rects[collision_detect(cleaners.rects,updateblock.rect)]
					del bcleaner_assets[cleaner_counter].rects[collision_detect(cleaners.rects,updateblock.rect)]
					cleaner_counter_del=cleaner_counter
				cleaner_counter=cleaner_counter+1
			asset_counter2=0
			replaced_block=False
			replaced_cleaner=False
			for asset in bassets:
				if asset.asset_id==block_to_in:
					bassets[asset_counter2].rects.append(rect_to_move)
					replaced_block=True
				asset_counter2=asset_counter2+1
			cleaner_counter2=0
			for cleaners in bcleaner_assets:
				if cleaners.asset_id==block_to_in:
					bcleaner_assets[cleaner_counter2].rects.append(rect_to_move)
					replaced_block=True
				cleaner_counter2=cleaner_counter2+1
			if not replaced_block:
				bassets[asset_counter_del].rects.append(rect_to_move)
	else:
		for block in selector_blocks:
			if block.rect.contains(updateblock.rect):
				block_to_insert= block.asset_id
		if savebtn_rect.contains(updateblock.rect):
			convert_rects_to_matrix()
			print("saved")

def add_npc(mouse_position):
	npc_x_cord=mouse_position[0] // 25
	npc_y_cord=mouse_position[1] // 25
	for npc in bnpc_assets:
		npc.paths_list.append([npc.paths_list[-1][0],[npc_x_cord,npc_y_cord]])
		print(npc.paths_list)

def delete_path():
	for npc in bnpc_assets:
		if len(npc.paths_list) > 2:
			del npc.paths_list[-1]
			npc.pathscount = npc.pathscount-1
			print(npc.paths_list)

def convert_rects_to_matrix():
	list_of_assets=[]
	for asset in bassets:
		for rect in asset.rects:
			list_of_assets.append([asset.asset_id,rect])
	for asset in bcleaner_assets:
		for rect in asset.rects:
			list_of_assets.append([asset.asset_id,rect])
	converted_to_matrix=getlevelbuilder()
	for item in list_of_assets:
		posx=item[1].left // 25
		posy=item[1].top // 25
		idnum=item[0]
		if idnum==9:
			idnum=0
		converted_to_matrix[posy][posx]=idnum
	routedata=[]
	for npc in bnpc_assets:
		routedata.append(npc.paths_list)
	write_level_to_file(converted_to_matrix,routedata)
	
def write_level_to_file(data,routedata):
	with open("customlevels.json", "r") as cust_level_read:
		try:
			json_data_current = cust_level_read.read()
			cust_level_read = json.loads(json_data_current)
			cust_level_read.append([{"CUSTOMLEVEL":data,"CUSTOMLEVEL_NPC":routedata}])
		except:
			cust_level_read=[[{"CUSTOMLEVEL":data,"CUSTOMLEVEL_NPC":routedata}]]
	with open("customlevels.json", "w") as file:
		json_data=json.dumps(cust_level_read)
		file.write(json_data)

intro_trigger = True

def startscreen(intro_trigger,status="start",score=0):
	mouse_rect=pygame.Rect(0,0,1,1)
	playgamebtn_rect=pygame.Rect(225,225,25,25)
	makegamebtn_rect=pygame.Rect(300,225,25,25)
	delcustomlevelbtn_rect=pygame.Rect(0,575,25,25)

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
				if event.key == pygame.K_b:
					build_level_start(8,LEVELS[8],LEVELS_NPC[8])
					level_builder_run()
					return False

		screen.fill((SCREEN_FILL_COLOR))
		show_custom_level_rects(screen)
		screen.blit(pygame.image.load('playganmebtn.png').convert(),playgamebtn_rect)
		screen.blit(pygame.image.load('makeganmebtn.png').convert(),makegamebtn_rect)
		screen.blit(pygame.image.load('delcustbtn.png').convert(),delcustomlevelbtn_rect)

		if playgamebtn_rect.contains(mouse_rect):
			level_start(0,LEVELS[0],LEVELS_NPC[0])
			intro_trigger = False
			return False

		if makegamebtn_rect.contains(mouse_rect):
			build_level_start(8,LEVELS[8],LEVELS_NPC[8])
			level_builder_run()
			return False

		if delcustomlevelbtn_rect.contains(mouse_rect):
			delete_custom_level(101)

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

def level_builder_run():
	global selector_blocks
	global block_to_insert
	savebtn_rect=pygame.Rect(0,575,25,25)
	backbtn_rect=pygame.Rect(25,575,25,25)
	undonpc_rect=pygame.Rect(100,575,25,25)
	mouse_rect=pygame.Rect(0,0,1,1)
	intro_trigger = True
	building=True
	while building:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				building = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouse_position = event.pos
					mouse_rect=pygame.Rect(mouse_position[0],mouse_position[1],1,1)
					if not block_to_insert==5 or mouse_position[1] > 500:
						block_change(mouse_position,block_to_insert)
					else:
						if mouse_position[0] < 500 and mouse_position[1] < 500:
							add_npc(mouse_position)
							print("block_to_insert = ")
							print(block_to_insert)
							print("mouse_position = ")
							print(mouse_position)

		screen.fill((SCREEN_FILL_COLOR))

		if backbtn_rect.contains(mouse_rect):
			building=False
			startscreen(True,status="start",score=0)
			#return False

		if undonpc_rect.contains(mouse_rect):
			delete_path()

		
		screen.blit(pygame.image.load('savebtn.png').convert(),savebtn_rect)
		screen.blit(pygame.image.load('backbtn.png').convert(),backbtn_rect)
		screen.blit(pygame.image.load('undobtn.png').convert(),undonpc_rect)

		for block in selector_blocks:
			block.display(screen)
		
		for asset in bassets:
			asset.display_level_rects(screen)

		for cleaners in bcleaner_assets:
			cleaners.display_level_rects(screen)
		
		for npc in bnpc_assets:
			npc.automove(screen)

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
