import copy


def terrain_expand(terrain_orig_array, terrain_array):

	"""
	If trajectory reaches the right-most end of the pattern, want to repeat it
	So add on original terrain to current terrain
	Parameters:
	 	- terrain_orig_array: original terrain, before any expansions to it
		- terrain_array: terrain, which could already be expanded
	Returns:
		new expanded terrain
	"""

	for i in range(len(terrain_orig_array)):

		terrain_array[i] += terrain_orig_array[i]

	return terrain_array


def perform_trajectory(terrain_orig_array, x, y):

	"""
	Do the terrain trajectory, calling terrain_expand when reach width of terrain
	Parameters
		- terrain_orig: original terrain, before any expansions to it
		- x: x step in each path iteration
		- y: y step in each path iteration
	Returns:
		terrain with trajectory and number of trees hit
	"""

	# initialise trajectory position (in x)
	x_position = 0

	# initilaise terrain as original terrain (without expansion)
	# need deepcopy as otherwise terrain_array refers to terrain_orig_array and so terrain_orig_array is modified
	terrain_array = copy.deepcopy(terrain_orig_array)

	# initialise number of trees encountered
	number_trees_encountered = 0

	# perform the trajectory
	for y_position in range(0, len(terrain_orig_array), y):

		# ignore (0,0) as this is starting point - can't hit a tree
		if y_position == 0:
			continue

		# if x_position reaches edge of terrain, expand the terrain
		if x_position + x > len(terrain_array[0])-1:
			terrain_array = terrain_expand(terrain_orig_array, terrain_array)
		
		# incremenr x position
		x_position += x

		# specify whether trajectory doesn't hit a tree in row (.) or does hit a tree (#)
		# replace terrain_array with miss (O) or hit (X) symbol
		if terrain_array[y_position][x_position] == '.':
			terrain_array[y_position][x_position] = 'O'
		elif terrain_array[y_position][x_position] == '#':
			number_trees_encountered += 1
			terrain_array[y_position][x_position] = 'X'

		
	return terrain_array, number_trees_encountered



# read in the terrain

file_terrain = open('day3_terrain.txt', 'r')
terrain_orig_array = []

for line in file_terrain:

	# remove blank space including newline chars from lines
	line = line.strip()

	# put each char in line into a temporary array that itself goes into terrain_orig_array
	temp_line_array = []
	for char in line:
		temp_line_array.append(char)
	
	terrain_orig_array.append(temp_line_array)




# PART 1
# User chooses what x and y velocities are

# hard code for now the x (right) and y (down) slope
x = int(input('Enter an x velocity: '))
y = int(input('Enter a y velocity: '))

print('\nORIGINAL TERRAIN:')
for row in terrain_orig_array:
	print(''.join(row))

terrain_array, number_trees_encountered = perform_trajectory(terrain_orig_array, x, y)

print('\nFINAL TERRAIN WITH TRAJECTORY:')
for row in terrain_array:
	print(''.join(row))

print('\nNumber trees hit =', number_trees_encountered)



# PART 2
# Choose preset trajectories and multiply number of trees from each

terrain_array_1, number_trees_encountered_1 = perform_trajectory(terrain_orig_array, 1, 1)
terrain_array_2, number_trees_encountered_2 = perform_trajectory(terrain_orig_array, 3, 1)
terrain_array_3, number_trees_encountered_3 = perform_trajectory(terrain_orig_array, 5, 1)
terrain_array_4, number_trees_encountered_4 = perform_trajectory(terrain_orig_array, 7, 1)
terrain_array_5, number_trees_encountered_5 = perform_trajectory(terrain_orig_array, 1, 2)

print('\nPart 2 number = ', number_trees_encountered_1*number_trees_encountered_2*number_trees_encountered_3*number_trees_encountered_4*number_trees_encountered_5)