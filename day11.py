import copy


def fill_seat(seat, surrounding_seats, tolerance):

	"""
	
	Determine whether a given seat abides by rules by looking at 8 surrounding seats

	USED IN PARTS 1 AND 2

	Parameters
	----------
	- seat (the seat in question)
	- surrounding_seats (the other seats the person can see at the seat position)
	- tolerance (how many occupied surrounding seats the person can tolerate being full 
		and for them to sit there)

	Returns
	-------
	- seat_new (the status of the seat un question - filled, unfilled, or same as before)

	"""


	# if seat currently empty and all surrounding seats unfilled, fill the chair
	if seat == 'L' and surrounding_seats.count('#') == 0:
		seat_new = '#'

	# if seat occupied and (tolerance) or more seats adjacent to it are also occupied, the seat now becomes empty
	elif seat == '#' and surrounding_seats.count('#') >= tolerance:
		seat_new = 'L'

	# otherwise, seat does not change	
	# including if seat is a floor seat, no-one ever sits in this so keep empty
	else:
		seat_new = seat

	return seat_new





def fill_seats_part_1(seats):

	"""
	
	USED IN PART 1

	For all seats, see if the seat will now be filled based on the NEAREST 8 neighbours
	Calls fill_seat function for each seat

	Parameters
	----------
	- seats (2D array of seats before being refilled)

	Returns
	-------
	- seats_new (refilled 2D seats array)

	"""

	# empty array to hold refilled seats 
	seats_new = []

	# loop over 2D array of seats
	for i in range(len(seats)):

		seat_row_new = []

		for j in range(len(seats[0])):

			# intialise 8 surrounding seat statuses
			upper_left_seat = upper_middle_seat = upper_right_seat = \
				middle_left_seat = middle_right_seat = \
				lower_left_seat = lower_middle_seat = lower_right_seat = '-'


			# if i = (first or last element in array) or j = (first of last element in array)
			# account for missing seats above, below, left or fight of the seats
			# set the above strings as empty
			if i == 0:
				upper_left_seat = upper_middle_seat = upper_right_seat = ''
			if i == len(seats)-1:
				lower_left_seat = lower_middle_seat = lower_right_seat = ''
			if j == 0:
				upper_left_seat = middle_left_seat = lower_left_seat = ''
			if j == len(seats[0])-1:
				upper_right_seat = middle_right_seat = lower_right_seat = ''

			# if not boundary seats, then fill the 8 surrounding seats as we would expect 
			if upper_left_seat != '':
				upper_left_seat = seats[i-1][j-1] 
			if upper_middle_seat != '':
				upper_middle_seat = seats[i-1][j]
			if upper_right_seat != '':
				upper_right_seat = seats[i-1][j+1]
			if middle_left_seat != '':
				middle_left_seat = seats[i][j-1]
			if middle_right_seat != '':
				middle_right_seat = seats[i][j+1]
			if lower_left_seat != '':
				lower_left_seat = seats[i+1][j-1]
			if lower_middle_seat != '':
				lower_middle_seat = seats[i+1][j]
			if lower_right_seat != '':
				lower_right_seat = seats[i+1][j+1]

			# put chars of 8 surrounding seats into one string
			surrounding_seats = upper_left_seat + upper_middle_seat + upper_right_seat + \
								middle_left_seat                    + middle_right_seat  + \
								lower_left_seat + lower_middle_seat + lower_right_seat

			#print(surrounding_seats)

			# call fill_seat function for each seat. pass string of surrounding_seats to function
			# in part 1, tolerance = 4
			seat_row_new.append(fill_seat(seats[i][j], surrounding_seats, 4))

		seats_new.append(seat_row_new)

	return seats_new








