import copy

def find_valid_and_not_valid_numbers(numbercyphers_list, preamble_length):

	"""
	
	Find values in numbercyphers_list where a pair of numbers (within the preamble range)
	fall sum to the number in numbercyphers_list under review
	This function iterates through all numbers in find_valid_and_not_valid_numbers
	and then calls check_if_valid_number function for each number
	If a matching pair is found, add number to valid_list
	Else add number to not_valid list

	USED FOR PART 1

	Parameters:
	-----------
	- numbercyphers_list (list of numbers in file)
	- preamble_length (how may numbers before the number in the list to consider)


	Returns:
	--------
	- valid_list (list of numbers where a pair in the preamble set sum to this number)
	- not_valid_list (list of numbers where a pair in the preamble set do not sum to this number)

	"""


	# initialise lists
	valid_list = []
	not_valid_list = []

	# check each number in the list 
	# (after just considering preamble numbers where we start indexing from index preamble_length)
	for i in range(preamble_length, len(numbercyphers_list)):

		if check_if_valid_number(numbercyphers_list[i], i, numbercyphers_list, preamble_length):
			valid_list.append(numbercyphers_list[i])
		else:
			not_valid_list.append(numbercyphers_list[i])

	return valid_list, not_valid_list




def check_if_valid_number(number, number_index, numbercyphers_list, preamble_length):

	"""
	
	Check if a pair of numbers in the premable set sum to the number in numbercyphers_list in question

	USED FOR PART 1

	Parameters:
	-----------
	- number (the number in numbercyphers_list being tested)
	- number_index (index of number in numbercyphers_list - needed for comparsion with preamble numbers)
	- preamble_length (how may numbers before the number in the list to consider)

	Returns:
	--------
	- True or False (depending on whether a pair sums to the number in question)

	"""

	# loop  over all pairs of preamble numbers
	for j in range(number_index-preamble_length, number_index-1):
		for k in range(j+1, number_index):
			
			# caluclate the sum of the pair of numbers and see if it matches the number under question
			sum_pair = numbercyphers_list[j] + numbercyphers_list[k]
			
			if sum_pair == number:
				return True

	# only if no match found return False
	return False



def find_sequences_of_numbners_summing_to_invalid_number(number, numbercyphers_list):

	"""

	For an invalid number found from part 1, find a contiguous set of at least two numbers
	in numbercyphers_list which sum to this invalid number

	USED FOR PART 2

	Parameters:
	-----------
	- number (the invalid number in numbercyphers_list)
	- numbercyphers_list (list of numbers in file)

	Returns:
	--------
	- valid_sequences (list of valid contiguous sets that sum to the invalid number - 
		could be more than 1 possibility in theory)

	"""

	# initialise list of valid sequences
	valid_sequences = []

	# remove number we are trying to sum to from list
	trial_numbercyphers_list = copy.deepcopy(numbercyphers_list)
	trial_numbercyphers_list.remove(number)


	# gather all possible slices of trial_numbercyphers_list where slice lenth >= 2
	for i in range(0, len(trial_numbercyphers_list)-1):
		for j in range(i+1, len(trial_numbercyphers_list)):
			
			lower_bound = i 
			upper_bound = j 

			#print(trial_numbercyphers_list[lower_bound:upper_bound+1])

			# check if sum of numbers in slice sums to the invalid number
			# if so - append slice to valid_sequences list
			if sum(trial_numbercyphers_list[lower_bound:upper_bound+1]) == number:

				valid_sequences.append(trial_numbercyphers_list[lower_bound:upper_bound+1])

	return valid_sequences



def find_best_valid_sequence_max_min_sum(valid_sequences):

	"""

	Find the sequence in valid_sequences list where the min + max value in the list
	is a minimum

	USED FOR PART 2

	Parameters:
	-----------	
	- valid_sequences (list of valid contiguous sets that sum to the invalid number

	Returns:
	--------
	- the minimum value of min + max value in the list of valid_sequences 

	"""


	for valid_sequence in valid_sequences:

		# initialise min(min + max value) to an arbitrary high value
		min_value = 9999999999

		# if max + min of slice in valid_sequencies is less than the smallest number so far, replace it
		max_min_sum = min(valid_sequence) + max(valid_sequence) 
		if max_min_sum < min_value:
			min_value = max_min_sum

	return min_value





###
### MAIN CODE
###

if __name__ == "__main__":

	# initialise list to hold the numbers
	numbercyphers_list = []

	# read in file that contains numbers and append to list
	#numbercyphers_file = open('test.txt', 'r')
	numbercyphers_file = open('day9_numbercyphers.txt', 'r')
	for line in numbercyphers_file:
		numbercyphers_list.append(int(line.strip()))




	# PART 1
	# find the first number in the numbercyphers_list (after the preamble = 25) 
	# which is not the sum of two of the 25 numbers before it. 
	# what is the first number that does not have this property?
	valid_list,  not_valid_list = find_valid_and_not_valid_numbers(numbercyphers_list, 25)
	print('first number that is not valid =', not_valid_list[0], '\n')

	# PART 2
	# find a contiguous set of at least two numbers in numbercyphers_list which sum to 
	# the invalid number from part 1
	# return the min + max value of this set
	# could be more than one possible set in theory so choose set where min + max value is a minumum
	# find valid sequence where min + max value is a minimum
	valid_sequences = find_sequences_of_numbners_summing_to_invalid_number(not_valid_list[0], numbercyphers_list)
	find_best_valid_sequence_max_min_sum = find_best_valid_sequence_max_min_sum(valid_sequences)
	print('best sequence where max + min value sums to that first invalid value =', find_best_valid_sequence_max_min_sum)








