
import math

def shuttle_found(depart_time, shuttle_numbers_filtered):

	"""

	USED IN PART 1

	Determine whether a shuttle will arrive at the depart_time time stamp

	Parameters
	----------
	- depart_time (a time when we will be at the stop)
	- shuttle_numbers_filtered (list of shuttle ID numbers - filtered out 'x' buses)

	Returns
	-------
	- depart time (equal to input parameter if match found)
	- shuttle_number (equal to shuttle ID where match found)

	"""

	# loop over all shuttle numbers and see if the depart_time is exactly divisible by the ID
	for shuttle_number in shuttle_numbers_filtered:

		# match found so return values
		if depart_time%shuttle_number == 0:
			return depart_time, shuttle_number

	# no match found so return default values
	return -1, -1 




def calc_earliest_timestamp(intervals, shuttle_numbers_unfiltered, shuttle_numbers_filtered):

	"""

	USED IN PART 2

	Use Chinese remained theorem to calculate earliest timestamp such that 
	the first bus ID departs at that time and each subsequent listed bus ID departs 
	at that subsequent minute

	See https://www.dave4math.com/mathematics/chinese-remainder-theorem/
	for proof

	Parameters
	----------
	- intervals (time interval between earliest_timestamp and shuttle bus departure)
	- shuttle_bus_numbers_unfiltered (list of shuttle ID numbers - includes 'x' buses)
	- shuttle_numbers_filtered (list of shuttle ID numbers - filtered out 'x' buses)

	Returns
	-------
	earliest_timestamp (earliest timestamp that meets the requirements)

	"""

	# multiply all shuttle bus numbers (these are prime) 
	N = math.prod(shuttle_numbers_filtered)

	# n are the set of shuttle bus numbers
	n = shuttle_numbers_filtered

	# a are the remainders of timestamp % shuttle bus number
	a = []
	for i in range(len(shuttle_numbers_unfiltered)):

		# ignore shuttles that are 'x'
		if shuttle_numbers_unfiltered[i] == 'x':
			continue
		else:
			# get remainder
			remainder = (int(shuttle_numbers_unfiltered[i]) - intervals[i]%int(shuttle_numbers_unfiltered[i])) % int(shuttle_numbers_unfiltered[i])
			print(remainder)
			a.append(remainder)

	# nbar are N divided by the elements in n
	nbar = [int((N/shuttle_number)) for shuttle_number in shuttle_numbers_filtered] # convert to int as otherwise get precision errors with huge numbers!
																					# should be int anyway

	# u are the smallest numbers where the nbar values % shuttle bus numbers equal one
	u = []
	for i in range(len(shuttle_numbers_filtered)):

		for j in range(shuttle_numbers_filtered[i]):

			if (nbar[i]*j % shuttle_numbers_filtered[i]) == 1:
				u.append(j)
				break

	# earliest timestamp given by sum(a[i]*nbar[i]*u[i] for all i) % N
	earliest_timestamp = int(sum(a[i]*nbar[i]*u[i] for i in range(len(a))) % N)

	return earliest_timestamp







###
### MAIN CODE
###

if __name__ == '__main__':

	# read in shuttle file
	with open('day13_shuttles.txt', 'r') as shuttle_file:
	#with open('test2.txt', 'r') as shuttle_file:

		# first line is  earliest time you can leave port
		earliest_depart_time = int(shuttle_file.readline().strip())
		
		# second line is shuttle numbers, split by commas
		shuttle_numbers = shuttle_file.readline().strip().split(',')




	# PART 1
	# see which shuttle will arrive first when we get to port

	# remove all out of service shuttles (designated x)
	shuttle_numbers_filtered = list(filter(lambda char: char != 'x', shuttle_numbers))

	# convert shuttle numbers to ints
	shuttle_numbers_filtered = list(map(int, shuttle_numbers_filtered))


	print(earliest_depart_time, shuttle_numbers_filtered)


	# initialise vars for while loop
	shuttle_and_time_found = False
	depart_time = earliest_depart_time

	# keep adding 1 to depart_time until a matching shuttle found
	while not shuttle_and_time_found:

		time, shuttle_number = shuttle_found(depart_time, shuttle_numbers_filtered)

		# match found so break out of loop 
		if shuttle_number != -1:
			shuttle_and_time_found = True
		
		# match not found so continue looping and add 1 to depart_time
		else:
			depart_time += 1


	print(depart_time, shuttle_number)
	print('PART 1 ID*TIME WAITED =', shuttle_number*(depart_time-earliest_depart_time))





	# PART 2

	# for this part, we keep the shuttles that are out of service (designated 'x')
	shuttle_numbers_unfiltered = shuttle_numbers
	print(shuttle_numbers_unfiltered)

	# in shuttle_numbers, timestamps must go t, t+1, t+2, t+3, ...
	# so interval of 1 between each number (including x's)
	# e.g. shuttle_numbers = [17, x, 13, 19] -> [t, t+1, t+2, t+3]
	intervals = [i for i in range(len(shuttle_numbers_unfiltered))]
	print(intervals)


	earliest_timestamp = calc_earliest_timestamp(intervals, shuttle_numbers_unfiltered, shuttle_numbers_filtered)
	print('PART 2 EARLIEST TIMESTAMP =', earliest_timestamp)