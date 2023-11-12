from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from gamelevels import *

def convert_matrix(matrix_data):
	new_matrix_data = []
	for lines in matrix_data:
		new_matrix_data_row=[]
		for item in lines:
			if item == 0 or item == 2 or item == 4 or item==9:
				new_matrix_data_row.append(1)
			else:
				new_matrix_data_row.append(0)
		new_matrix_data.append(new_matrix_data_row)
		new_matrix_data_row=[]
	return new_matrix_data

def find_route(startx,starty,endx,endy,levelmap):
	matrix=convert_matrix(levelmap)
	grid = Grid(matrix=matrix)
	start=grid.node(startx,starty)
	end=grid.node(endx,endy)
	finder = AStarFinder()
	path,runs=finder.find_path(start,end,grid)
	newlist=[]
	for items in path:
		newlist.append([(items.x),(items.y)])
	return newlist




