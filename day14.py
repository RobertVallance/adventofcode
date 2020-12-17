

class Memory_allocations(dict):

	"""

	Class to assign values to given memory addresses
	Inherits from dict so assignment operators included by default
	NB __init__ function not needed

	"""


	def __str__(self):

		"""

		Function to print the dictionary in a nice form

		"""

		print('Memory allocations are:')
		for key, value in self.items():
			print(f'mem address = {key} \t value = {value}')

		# needed as cannot return None type
		return ''


	def sum_values(self):

		"""

		Function to return the sum of the values at the memory addresses in the class dictionary

		"""
		
		return sum(self.values())





	def set_memory_value(self, memory_address_decimal, decimal_number, mask, part_number):

		"""

		Funcion to assign a number (which is masked) to a memory address

		Parameters
		----------
		- self (the dictionary instance of all the memory allocations)
		- memory_address_decimal (the memory address - an integer decimal number - we assign to)
		- decimal_number (the number assigned to the memory address as-is or after modification in part_1)
		- mask (a string which is the mask we compare our number with)
		- part_number (whether this is 'part_1' or 'part_2' of the problem)

		"""

		# recast decimal_number from a string to an integer
		decimal_number = int(decimal_number)

		# PART 1
		if part_number == 'part_1':

			# first convert given decimal number to binary number
			binary_number = decimal_to_binary(decimal_number)

			# now mask it to get a new binary number
			masked_binary_number = self.get_masked_binary_number_part_1(mask, binary_number)

			# finally convert the masked binary number to a decimal number
			masked_decimal_number = binary_to_decimal(masked_binary_number)

			# assign new masked_decimal_number to our memory address using dictionary notation
			self[memory_address_decimal] = masked_decimal_number


		# PART 2
		elif part_number == 'part_2':

			# convert the memory address to binary format
			memory_address_binary = decimal_to_binary(memory_address_decimal)

			# now mask it to get the new memory addresses
			masked_memory_addresses_decimal = self.get_masked_memory_address_part_2(mask, memory_address_binary)

			# for each memory address in the list, assign decimal_number to that memory address
			for masked_memory_addresses_decimal in masked_memory_addresses_decimal:

				# assign new masked_decimal_number to our memory address using dictionary notation
				self[masked_memory_addresses_decimal] = decimal_number

		



	def get_masked_binary_number_part_1(self, mask, binary_number):

		"""

		USED IN PART 1

		Convert a given binary number into a new binary number using the mask

		Parameters
		----------
		- self (the dictionary instance of all the memory allocations)
		- mask (a string which is the mask we compare the binary_number to)
		- binary_number (the as yet unmasked value we mask)

		Returns
		-------
		- masked_binary_number (a new binary number that is masked with mask)

		"""
	
		# initialise new masked binary number
		masked_binary_number = '' 

		# use mask to convert binary_number into masked_binary_number:
		# X means mask has no effect
		# 0 means mask converts binary digit at that position to 0
		# 1 means mask converts binary digit at that position to 1
		for i in range(len(mask)):
			
			if mask[i] == 'X':
				masked_binary_number +=  binary_number[i]
			elif mask[i] == '0':
				masked_binary_number += '0'
			elif mask[i] == '1':
				masked_binary_number += '1'


		return masked_binary_number



	def get_masked_memory_address_part_2(self, mask, memory_address_binary):

		"""

		USED IN PART 2

		Convert a given binary number into a new memory address number using the mask
		Now can have floating point numbers

		Parameters
		----------
		- self (the dictionary instance of all the memory allocations)
		- mask (a string which is the mask we compare the memory addres to)
		- memory_address_binary (the starting memory address - binary form - we apply the mask to)

		Returns
		-------
		- masked_memory_addresses_decimal (list of new memory addresses we will apply value to)

		"""
	
		# initialise new masked memory address
		masked_memory_address_binary = '' 

		# use mask to convert binary_number into new masked_memory_address:
		# X means mask converts binary digit at that point to floating X
		# 0 means mask has no effect on binary digit at that posision
		# 1 means mask converts binary digit at that position to 1
		for i in range(len(mask)):
			
			if mask[i] == 'X':
				masked_memory_address_binary +=  'X'
			elif mask[i] == '0':
				masked_memory_address_binary += memory_address_binary[i]
			elif mask[i] == '1':
				masked_memory_address_binary += '1'

		# now convert floating point digits into all possibilities (have 2^(num_x_counts) possibilities)
		num_x_counts = masked_memory_address_binary.count('X')
		num_possibilities = 2**num_x_counts
		
		# create list of all possible combinations of X values (0 or 1 for each X value)
		# there will be a total of num_possibilities possible combinations
		# e.g. for 3 X values, have 2^3 = 8 combinations, which are:
		# [000, 001, 010, 011, 100, 101 110, 111]
		combinations = []
		for i in range(num_possibilities):
			combinations.append(decimal_to_binary(i)[len(masked_memory_address_binary)-num_x_counts:])

		# initialise list for new masked memory addresses
		masked_memory_addresses_decimal = []
		
		# get out all possible combinations of memory addresses
		# use all possible combinations, where nth position number for an element in combinations
		# corresponds to the nth instance of X in memory_address_binary
		for i in range(num_possibilities):

			new_masked_memory_address_binary = masked_memory_address_binary
			
			# replace each X value with the number in a combination in turn
			for j in range(num_x_counts):
				new_masked_memory_address_binary = new_masked_memory_address_binary.replace('X', combinations[i][j], 1)

			masked_memory_addresses_decimal.append(binary_to_decimal(new_masked_memory_address_binary))



		return masked_memory_addresses_decimal





