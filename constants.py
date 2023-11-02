# constants
SCREENX = 550
SCREENY = 600
LEVSIZE=25
LEVNUMBERS=8
GAMEBLOCK_COLOR=[0,0,0]
GAMEGOAL_COLOR=[100,100,100]
SCREEN_FILL_COLOR=[255,255,255]
PLAYER1_SETUP=[75,75,5,3,3]
#CLEANER1_SETUP=[100,100,25,3,5]
# .3 easy .6 hard
DIFFICULTY_FACTOR=.5

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

#player setup
