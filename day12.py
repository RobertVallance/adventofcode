
import math

def update_facing_direction(current_degrees, value):

	"""

	USED IN PART 1

	Update the degree angle the ferry faces
	Negative value in argument means rotate anticlockwise
	Positive value in argument means rotate clockwise
	Define 0 degrees and north and 180 degrees as south
	Set bounds of 0 - 360 degrees so ensure wrap around these numbers

	Parameters
	----------
	- current_degrees (current facing position in degrees)
	- value (number of degrees to rotate ferry by)

	Returns
	-------
	facing_direction (angle in degrees the ship is facing)
	
	"""

	facing_direction = (current_degrees + value)%360 

	return facing_direction



def ferry_position_part_1(directions_list):

	"""
	
	USED IN PART 1

	Update position of ferry based on following rules:
	- Action N means to move north by the given value
	- Action S means to move south by the given value
	- Action E means to move east by the given value
	- Action W means to move west by the given value
	- Action L means to turn left the given number of degrees
	- Action R means to turn right the given number of degrees
	- Action F means to move forward by the given value in the direction the ship is currently facing

	Parameters
	----------
	- directions_list (list of directions where each element is a tuple of action and value)

	Returns
	-------
	- manhattan_distance (distance metric of final position of ferry)


	"""

	# set initial co-ordinates of ferry
	x_position = y_position = 0

	# ship starts by facing east
	facing_direction = 90

	# loop over directions instructions
	for line in directions_list:

		# separate action and value in line
		action, value = line
		print(action, value)

		# update position boat is facing (if action = L, R) so x and y position can be updated correctly
		if action == 'L':
			facing_direction = update_facing_direction(facing_direction, -value)
		elif action == 'R':
			facing_direction = update_facing_direction(facing_direction, +value)

		# update x and y position of ferry (if action = N, S, E, W) 
		elif action == 'N':
			y_position += value
		elif action == 'S':
			y_position -= value
		elif action == 'E':
			x_position += value
		elif action == 'W':
			x_position -= value 

		# upate direction according to current direction facing (if faction = F)
		elif action == 'F':
			x_position += value*round(math.sin(math.radians(facing_direction)))
			y_position += value*round(math.cos(math.radians(facing_direction)))


		print(f'[{x_position}, {y_position}] {facing_direction} deg')

	# return ship's Manhattan distance - sum of the absolute values of its east/west 
	# position and its north/south position
	manhattan_distance = abs(x_position) + abs(y_position)

	return manhattan_distance



def ferry_position_part_2(directions_list):


	"""
	
	USED IN PART 2

	Now use waypoint (coordinates relative to ferry's position) to update ferry position

	Update position of ferry based on following rules:
	- Action N means to move the waypoint north by the given value
	- Action S means to move the waypoint south by the given value
	- Action E means to move the waypoint east by the given value
	- Action W means to move the waypoint west by the given value
	- Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees
	- Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees
	- Action F means to move forward to the waypoint a number of times equal to the given value

	Parameters
	----------
	- directions_list (list of directions where each element is a tuple of action and value)

	Returns
	-------
	- manhattan_distance (distance metric of final position of ferry)


	"""

	# set initial co-ordinates of ferry 
	x_position = y_position = 0
	
	# initial waypoint is 10 units east and 1 unit north relative to the ship
	x_waypoint = x_position + 10
	y_waypoint = y_position + 1


	# loop over directions instructions
	for line in directions_list:

		# separate action and value in line
		action, value = line
		print(action, value)

		# offset between waypoint and ferry
		x_diff_waypoint_position = x_waypoint - x_position
		y_diff_waypoint_position = y_waypoint - y_position

		# rotate position of waypoint (if action = L or R) relative to ferry position
		# x' = xcos(theta) - ysin(theta)
		# y' = ycos(theta) + xsin(theta)
		# above formula assume rotation is anticlockwise by value
		# so for clockwise rotation, use negaive of the value in the above formulae
		if action == 'L':
			x_waypoint = x_position + x_diff_waypoint_position*round(math.cos(math.radians(value))) \
									- y_diff_waypoint_position*round(math.sin(math.radians(value)))
			y_waypoint = y_position + y_diff_waypoint_position*round(math.cos(math.radians(value))) \
									+ x_diff_waypoint_position*round(math.sin(math.radians(value)))
		elif action == 'R':
			x_waypoint = x_position + x_diff_waypoint_position*round(math.cos(math.radians(-value))) \
									- y_diff_waypoint_position*round(math.sin(math.radians(-value)))
			y_waypoint = y_position + y_diff_waypoint_position*round(math.cos(math.radians(-value))) \
									+ x_diff_waypoint_position*round(math.sin(math.radians(-value)))

		# update x and y position of waypoint (if action = N, S, E, W) 
		elif action == 'N':
			y_waypoint += value
		elif action == 'S':
			y_waypoint -= value
		elif action == 'E':
			x_waypoint += value
		elif action == 'W':
			x_waypoint -= value 

		# only if action = F do we update the ferry position
		elif action == 'F':	
			x_position += x_diff_waypoint_position * value
			x_waypoint = x_position + x_diff_waypoint_position
			y_position += y_diff_waypoint_position * value
			y_waypoint = y_position + y_diff_waypoint_position

		print(f'SHIP [{x_position}, {y_position}]')
		print(f'WAYPOINT [{x_waypoint}, {y_waypoint}]')		


	# return ship's Manhattan distance - sum of the absolute values of its east/west 
	# position and its north/south position
	manhattan_distance = abs(x_position) + abs(y_position)
	
	return manhattan_distance





###
### MAIN CODE
###

if __name__ == "__main__":

	# read in file of directions and split each line into a tuple of th action and the value
	directions_list = [(line[0], int(line[1:])) for line in open('day12_directions.txt').readlines()]
	#directions_list = [(line[0], int(line[1:])) for line in open('test.txt').readlines()]


	# PART 1
	# calculate Manhattan distance assuming instructions from part 1
	manhattan_distance_part_1 = ferry_position_part_1(directions_list)
	print('PART 1 Manhattan distance =', manhattan_distance_part_1)
	print()


	# PART 2
	# calculate Manhattan distance assuming instructions from part 2
	manhattan_distance_part_2 = ferry_position_part_2(directions_list)
	print('PART 2 Manhattan distance =', manhattan_distance_part_2)


