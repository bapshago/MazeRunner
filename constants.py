
# constants
SCREENX = 550
SCREENY = 600
LEVSIZE=25
LEVNUMBERS=8
GAMEBLOCK_COLOR=[0,0,0]
GAMEGOAL_COLOR=[100,100,100]
SCREEN_FILL_COLOR=[255,255,255]
PLAYER1_SETUP=[75,75,5,3,3,'player.png']
NPC_PENALTY=10
#NPC_SPEED must be divisable by 25
NPC_SPEED=5
#CLEANER1_SETUP=[100,100,25,3,5]
# .3 easy .6 hard
DIFFICULTY_FACTOR=.5

#Game Assets
GAMEBLOCKS=[1,'brick_wall_25x25.png',False,False,False]
GAMEGOAL=[2,'black_white.png',True,True,True]
GAMEBLOCKBREAKABLE=[3,'brick_wall_25x25.png',True,False,False]
LEVELBUILDINGBLOCK=[9,'blank.png',True,False,False]

#NPC Assets
NPC1=[25,25,25,5,'npc.png']

#GAME_ASSETS=[GAMEBLOCKS,GAMEGOAL,GAMEBLOCKBREAKABLE,GAMECLEANERS]
GAME_ASSETS=[GAMEBLOCKS,GAMEGOAL,GAMEBLOCKBREAKABLE,LEVELBUILDINGBLOCK]
NPC_ASSETS=[NPC1]

#CLEANER Assets
CLEANER_IMAGES = ['cleaner.png','cleaner1.png','cleaner2.png','cleaner3.png','cleaner4.png','cleaner5.png','cleaner6.png','cleaner7.png']
CLEANER1 = [4,CLEANER_IMAGES,False,False,False,10,10]
CLEANER_ASSETS = [CLEANER1]

#Level Builder Selectors (pos_x, pos_y,rectsize,image_file,asset_id)


#setup variables
current_pos = None
last_pos = None
move_x_neg = False
move_x_pos = False
move_y_neg = False
move_y_pos = False
running = True
selectedlev = 0
timer=0
timerswitch = False

#levelbuilder setup
block_to_insert=0
mouse_position=[]
print_once=True
build_once=True
CUSTOMLEVELTHUMBIMAGE='customlevel.png'



