
import copy
import math


def number_binomial_combinations(n, r):

	"""
	
	Get number of total ordered combinations that we may need to iterate over for part 2

	Parameters
	----------
	- n (length of array)
	- r (size of subset of array)


	Returns
	-------
	- how many combinations there are for a subset of size r in array of size n

	"""


	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))



def tribonacci_map(length):

	"""

	Translate a sequence of numbers with interval of 1 into all possible ordered combinations
	where first and last number must remain fixed and an interval between two numbers in a combination
	cannot be larger than 3. This follows a tribonacci sequence. 
	Function maps list length to fibonnaci combination size

	Parameters
	----------
	- length (length of array)

	Returns
	-------
	- number of unique ordered fibonacci combinations for that array length

	"""

	tribonacci_dict = {0:0, 1:1, 2:1, 3:2, 4:4, 5:7, 6:13, 7:24, 8:81,
					   9:149, 10:274, 11:504, 12:927, 13:1705, 14:3136,
					   15:5768, 16:10609, 17:19513}
	
	return tribonacci_dict[length]



def count_valid_combinations(adaptors, combinations_count, combinations_list):

	"""

	Computer expensive way to calculate all valid ordered combinations of lists that match the rules:
	- intervals between numbers in subsets cannot be > 3
	- first and last number in subset must be same as first and last number in original list

	Parameters
	----------
	- adaptors (ordered list of adaptors, including charging outlet joltage and device's 
		built-in joltage adaptor)
	- combinations_count (initial number of combinations - user sets to 1 at parent level 
		as full array itself is a valid combination)
	- combinations_list (initial combinations - user sets to [adaptors] at parent level
		as full array itself is a valid comination)

	Returns
	-------
	- combinations_count (total number of valid combinations - 
		added to continuously throughout function from original count of 1)
	- combinations_list (list of all valid combinations - 
		appended to continuously throughout function from original entry of [adaptors])

	""" 

	# start with all combinations and progressively remove one at a time for all combinations
	# if can remove an element, use recursion to remove another, etc.

	# must keep first and last element of adaptors, hence range bounds 1 to len-1
	for i in range(1, len(adaptors)-1):

		# remove an element (element i) from adaptors
		temp_adaptors = adaptors[0:i] + adaptors[i+1:]

		# calculate intervals between numbers in temp_adaptors
		intervals = [temp_adaptors[i]-temp_adaptors[i-1] for i in range(1, len(temp_adaptors))]

		# if any interval is > 3 or the combination has already been tested (and shown valid)
		# skip adding to count and adding temo_adaptors to combinations_list 
		if any(interval>3 for interval in intervals) or temp_adaptors in combinations_list:
			continue
		
		# else we have a valid combination so add one to count and append combination to combinations_list
		# then continue recursion with the temp_adaptors list
		else:
			combinations_count += 1
			combinations_list.append(temp_adaptors)
			combinations_count, combinations_list = count_valid_combinations(temp_adaptors, combinations_count, combinations_list)


	return combinations_count, combinations_list



def count_valid_combinations_fast(adaptors):

	"""

	Same function as above mut much faster using tribonacci sequence giving O(n) speed

	Parameters
	----------
	- adaptors (ordered list of adaptors, including charging outlet joltage and device's 
		built-in joltage adaptor)

	Returns
	-------
	- combinations_count (total number of valid combinations)

	"""


	# first put numbers that have intervals of 1 between them in their own lists
	# lists separated by interval of 3 separate the lists
	# NB never have intervals of two in original adaptors list
	adaptors_separated = []

	# ensure first element of adaptors goes into adaptors_separated list
	list_of_numbers_separated_by_1_temp = [adaptors[0]]

	# put numbers that have intervals of 1 between them in their own lists
	for i in range(1, len(adaptors)):

		if adaptors[i]-adaptors[i-1] == 1:
			list_of_numbers_separated_by_1_temp.append(adaptors[i])
		else:
			adaptors_separated.append(list_of_numbers_separated_by_1_temp)
			list_of_numbers_separated_by_1_temp = [adaptors[i]]

	# ensure last elements of adaptors go into adaptors_separated list
	adaptors_separated.append(list_of_numbers_separated_by_1_temp)

	# calculate total combinations for each (interval of 1) sublist in adaptors_separate using tribonacci map
	# put the total combinations for each sublist as elements in a list
	adaptors_separated_combination_count_list = []
	for element in adaptors_separated:
		adaptors_separated_combination_count_list.append(tribonacci_map(len(element)))

	# final overall number of combinations is multiple of all elements in above list
	combinations_count = math.prod(adaptors_separated_combination_count_list)

	return combinations_count











###
### MAIN CODE
###

if __name__ == '__main__':

	# read in file of adaptors, adding in charging outlet joltage of [0] and sorting in ascending order
	#adaptors = sorted([0] + list(map(int, open('test.txt', 'r').readlines())))
	adaptors = sorted([0] + list(map(int, open('day10_adaptors.txt', 'r').readlines())))

	# add in device's built-in joltage adaptor, which is rated 3 higher than the highest-rated adaptor
	adaptors.append(max(adaptors) + 3)
	print('adaptors =', adaptors)



	# PART 1
	# Find a chain that uses all of the adaptors to connect the charging outlet 
	# to the device's built-in adaptor and count the joltage differences between 
	# the charging outlet, the adapters, and the device. 
	# What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

	intervals_between_adaptors = [adaptors[i]-adaptors[i-1] for i in range(1, len(adaptors))]
	number_intervals_of_1_times_number_intervals_of_3 = \
		 intervals_between_adaptors.count(1)*intervals_between_adaptors.count(3)
	print('PART 1 number intervals of 1 times number intervals of 3 =', number_intervals_of_1_times_number_intervals_of_3)



	# PART 2
	# What is the total number of distinct ways you can arrange the adaptors
	# to connect the charging outlet to the device?
	# Remember any given adaptor can take an input 1, 2, or 3 jolts 
	# lower than its rating and still produce its rated output joltage

	# first see how many possible ordered conbinations we might have to run over
	total_combinations = sum([number_binomial_combinations(len(adaptors), i) for i in range(1, len(adaptors))])
	#print(total_combinations)

	# if total_combinations is small, can use expensive method, which also returns 
	# a list of the valid combinations
	if (total_combinations < 1000):

		combinations_count = 1
		combinations_list = copy.deepcopy([adaptors])

		combinations_count, combinations_list = count_valid_combinations(adaptors, combinations_count, combinations_list)
		
		for combination in combinations_list:
			print(combination)


	# if huge number, use tribonacci method, which is quick and gives count
	# but doesn't give a list of valid combinations
	else:
		combinations_count = count_valid_combinations_fast(adaptors)


	print('PART 2 number unique combinations =', combinations_count)

