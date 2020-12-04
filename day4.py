
class Passport(dict):

	"""
	Class to hold passport details of the individuals (if missing default to none)
	Inherits from dict so call and assignment methods already in place 
	"""

	# class variables - shared among all instances of the class
	total_number_passports                 = 0
	total_number_valid_passports_nonstrict = 0
	total_number_valid_passports_strict    = 0

	def __init__(self, birth_yr=None, issue_yr=None, exp_yr=None, height=None, 
		hair_clr = None, eye_clr=None, passport_id=None, country_id=None):

		"""
		Initialisation function where dictionary values for each instance of Passport are filled
		Checks for validity of passports and updates class variables
		"""

		self['birth_yr']    = birth_yr
		self['issue_yr']    = issue_yr
		self['exp_yr']      = exp_yr
		self['height']      = height
		self['hair_clr']    = hair_clr
		self['eye_clr']     = eye_clr
		self['passport_id'] = passport_id
		self['country_id']  = country_id

		Passport.total_number_passports += 1

		self.check_valid_nonstrict()
		self.check_valid_strict()


	def check_valid_nonstrict(self):

		"""
		PART 1
		Check if passport is valid (non strict rules)
		Must have all the fields filled except country_id, which is optional
		Parameters:
			- self - the dictionary
		Returns:
			- True or False depending if valid or not
		"""

		if (self['birth_yr'] != None and self['issue_yr'] != None and self['exp_yr'] != None and 
			self['height'] != None and self['hair_clr'] != None and self['eye_clr'] != None and 
			self['passport_id'] != None):
			Passport.total_number_valid_passports_nonstrict += 1
			return True
		else:
			return False


	def check_valid_strict(self):

		"""
		PART 2
		Check if passport is valid (strict rules)
		Must have all the fields filled except country_id, which is optional
		Also require:
    		- birth_yr - four digits; at least 1920 and at most 2002.
    		- issue_yr - four digits; at least 2010 and at most 2020.
    		- exp_yr - four digits; at least 2020 and at most 2030.
    		- height - a number followed by either cm or in:
        		If cm, the number must be at least 150 and at most 193.
        		If in, the number must be at least 59 and at most 76.
    		- hair_clr - a # followed by exactly six characters 0-9 or a-f.
    		- eye_clr - exactly one of: amb blu brn gry grn hzl oth.
    		- passport_id - a nine-digit number, including leading zeroes.
		Parameters:
			- self - the dictionary
		Returns:
			- True or False depending if valid or not
		"""		

		# check if any are None
		if (self['birth_yr'] == None or self['issue_yr'] == None or self['exp_yr'] == None or 
			self['height'] == None or self['hair_clr'] == None or self['eye_clr'] == None or 
			self['passport_id'] == None):
			#print('One or more are None', self)
			return False
		
		# birth year
		if (len(self['birth_yr']) != 4 or
			int(self['birth_yr']) < 1920 or int(self['birth_yr']) > 2002):
			#print('bad birth year', self['birth_yr'])
			return False

		# issue year
		if (len(self['issue_yr']) != 4 or 
			int(self['issue_yr']) < 2010 or int(self['issue_yr']) > 2020):
			#print('bad issue year', self['issue_yr'])
			return False

		# expiration year
		if (len(self['exp_yr']) != 4 or
			int(self['exp_yr']) < 2020 or int(self['exp_yr']) > 2030):
			#print('bad expiration year', self['exp_yr'])
			return False

		# height
		if (self['height'][-2:] != 'cm' and self['height'][-2:] != 'in'):
			#print('bad height no cm or in', self['height'][-2:])
			return False
		if (self['height'][-2:] == 'cm' and 
			(int(self['height'][:-2]) < 150 or int(self['height'][:-2]) > 193)):
			#print('bad height cm', self['height'])
			return False
		if (self['height'][-2:] == 'in' and 
			(int(self['height'][:-2]) < 59 or int(self['height'][:-2]) > 76)):
			#print('bad height in', self['height'])
			return False

		# hair colour
		if (self['hair_clr'][0] != '#' or len(self['hair_clr']) != 7):
			#print('bad hair colour', self['hair_clr'])
			return False
		allowed_hair_colour_code_chars = '0123456789abcdef'
		for char in self['hair_clr'][1:7]:
			if char not in allowed_hair_colour_code_chars:
				#print('bad hair colour', self['hair_clr'])
				return False
		
		# eye colour
		if (self['eye_clr'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
			#print('bad eye colour', self['eye_clr'])
			return False

		# passport id
		if (len(self['passport_id']) != 9):
			#print('bad passport id', self['passport_id'])
			return False



		# if didn't return false in any if statements, passport is valid
		Passport.total_number_valid_passports_strict += 1
		return True



def get_individual_info(credential_list):

	"""
	Function that reads in the keys and values (combined as elements in credential_list)
	for each individual, parses them nicely and creates passport instances for individuals
	Parameters:
		- credential_list - array containing all available credentials of individual
	Returns:
		- passport - passport dictionary for an individual
	"""

	# initialise passport credentials to None
	birth_yr = issue_yr = exp_yr = height = hair_clr = eye_clr = passport_id = country_id = None

	# loop over credentials in list and split the key, value pairs (by colon) into dictionary items
	for credential in credential_list:

		try:
			key, value = credential.split(':')
		except:
			print('Could not extract key and value for individual')
			print('Problematic credential is', credential)
			break

		# match key, value pairs with code names in file
		if key == 'byr':
			birth_yr = value
		elif key == 'iyr':
			issue_yr = value
		elif key == 'eyr':
			exp_yr = value
		elif key == 'hgt':
			height = value
		elif key == 'hcl':
			hair_clr = value
		elif key == 'ecl':
			eye_clr = value
		elif key == 'pid':
			passport_id = value
		elif key == 'cid':
			country_id = value
		else:
			print('Unknowkn key in individual:', key, ':', value)

	# create a passport instance for the individual
	passport = Passport(birth_yr, issue_yr, exp_yr, height, hair_clr, eye_clr, passport_id, country_id)
	
	return passport



def read_process_passport_file(filename):

	"""
	Read in a file with passport info.
	New individuals are separated by blank lines
	Credential information for an individal is represented as a sequence of key:value pairs 
	separated by spaces or newlines
	Parameters:
		- filename to read in
	Returns
		- all_passports - container array that stores the passports for all individuals
	"""

	all_passports = []    # passport list for all individuals
	credential_list = []  # temporary passport list for one individual

	# open and read in file

	passport_file = open(filename, 'r')
	lines = passport_file.readlines()

	for line in lines:

		# if have a blank line (or at end of file), means we have reached end of 
		# an individual's info, so save passport info for current individual 
		# and reset credential list

		if line == '\n' or line == lines[-1]:

			# case where at end of file, want to save that last line
			if line == lines[-1]:
				# remove newlines at end of lines and split by whitespace
				line = line.strip()
				credential_list.append(line.split())
			
			# each line for an individual results in a list, so end up with a list of lists
			# flatten the list to 1D

			credential_list = [item for sublist in credential_list for item in sublist]
			passport = get_individual_info(credential_list)
			all_passports.append(passport)
			credential_list = []
			continue
		
		# if don't have blank line or not at end of file, means we are still on same
		# individual so keep reading in their passport info

		else:
			# remove newlines at end of lines and split by whitespace
			line = line.strip()
			credential_list.append(line.split())


	return all_passports








### 
### MAIN CODE to read in passport file and call the functions that do the verification checks
### 

all_passports = read_process_passport_file('day4_passports.txt')

#for passport in all_passports:
#	print(passport)

print('Total number of passports =', Passport.total_number_passports)
print('Total number of valid passports (non strict requirements) =', Passport.total_number_valid_passports_nonstrict)
print('Total number of valid passports (strict requirements) =', Passport.total_number_valid_passports_strict)