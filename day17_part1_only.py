
import copy

def populate_neighbours_inactive(arrangement_zALL):

	"""
	
	Put a default '.' for the neighbours of each cube (if that neighbour doesn't yet exist)
	Effectively puts a border pad of '.' around the current setup which we will consider next

	Parameters
	----------
	- arrangement_zALL (unpadded cube arrangement)

	Returns
	-------
	- arrangement_zALL (overwritten cube arrangement that is now padded)

	""" 

	# get index of z=0 slice and number of rows and columns
	z0_index = int((len(arrangement_zALL)/2) - 0.5)
	number_rows = len(arrangement_zALL[z0_index])
	number_cols = len(arrangement_zALL[z0_index][0])
	
	# add new slices in 3rd dimension that are all '.' (also expanding their rows and cols by 2)
	new_slice_lower = [['.' for k in range(number_cols+2)] for j in range(number_rows+2)]
	new_slice_upper = [['.' for k in range(number_cols+2)] for j in range(number_rows+2)]
	arrangement_zALL.insert(0, new_slice_lower)
	arrangement_zALL.insert(len(arrangement_zALL), new_slice_upper)

	# now focus on inner slices - pad rows
	for i in range(1, len(arrangement_zALL)-1):

		arrangement_zALL[i].insert(0, ['.' for k in range(number_cols+2)])
		arrangement_zALL[i].insert(len(arrangement_zALL[0]), ['.' for k in range(number_cols+2)])

		# now focus on inner slices - pad cols	
		for j in range(1, len(arrangement_zALL[i])-1):

			arrangement_zALL[i][j].insert(0, '.')
			arrangement_zALL[i][j].insert(len(arrangement_zALL[i][j]), '.')
	

	return arrangement_zALL



def change_cubes_status(arrangement_zALL):

	"""

	Make cubes become active or inactive:
	During a cycle, all cubes SIMULTANEOUSLY change their state according to the following rules
	Simultaneous so fill new arrangement based on old one 
	(don't upate old one as a new entry will affect the following iteration) 
	- If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. 
	  Otherwise, the cube becomes inactive.
	- If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. 
	  Otherwise, the cube remains inactive.

	Parameters
	----------
	- arrangement_zALL (arrangement of cubes)

	Returns
	-------
	- arrangement_zALL_new (new arrangement of cubes following cycle)

	"""

	arrangement_zALL_new = copy.deepcopy(arrangement_zALL)

	# consider each cube in turn, remembering to include the border pad cubes too
	for i in range(0, len(arrangement_zALL)):
			for j in range(0, len(arrangement_zALL[i])):
				for k in range(0, len(arrangement_zALL[i][j])):

					# look at all 26 neighbours of the cube
					count_active_neighbours = 0
					for a in range(-1, 2):
						for b in range(-1, 2):
							for c in range(-1, 2):

								# at the cube in question so ignore
								if a == 0 and b == 0 and c == 0:
									continue
								
								# see if neighbours are '#'
								# try statment as indices may go out of bounds on border cases
								try:
									if arrangement_zALL[i+a][j+b][k+c] == '#':
										count_active_neighbours += 1
								except:
									continue

					# if cube active and active neighbour count = 2 or 3, cube remains active,
					# else cube becomes inactive
					if arrangement_zALL[i][j][k] == '#':
						if count_active_neighbours in [2, 3]:
							arrangement_zALL_new[i][j][k] = '#'
						else:
							arrangement_zALL_new[i][j][k] = '.'

					# if cube inactive and active neighbour count =  3, cube becomes active,
					# else cube remains inactive
					elif arrangement_zALL[i][j][k] == '.':
						if count_active_neighbours == 3:
							arrangement_zALL_new[i][j][k] = '#'
						else:
							arrangement_zALL_new[i][j][k] = '.'

	
	return arrangement_zALL_new


def count_active_cubes(arrangement_zALL):

	"""

	Count the number of acive cubes (those that have status = #) in the arrangement

	Parameters
	----------
	- arrangement_zALL (arrangement of cubes)

	Returns
	-------
	- active_cue_sum (sum of active cubes in arrangement)

	"""


	# intialise sum
	active_cube_sum = 0

	# loop over 3rd dimnesion, adding to count of '#' each time
	for i in range(len(arrangement_zALL)):
		active_cube_sum += sum([j.count('#') for j in arrangement_zALL[i]])
	
	return active_cube_sum
	





###
### MAIN CODE
###

if __name__ == '__main__':

	# set hyperparameters
	test = False
	number_cycles = 6

	# read in initial state file and put in 2D array
	# this is a 2D slice of the full 3D space	
	if test:
		arrangement_z0 = [[cube for cube in line.strip()] for line in open('test.txt').readlines()]
	else:
		arrangement_z0 = [[cube for cube in line.strip()] for line in open('day17_initialstate.txt').readlines()]

	# put this as an element in the 3D array
	arrangement_zALL = [arrangement_z0]

	# run the cycles
	for i in range(number_cycles):

		# pad the arrangement with zeros
		arrangement_zALL = populate_neighbours_inactive(arrangement_zALL)

		# make cubes become active or inactive depending on rules
		arrangement_zALL = change_cubes_status(arrangement_zALL)


	# get active cube count
	active_cube_count = count_active_cubes(arrangement_zALL)
	print('PART 1 ACTIVE CUBE COUNT =', active_cube_count)


# CODE OPTIMISED FOR PART 1 (3D only)
# EXTRA STAR IS TO INCUDE 4TH DIMENSION