def fill_seats_part_2(seats):

	"""
	
	USED IN PART 2

	For all seats, see if the seat will now be filled based on the 8 SEEN neighbours
	Calls fill_seat function for each seat

	Parameters
	----------
	- seats (2D array of seats before being refilled)

	Returns
	-------
	- seats_new (refilled 2D seats array)

	"""

	# empty array to hold refilled seats 
	seats_new = []


	# loop over 2D array of seats
	for i in range(len(seats)):

		seat_row_new = []

		for j in range(len(seats[0])):

			# initialise parameters

			upper_left_seats_can_see = upper_middle_seats_can_see = upper_right_seats_can_see = \
				middle_left_seats_can_see = middle_right_seats_can_see = \
				lower_left_seats_can_see = lower_middle_seats_can_see = lower_right_seats_can_see = '-'

			upper_left = upper_middle = upper_right = \
				middle_left = middle_right = \
				lower_left = lower_middle = lower_right = ''

			# upper left diagonal first
			# look at all diagonal left seats from seat.
			# if come across a '#', then set upper_left_seats_can_see = '#' and break out
			# but if come across an 'L' first, then this blocks any '#'s further away, 
			# so break out and set upper_left_seats_can_see = ''.
			# also if reach bounds of array, then break out to avoid undefined behaviour
			for k in range(1, len(seats)*len(seats[0])):
				if (i-k >= 0 and j-k >= 0):
					upper_left = seats[i-k][j-k]
					if upper_left == '#':
						upper_left_seats_can_see = '#'
						break
					elif upper_left == 'L':
						upper_left_seats_can_see = ''
						break
				else:
					break

			# upper middle
			for k in range(1, len(seats)):
				if (i-k >= 0):
					upper_middle = seats[i-k][j]
					if upper_middle == '#':
						upper_middle_seats_can_see = '#'
						break
					elif upper_middle == 'L':
						upper_middle_seats_can_see = ''
						break
				else:
					break
				
			# upper right diagonal
			for k in range(1, len(seats)*len(seats[0])):
				if (i-k >= 0 and j+k < len(seats[0])):
					upper_right = seats[i-k][j+k]
					if upper_right == '#':
						upper_right_seats_can_see = '#'
						break
					elif upper_right == 'L':
						upper_right_seats_can_see = ''
						break
				else:
					break

			# middle left
			for k in range(1, len(seats[0])):
				if (j-k >= 0):
					middle_left = seats[i][j-k]
					if middle_left == '#':
						middle_left_seats_can_see = '#'
						break
					elif middle_left == 'L':
						middle_left_seats_can_see = ''
						break
				else:
					break

			# middle right
			for k in range(1, len(seats[0])):
				if (j+k < len(seats[0])):
					middle_right = seats[i][j+k]
					if middle_right == '#':
						middle_right_seats_can_see = '#'
						break
					elif middle_right == 'L':
						middle_right_seats_can_see = ''
						break
				else:
					break

			# lower left diagonal
			for k in range(1, len(seats)*len(seats[0])):
				if (i+k < len(seats) and j-k >= 0):
					lower_left = seats[i+k][j-k]
					if lower_left == '#':
						lower_left_seats_can_see = '#'
						break
					elif lower_left == 'L':
						lower_left_seats_can_see = ''
						break
				else:
					break

			# lower middle
			for k in range(1, len(seats)):
				if (i+k < len(seats)):
					lower_middle = seats[i+k][j]
					if lower_middle == '#':
						lower_middle_seats_can_see = '#'
						break
					elif lower_middle == 'L':
						lower_middle_seats_can_see = ''
						break
				else:
					break

			# lower right diagonal
			for k in range(1, len(seats)*len(seats[0])):
				if (i+k < len(seats) and j+k < len(seats[0])):
					lower_right = seats[i+k][j+k]
					if lower_right == '#':
						lower_right_seats_can_see = '#'
						break
					elif lower_right == 'L':
						lower_right_seats_can_see = ''
						break
				else:
					break


			# put chars of 8 seen seats into one string
			surrounding_seats = upper_left_seats_can_see + upper_middle_seats_can_see + upper_right_seats_can_see + \
								middle_left_seats_can_see                             + middle_right_seats_can_see  + \
								lower_left_seats_can_see + lower_middle_seats_can_see + lower_right_seats_can_see

			#print(surrounding_seats)

			# call fill_seat function for each seat. pass string of surrounding_seats to function
			# in part 2, tolerance = 5
			seat_row_new.append(fill_seat(seats[i][j], surrounding_seats, 5))


		seats_new.append(seat_row_new)

	return seats_new




# read in seating arrangement and put in 2D array
seats = [[seat for seat in line.strip()] for line in open('day11_seats.txt').readlines()]





# PART 1
# fill seats until they no longer change with part 1 rules

seats_old = copy.deepcopy(seats)
seats_new = fill_seats_part_1(seats_old)

while seats_new != seats_old:
	seats_old = copy.deepcopy(seats_new)
	seats_new = fill_seats_part_1(seats_old)


for line in seats_new:
	print(''.join(line))

print('Final seats occupied PART 1 =', sum(line.count('#') for line in seats_new))





# PART 2
# fill seats until they no longer change with part 2 rules

seats_old = copy.deepcopy(seats)
seats_new = fill_seats_part_2(seats_old)

"""
for line in seats_old:
	print(''.join(line))
print()
	
for line in seats_new:
	print(''.join(line))
print()
"""

while seats_new != seats_old:
	seats_old = copy.deepcopy(seats_new)
	seats_new = fill_seats_part_2(seats_old)

	"""
	for line in seats_new:
		print(''.join(line))
	print()
	"""

for line in seats_new:
	print(''.join(line))

print('Final seats occupied PART 2 =', sum(line.count('#') for line in seats_new))
