
import numpy as np
from itertools import product
import copy
import sys

# no limit on numpy print size
np.set_printoptions(threshold=sys.maxsize)



def populate_neighbours_inactive(arrangement_zALL):

	"""
	
	Put a default '.' for the neighbours of each cube (if that neighbour doesn't yet exist)
	Effectively puts a border pad of '.' around the current setup which we will consider next

	Parameters
	----------
	- arrangement_zALL (unpadded cube arrangement)

	Returns
	-------
	- padded cube arrangement

	""" 

	return np.pad(arrangement_zALL, pad_width=1)



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

	n_dimensions = arrangement_zALL.ndim

	# want to consider neighbours that are up to 1 co-ordinate away in ALL dimensions
	num_neighbours = 3**n_dimensions

	# want there to get all possible combinations of the three numbers [-1,0,1] for the neighbour
	# intervals between neighbour and element under consideration in arrangement_zALL
	neighbour_intervals = list(product([-1, 0, 1], repeat=n_dimensions))
	
	# remove neighbour intervals are 0 in every dimensions (as this is the element itself)
	neighbour_intervals.remove(tuple([0]*n_dimensions))

	arrangement_zALL_new = copy.deepcopy(arrangement_zALL)

	
	# loop over all elements in array
	for index_tuple, element in np.ndenumerate(arrangement_zALL):

		# see if any neighbours equal 1 ('#')
		# if so, add 1 to count_active_neighbours
		count_active_neighbours = 0
		
		# loop over all neighbour intervals
		for neighbour_interval in neighbour_intervals:

			# add neighbour interval to element index to get neighbour index
			neigbour_index = tuple(map(lambda x, y: x + y, index_tuple, neighbour_interval))

			# see if neighbour equals 1 ('#')
			# try statment as neighbour indices may go out of bounds on border cases
			try: 
				if arrangement_zALL[neigbour_index] == 1:
					count_active_neighbours += 1
			except:
				continue

		# if cube active and active neighbour count = 2 or 3, cube remains active,
		# else cube becomes inactive
		if element == 1:
			if count_active_neighbours in [2, 3]:
				arrangement_zALL_new[index_tuple] = 1
			else:
				arrangement_zALL_new[index_tuple] = 0

		# if cube inactive and active neighbour count =  3, cube becomes active,
		# else cube remains inactive
		elif element == 0:
			if count_active_neighbours == 3:
				arrangement_zALL_new[index_tuple] = 1
			else:
				arrangement_zALL_new[index_tuple] = 0


	
	return arrangement_zALL_new



def count_active_cubes(arrangement_zALL):

	"""

	Count the number of acive cubes (those that have status = #) in the arrangement

	Parameters
	----------
	- arrangement_zALL (arrangement of cubes)

	Returns
	-------
	- sum of active cubes in arrangement

	"""
	
	# flatten array into 1D and sum the 1s ('#'s)
	return np.sum(arrangement_zALL.flatten())



def char_to_int_map(row):

	"""

	Function to map chars '.' and '#' to ints 0 and 1, respectively

	Parameters
	----------
	- row (list of chars '.' and '#' corresponding to a row in the initial slice)

	Returns
	-------
	- new_row (new row with the replaced chars)

	"""

	new_row = []

	for element in row:
		if element == '.':
			new_row.append(0)
		elif element == '#':
			new_row.append(1)
		else:
			new_row.append(element)
	
	return new_row






###
### MAIN CODE
###

if __name__ == '__main__':

	# set hyperparameters
	test = False
	number_cycles = 6

	# read in initial state file and put in 2D array
	# this is a 2D slice of the full 3D or 4D space	
	if test:
		arrangement_z0 = [[cube for cube in line.strip()] for line in open('test.txt').readlines()]
	else:
		arrangement_z0 = [[cube for cube in line.strip()] for line in open('day17_initialstate.txt').readlines()]

	# convert chars in slice to 0s ('.') and 1s ('#') and recast as numpy array
	arrangement_z0 = np.array(list(map(char_to_int_map, arrangement_z0)))

	# put this slice as an element in a 3D (part 1) and 4D array (part 2)
	arrangement_zALL_3D = np.expand_dims(arrangement_z0, axis=0)
	arrangement_zALL_4D = np.expand_dims(arrangement_z0, axis=(0,1))


	# run the cycles
	for i in range(number_cycles):

		# pad the arrangements with zeros
		arrangement_zALL_3D = populate_neighbours_inactive(arrangement_zALL_3D)
		arrangement_zALL_4D = populate_neighbours_inactive(arrangement_zALL_4D)

		# make cubes become active or inactive depending on rules
		arrangement_zALL_3D = change_cubes_status(arrangement_zALL_3D)
		arrangement_zALL_4D = change_cubes_status(arrangement_zALL_4D)
		


	print('Final 3D arrangement =', arrangement_zALL_3D)
	print('Final 4D arrangement =', arrangement_zALL_4D)

	# get active cube counts
	active_cube_count_3D = count_active_cubes(arrangement_zALL_3D)
	active_cube_count_4D = count_active_cubes(arrangement_zALL_4D)
	print('PART 1 ACTIVE CUBE COUNT =', active_cube_count_3D)
	print('PART 2 ACTIVE CUBE COUNT =', active_cube_count_4D)