# 2 GENERAL FUNCTIONS OUTSIDE CLASS TO DO BINARY-DECIMAL CONVERSIONS

def binary_to_decimal(binary_number):

	"""

	Convert binary numbers to decimal numbers
	Easiest to work with binary number in string format and loop backwards

	Parameters
	----------
	- binary_number (the input binary number)

	Returns
	-------
	- decimal_number (the converted binary number to decimal)

	"""

	# ensure binary number is a string
	binary_number = str(binary_number)

	decimal_number = 0  # initialise decimal_number
	j = 0               # counter for power of 2

	# convert binary number to decimal number
	for i in range(len(binary_number)-1, -1, -1):

		decimal_number += 2**(j) * int(binary_number[i])
		j += 1


	return decimal_number


def decimal_to_binary(decimal_number):

	"""

	Convert decimal numbers to binary numbers
	Assumes working with 36-bit numbers

	Parameters
	----------
	- decimal_number (the input decimal number)

	Returns
	-------
	- binary_number (the converted decimal number to binary in 36-bits)

	"""

	# ensure decimal_number is an integer (not string)
	decimal_number = int(decimal_number)
	
	# used to calculate how much of the decimal number is not yet accounted for in each step
	# of the upcoming for loop
	decimal_number_unaccounted_for = decimal_number

	# initialise binary number
	binary_number = ''

	# convert decimal number to binary number
	for i in range(35, -1, -1):

		if (2**i) > decimal_number_unaccounted_for:
			binary_number += '0'
		else:
			binary_number += '1'
			decimal_number_unaccounted_for -= 2**i


	return binary_number




###
### MAIN CODE
###

if __name__ == '__main__':

	# initialise class dictionaries (one for each part of the task) to hold our memory addresses and numbers
	memory_allocations_part_1 = Memory_allocations()
	memory_allocations_part_2 = Memory_allocations()

	# initilise mask and memory_address - these are updated straight away so are dummy here
	mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
	memory_address = 0

	# open and loop over bitmask file
	with open('day14_bitmask.txt') as bitmask_file:

		for line in bitmask_file:

			# if line starts with 'mask', then we are updating the mask
			if line.startswith('mask'):

				# get 3rd part of line separated by spaces e.g. 00110X11X0000110X0000001000111010X00
				mask = line.split()[2]
			
			# if line starts with 'mem', then we are updating a memory location with a new value
			elif line.startswith('mem'):

				# get first part of line e.g. mem[39993]
				memory_string = line.split()[0]

				# extract number from this e.g. 39993
				memory_address = memory_string[4:-1]

				# decimal_number is 3rd part of line separated by spaces e.g. 276
				decimal_number = line.split()[2]

				# update dictionaries
				memory_allocations_part_1.set_memory_value(memory_address, decimal_number, mask, 'part_1')
				memory_allocations_part_2.set_memory_value(memory_address, decimal_number, mask, 'part_2')



print(memory_allocations_part_1)
print(memory_allocations_part_2)
print('PART 1 sum of values in memory =', memory_allocations_part_1.sum_values())
print('PART 2 sum of values in memory =', memory_allocations_part_2.sum_values())