def get_seat_number_from_boarding_string(boarding_string):

	"""
	Get the seat number from the row string of 10 chars
	First 7 chars tell you about the row number
	Last 3 chars tell you about the column number
	Each letter tells you which half of a region the given seat is in
	F in row_string means front (1st half of row range)
	B in row_string means back  (2nd half of row range)
	F in row_string means front (1st half of column range)
	B in row_string means back  (2nd half of column range)

	For example, consider the boarding_string FBFBBFFRLR:

	First 7 chars:
	- Start by considering the whole range, rows 0 through 127
	- F means to take the lower half, keeping rows 0 through 63
	- B means to take the upper half, keeping rows 32 through 63
	- F means to take the lower half, keeping rows 32 through 47
	- B means to take the upper half, keeping rows 40 through 47
	- B keeps rows 44 through 47
	- F keeps rows 44 through 45
	- The final F keeps the lower of the two, row 44

	Last 3 chars:
	- Start by considering the whole range, columns 0 through 7
	- R means to take the upper half, keeping columns 4 through 7
	- L means to take the lower half, keeping columns 4 through 5
	- The final R keeps the upper of the two, column 5


	Parameters:
		- row_string: the 7 chars that specify the row number
	Returns:
		- row_number: the row number (must be between 0 and 128)
	"""

	# initialise upper and lower limits for row and column number
	row_lower_limit = 0
	row_upper_limit = 127
	col_lower_limit = 0
	col_upper_limit = 7
	
	# loop over boarding_string to get the row and column number
	for char in boarding_string:

		# ROWS: front (1st half of region)
		if char == 'F':
			row_upper_limit = (row_lower_limit+row_upper_limit-1)/2

		# ROWS: back (2nd half of region)
		elif char == 'B':
			row_lower_limit = (row_lower_limit+row_upper_limit+1)/2

		# COLUMNS: front (1st half of region)
		elif char == 'L':
			col_upper_limit = (col_lower_limit+col_upper_limit-1)/2

		# COLUMNS: back (2nd half of region)
		elif char == 'R':
			col_lower_limit = (col_lower_limit+col_upper_limit+1)/2

	# if algorithm worked correctly, row_lower_limit must equal row_upper_limit at and of iterations
	assert row_lower_limit == row_upper_limit, 'row number could not be determined'

	# same for columns
	assert col_lower_limit == col_upper_limit, 'column number could not be determined'

	row_number = row_lower_limit
	col_number = col_lower_limit

	seat_number = row_number*8 + col_number
	return int(seat_number)




def get_boarding_string_from_seat_number(seat_number):

	"""
	Inverse of above function to get boarding pass string from seat number

	Parameters:
		- seat_number: the integer seat number
	Returns:
		- boarding_string: boarding pass string

	"""

	# initialise upper and lower limits for row and column number
	row_lower_limit = 0
	row_upper_limit = 127
	col_lower_limit = 0
	col_upper_limit = 7

	boarding_string = ''

	col_number = (seat_number)%8
	row_number = (seat_number - col_number)/8

	#print(seat_number, row_number, col_number)

	# determine row string
	for i in range(0, 7):

		# first half of region
		if row_number < (row_lower_limit+row_upper_limit+1)/2:
			boarding_string += 'F'
			row_upper_limit = (row_lower_limit+row_upper_limit-1)/2
		
		# second half of region
		elif row_number >= (row_lower_limit+row_upper_limit+1)/2:
			boarding_string += 'B'
			row_lower_limit = (row_lower_limit+row_upper_limit+1)/2

		#print(row_lower_limit, row_upper_limit)


	# determine column string
	for i in range(0, 3):

		# first half of region
		if col_number < (col_lower_limit+col_upper_limit+1)/2:
			boarding_string += 'L'
			col_upper_limit = (col_lower_limit+col_upper_limit-1)/2
		
		# second half of region
		elif col_number >= (col_lower_limit+col_upper_limit+1)/2:
			boarding_string += 'R'
			col_lower_limit = (col_lower_limit+col_upper_limit+1)/2

		#print(col_lower_limit, col_upper_limit)

	# if algorithm worked correctly, row_lower_limit must equal row_upper_limit at and of iterations
	assert row_lower_limit == row_upper_limit, 'row boarding code could not be determined'

	# same for columns
	assert col_lower_limit == col_upper_limit, 'column boarding code could not be determined'

	return boarding_string










###
### MAIN CODE
###

# read the boarding passes file
file_boardingpasses = open('day5_boardingpasses.txt', 'r')

# array to hold all the seat numbers
filled_seat_numbers = []

# loop through the file and fill in the seat_numbers array
for line in file_boardingpasses:

	# get the seat number from the boarding pass code
	line = line.strip()
	seat_number = get_seat_number_from_boarding_string(line)
	
	# consistency check - in getting seat_number from boarding_string, can we use
	# inverse function to get boarding_string back from seat_number
	assert line == get_boarding_string_from_seat_number(seat_number), "boarding pass string calculated from seat_number does not match original boarding pass string in file"

	# fill array with seat number
	filled_seat_numbers.append(seat_number)





# PART 1

# get the maximum value of the seat number in the filled_seat_numbers array
print('Highest seat number filled =', max(filled_seat_numbers))








# PART 2

# get my missing seat number

# create array of all POSSIBLE SEAT NUMBERS
all_possible_seat_numbers = [i for i in range(max(filled_seat_numbers)+1)]

# convert the filled and possile seat numbers to sets and calculate 
# the difference between the two to show possible empty seats
all_possible_seat_numbers_set = set(all_possible_seat_numbers)
filled_seat_numbers_set = set(filled_seat_numbers)
unfilled_seat_numbers_set = all_possible_seat_numbers_set.difference(filled_seat_numbers_set)

# catch is some of the seats at the very front and back of the plane don't exist 
# on this aircraft, so they'll show up in the above unfilled_seat_numbers_set.
# but my seat wasn't at the very front or back though - the seats with
# IDs +1 and -1 from yours will be in my list.

# so if numbers in unfilled set go up sequentially by one, 
# these are seats not existing on this flight
unfilled_seat_numbers_list = list(unfilled_seat_numbers_set)
unfilled_seat_number = None
for i in range(1, len(unfilled_seat_numbers_list)):
	
	# if missing numbers go up sequentially by one, ignore these
	if unfilled_seat_numbers_list[i] == unfilled_seat_numbers_list[i-1] + 1:
		continue

	# this is missing seat number
	else:
		unfilled_seat_number = unfilled_seat_numbers_list[i]
		print('My seat number =', unfilled_seat_numbers_list[i])




# get boarding string from seat number (as an extension)

boarding_string = get_boarding_string_from_seat_number(unfilled_seat_number)

# consistency check - if input the calculated boarding_string to the first function
# do we get back same seat_number
assert unfilled_seat_number == get_seat_number_from_boarding_string(boarding_string), "seat number calculated from determined boarding pass string does not match original seat number"

print('My boarding string =', boarding_string)
