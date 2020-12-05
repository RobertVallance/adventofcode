import copy
import time


# emoji symbols
emoji_tree = '\U0001F332'
emoji_sled = '\U0001f6f7'
emoji_boom = '\U0001f4a5'


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
		
		# increment x position
		x_position += x

		# specify whether trajectory doesn't hit a tree in row (.) or does hit a tree (#)
		# replace terrain_array with miss or hit symbol
		if terrain_array[y_position][x_position] == '.':
			terrain_array[y_position][x_position] = emoji_sled
		elif terrain_array[y_position][x_position] == emoji_tree:
			number_trees_encountered += 1
			terrain_array[y_position][x_position] = emoji_boom

		
	return terrain_array, number_trees_encountered



# read in the terrain

file_terrain = open('day3_random_terrain.txt', 'r')
terrain_orig_array = []

maxrows = 32

for j, line in enumerate(file_terrain):

	if j == maxrows:
		break

	# remove blank space including newline chars from lines
	line = line.strip()

	# put each char in line into a temporary array that itself goes into terrain_orig_array

	temp_line_array = []
	
	for char in line:
		
		# replace hashes with emoji for a tree
		if char == '#':
			char = emoji_tree

		temp_line_array.append(char)
	
	terrain_orig_array.append(temp_line_array)




# PART 1
# user chooses what x and y velocities are

x = int(input('Enter x velocity: '))
y = int(input('Enter y velocity: '))

#print('\nORIGINAL TERRAIN:')
#print()
#for row in terrain_orig_array:
#	print(''.join(row))

terrain_array, number_trees_encountered = perform_trajectory(terrain_orig_array, x, y)

print('\nFINAL TERRAIN WITH TRAJECTORY:')
print()

# print final terrain with sled at (0,0) first
for j in range(len(terrain_array)):

	printout = ''.join(terrain_array[j])
	printout = printout.replace(emoji_sled, '.')
	printout = printout.replace(emoji_boom, emoji_tree)
	
	# emoji_tree and emoji_sled take up two spaces so need to set all chars to do this
	printout = printout.replace('.', '. ')

	# for line zero, want to show the sled at (0,0)
	if j == 0:
		# need these if statments as tree takes up two chars and dot one char
		if printout[0] == '.': 			printout = emoji_sled + printout[2:]
		if printout[0] == emoji_tree:   printout = emoji_sled + printout[1:]
	print(printout)



# now go back to top of printed terrain - we will replace each terrain line with the sled (or boom) superimposed on top
for i in range(len(terrain_array)+1):
	print('\033[A' + '\033[A')



# print countdown from 3 to 1 and finally GO!!!
for i in reversed(range(1, 4)):
	print(i, end='\r')
	time.sleep(1)
print('GO!!!')



# now replace each terrain line so the character where sled is will be replaced by a sled (no hit) or boom (hit with tree)
# also replace line above the current one to the original without sled or boom
for j in range(len(terrain_array)):

	# replace line above current one with the original terrain_array line (without sled or boom) as sled no longer there
	# don't need to replace line above line zero (there isn't one to replace) so treat this as special case
	if j != 0:
		print('\033[A' + '\033[A')
		prev_printout = ''.join(terrain_array[j-1])
		prev_printout = prev_printout.replace(emoji_sled, '.')
		prev_printout = prev_printout.replace(emoji_boom, emoji_tree)
		prev_printout = prev_printout.replace('.', '. ')
		print(prev_printout)

	printout = ''.join(terrain_array[j])

	# emoji_tree and emoji_sled take up two spaces so need to set all chars to do this
	printout = printout.replace('.', '. ')
	
	# for line zero, want to show the sled at (0,0)
	if j == 0:
		# need these if statments as tree takes up two chars and dot one char
		if printout[0] == '.': 			printout = emoji_sled + printout[2:]
		if printout[0] == emoji_tree:   printout = emoji_sled + printout[1:]
	print(printout)
	
	# if sled has collision with tree (so there is emoji_boom in the line, then pause the animation)
	if emoji_boom in printout:
		time.sleep(0.5)
	time.sleep(0.2)

print('\nNumber trees hit =', number_trees_encountered, '\n')



# PART 2
# choose preset trajectories and multiply number of trees from each

terrain_array_1, number_trees_encountered_1 = perform_trajectory(terrain_orig_array, 1, 1)
terrain_array_2, number_trees_encountered_2 = perform_trajectory(terrain_orig_array, 3, 1)
terrain_array_3, number_trees_encountered_3 = perform_trajectory(terrain_orig_array, 5, 1)
terrain_array_4, number_trees_encountered_4 = perform_trajectory(terrain_orig_array, 7, 1)
terrain_array_5, number_trees_encountered_5 = perform_trajectory(terrain_orig_array, 1, 2)

print('\nPart 2 number = ', number_trees_encountered_1*number_trees_encountered_2*number_trees_encountered_3*number_trees_encountered_4*number_trees_encountered_5)
