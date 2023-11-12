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
import json


#initiate Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREENX,SCREENY])

#inital build of game assets
selectedlev=8
assets=[]
selector_blocks=[]
selector_blockcount=0
for asset_to_load in GAME_ASSETS:
	assets.append(Game_asset(asset_to_load[0],asset_to_load[1],asset_to_load[2],asset_to_load[3],asset_to_load[4],selectedlev))
	selector_blocks.append(Selectorblock(25*selector_blockcount,550,LEVSIZE,asset_to_load[1],asset_to_load[0]))
	selector_blockcount=selector_blockcount+1
npc_assets=[]
for npc in NPC_ASSETS:
	npc_assets.append(Npc(npc[0],npc[1],npc[2],npc[3],npc[4],LEVELS[selectedlev],LEVELS_NPC[selectedlev]))
	selector_blocks.append(Selectorblock(25*selector_blockcount,550,LEVSIZE,npc[4],npc[3]))
	selector_blockcount=selector_blockcount+1

cleaner_assets=[]
for cleaners in CLEANER_ASSETS:
	cleaner_assets.append(Cleaner_asset(cleaners[0],cleaners[1],cleaners[2],cleaners[3],cleaners[4],cleaners[5],cleaners[6],selectedlev))
	selector_blocks.append(Selectorblock(25*selector_blockcount,550,LEVSIZE,cleaners[1][1],cleaners[0]))
	selector_blockcount=selector_blockcount+1

savebtn_rect=pygame.Rect(0,575,25,25)

intro_trigger = True

updateblock=Blockselector(0,0,1)

def block_change(pos,block_to_in):
	global assets
	global cleaner_assets
	global block_to_insert

	updateblock.x=pos[0]
	updateblock.y=pos[1]
	updateblock.update()
	
	if updateblock.x < 500 and updateblock.y < 500:
		if not block_to_in==5:
			asset_counter=0
			for asset in assets:
				if collision_detect(asset.rects,updateblock.rect) > -1:
					rect_to_move=assets[asset_counter].rects[collision_detect(asset.rects,updateblock.rect)]
					del assets[asset_counter].rects[collision_detect(asset.rects,updateblock.rect)]
					asset_counter_del=asset_counter
				asset_counter=asset_counter+1
			cleaner_counter=0
			for cleaners in cleaner_assets:
				if collision_detect(cleaners.rects,updateblock.rect) > -1:
					rect_to_move=cleaner_assets[cleaner_counter].rects[collision_detect(cleaners.rects,updateblock.rect)]
					del cleaner_assets[cleaner_counter].rects[collision_detect(cleaners.rects,updateblock.rect)]
					cleaner_counter_del=cleaner_counter
				cleaner_counter=cleaner_counter+1
			asset_counter2=0
			replaced_block=False
			replaced_cleaner=False
			for asset in assets:
				if asset.asset_id==block_to_in:
					assets[asset_counter2].rects.append(rect_to_move)
					replaced_block=True
				asset_counter2=asset_counter2+1
			cleaner_counter2=0
			for cleaners in cleaner_assets:
				if cleaners.asset_id==block_to_in:
					cleaner_assets[cleaner_counter2].rects.append(rect_to_move)
					replaced_block=True
				cleaner_counter2=cleaner_counter2+1
			if not replaced_block:
				assets[asset_counter_del].rects.append(rect_to_move)
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
	for npc in npc_assets:
		npc.paths_list.append([npc.paths_list[-1][0],[npc_x_cord,npc_y_cord]])
		print(npc.paths_list)

def delete_path():
	for npc in npc_assets:
		if len(npc.paths_list) > 2:
			del npc.paths_list[-1]
			npc.pathscount = npc.pathscount-1
			print(npc.paths_list)

def convert_rects_to_matrix():
	list_of_assets=[]
	for asset in assets:
		for rect in asset.rects:
			list_of_assets.append([asset.asset_id,rect])
	for asset in cleaner_assets:
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
	for npc in npc_assets:
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

def startscreen(intro_trigger,status="Levelbuild",score=0):
	while intro_trigger:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					intro_trigger = False
					return False

		screen.fill((SCREEN_FILL_COLOR))

		if status=="start":
			caption = str('Maze Runner - Press space bar to start')
		if status=="loss":
			caption = str('Maze Runner - You lost! - '+ str(score) +' -  Press space bar to start')
		if status=="win":
			caption = str('Maze Runner - You won! - '+ str(score) +' - Press space bar to start')
		if status=="Levelbuild":
			caption = str('Maze Runner - Level Builder!')
		pygame.display.set_caption(caption)	
		pygame.display.flip()
		clock.tick(60)  # 60 FPS

while running:
	intro_trigger = startscreen(intro_trigger)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				mouse_position = event.pos
				if not block_to_insert==5 or mouse_position[1] > 500:
					block_change(mouse_position,block_to_insert)
				else:
					if mouse_position[0] < 500 and mouse_position[1] < 500:
						add_npc(mouse_position)

		if event.type == pygame.KEYDOWN:
			timerswitch=True
			if event.key == pygame.K_a:
				block_to_insert = 9
			if event.key == pygame.K_s:
				block_to_insert = 1
			if event.key == pygame.K_d:
				block_to_insert = 2
			if event.key == pygame.K_f:
				block_to_insert = 3
			if event.key == pygame.K_g:
				block_to_insert = 4
			if event.key == pygame.K_z:
				block_to_insert = 5
			if event.key == pygame.K_x:
				if print_once:
					delete_path()
			if event.key == pygame.K_p:
				if print_once:
					convert_rects_to_matrix()
					print_once=False

	screen.fill((SCREEN_FILL_COLOR))
	
	screen.blit(pygame.image.load('savebtn.png').convert(),savebtn_rect)

	for block in selector_blocks:
		block.display(screen)
	
	for asset in assets:
		asset.display_level_rects(screen)

	for cleaners in cleaner_assets:
		cleaners.display_level_rects(screen)
	
	for npc in npc_assets:
		npc.automove(screen)

	pygame.display.flip()		
	clock.tick(60)  # 60 FPS

pygame.quit()
