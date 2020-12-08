
def principal_bag_contains_shiny_gold_bag_new(principal_bag, line_i, lines):

	"""
	Determine whether a given principal bag will eventually contain a shiny gold bag
	Use recursion - count number of contained bags in the principal bag
	and then reset the principal bag to a contained bag and repeat

	Parameters
	----------
	principal_bag - the name of the principal bag
	
	line_i - the current line of text in the file where the bag in question is the parent bag
	e.g. if principal_bag = 'shiny bag', then line_i could be:
	'shiny gold bags contain 4 drab blue bags, 4 posh purple bags, 2 drab silver bags, 4 wavy turquoise bags.'
	
	lines - all the lines of the bag file (needed to do matching of contained bags in a principal bag 
	to their own respective entries as principal bags)
	e.g.  priniciapal bag = 'shiny gold bags contain 4 drab blue bags, 4 posh purple bags, 2 drab silver bags, 4 wavy turquoise bags.'
	so will match '4 drab blue bags' later to 
	'drab blue bags contain 5 dull salmon bags.'
'

	Returns
	-------
	principal_bag_contained_bags - list of bags contained in prinicpal bag

	contains_shiny_gold - whether above list contains a shiny gold bag

	"""

	# initialise list to contain bags contained within principal bag and whether list contains shiny gold bag
	principal_bag_contained_bags = []
	contains_shiny_gold = False

	# contained bags defined as fourth word onwards in line_i - set to string
	contained_bags = ' '.join(line_i.split()[4:])

	# remove final full stop on contained_bags string
	contained_bags = contained_bags.replace('.', '')

	# separate the contained bags split by comma and put in list
	contained_bags = contained_bags.split(', ')
	
	# loop over contained bags in principal bag 
	for contained_bag in contained_bags:

		# if the contained bag is empty, stop iterating for this contained bag
		if contained_bag == 'no other bags':
			continue

		# append bag contained by principal bag to principal_bag_contained_bags list
		principal_bag_contained_bags.append(contained_bag)

		# reset principal bag to the contained bag (forget about number of them for now)
		principal_bag = ' '.join(contained_bag.split()[1:3])
		
		# match up new principal bag with its respective line in lines (the bag file)
		for line_j in lines:

			# just get the first two elements (the principal bag name) in the lines (bag file)
			line_principal_bag = ' '.join(line_j.split()[:2])

			# matching found
			if principal_bag == line_principal_bag:
				line_i = line_j
		
		# recursively call the principal_bag_contains_shiny_gold_bag_new function
		# to see if our list contains 'shiny gold' - if so then break out
		principal_bag_contained_bags_temp, contains_shiny_gold = principal_bag_contains_shiny_gold_bag_new(principal_bag, line_i, lines)
		principal_bag_contained_bags += [item for item in principal_bag_contained_bags_temp if item not in principal_bag_contained_bags] 
		for item in principal_bag_contained_bags:
			if 'shiny gold' in item:
				contains_shiny_gold = True
				break


	return principal_bag_contained_bags, contains_shiny_gold









# OLD DEPRECATED FUNCTION THAT USES WHILE LOOP INTSEAD OF RECURSION
def principal_bag_contains_shiny_gold_bag_old(principal_bag, line_i, lines):


	"""
	Determine whether a given principal bag will eventually contain a shiny gold bag
	Uses while loop to keep iteraing over child bags (and appending them to a list)
	until no more bags are contained by the parent bag

	Parameters
	----------

	principal_bag - the name of the principal bag
	
	line_i - the current line of text in the file where the bag in question is the parent bag
	e.g. if principal_bag = 'shiny bag', then line_i could be:
	'shiny gold bags contain 4 drab blue bags, 4 posh purple bags, 2 drab silver bags, 4 wavy turquoise bags.'
	
	lines - all the lines of the bag file (needed to do matching of contained bags in a principal bag 
	to their own respective entries as principal bags)
	e.g.  priniciapal bag = 'shiny gold bags contain 4 drab blue bags, 4 posh purple bags, 2 drab silver bags, 4 wavy turquoise bags.'
	so will match '4 drab blue bags' later to 
	'drab blue bags contain 5 dull salmon bags.'


	Returns
	-------

	principal_bag_contained_bags - list of bags contained by the principal bag

	contains_shiny_gold - bool of whether the principal bag eventually contains a shiny gold bag


	"""


	# initialise parameters
	contains_shiny_gold = False
	continue_iterating = True

	# contained bags defined fourth word onwards in line (and remove final full stop on line)
	principal_bag_contained_bags = ' '.join(line_i.split()[4:])
	principal_bag_contained_bags = principal_bag_contained_bags.replace('.', '')

	# separate the contained bags split by comma
	principal_bag_contained_bags = principal_bag_contained_bags.split(', ')

	while continue_iterating:

		original_contained_bags_length = len(principal_bag_contained_bags)

		# iterate over our contained bags for a given parent bag
		for bag in principal_bag_contained_bags:

			bag_name = ' '.join(bag.split()[1:3])

			# iterate over all parent bags in file
			# if a principal bag in the file matches one of our contained bags,
			# then add the containter of this principal bag to our current container
			for line_j in lines:

				principal_bag_name_in_file 		   = ' '.join(line_j.split()[:2])
				contained_by_principal_bag_in_file = ' '.join(line_j.split()[4:])
				contained_by_principal_bag_in_file = contained_by_principal_bag_in_file.replace('.', '')
				contained_by_principal_bag_in_file = contained_by_principal_bag_in_file.split(', ')
				

				# if have a match, append new principal bag to list
				if principal_bag_name_in_file == bag_name:

					# only need to append if bag doesn't alread exist in list - otherwise will continue iteration for no reason
					principal_bag_contained_bags = principal_bag_contained_bags + [bag for bag in contained_by_principal_bag_in_file if bag not in principal_bag_contained_bags]
					


		# if we didn't append any more bags to this list, means we have 
		if len(principal_bag_contained_bags) == original_contained_bags_length:
			continue_iterating = False


	# remove item if it is 'no other bags'
	principal_bag_contained_bags.remove('no other bags')

	# check if 'shiny gold' exists in the list - if so then principal bag contains a shiny gold bag
	for item in principal_bag_contained_bags:
		if 'shiny gold' in item:
			contains_shiny_gold = True
			break

	return principal_bag_contained_bags, contains_shiny_gold






def count_number_bags_in_princpal_bag(principal_bag, line_i, lines):

	"""
	Count the total number of bags contained within a given principal bag
	Use recursion - count number of contained bags in the principal bag
	and then reset the principal bag to a contained bag and repeat
	
	Calcualate the number of bags as:
	number principal bags + (number principal bags * number bags contained by principal bag)


	Parameters
	----------
	principal_bag - the name of the principal bag
	
	line_i - the current line of text in the file where the bag in question is the parent bag
	e.g. if principal_bag = 'shiny bag', then line_i could be:
	'shiny gold bags contain 4 drab blue bags, 4 posh purple bags, 2 drab silver bags, 4 wavy turquoise bags.'
	
	lines - all the lines of the bag file (needed to do matching of contained bags in a principal bag 
	to their own respective entries as principal bags)
	e.g.  priniciapal bag = 'shiny gold bags contain 4 drab blue bags, 4 posh purple bags, 2 drab silver bags, 4 wavy turquoise bags.'
	so will match '4 drab blue bags' later to 
	'drab blue bags contain 5 dull salmon bags.'
'

	Returns
	-------
	bag_count - the total number of bags that the uppermost principal bag contains

	"""

	# initialise bag count
	bag_count = 0

	# contained bags defined as fourth word onwards in line_i - set to string
	contained_bags = ' '.join(line_i.split()[4:])

	# remove final full stop on contained_bags string
	contained_bags = contained_bags.replace('.', '')

	# separate the contained bags split by comma and put in list
	contained_bags = contained_bags.split(', ')
	
	# loop over contained bags in principal bag 
	for contained_bag in contained_bags:
		
		# if the contained bag is empty, stop iterating for this contained bag
		if contained_bag == 'no other bags':
			continue

		# reset principal bag to the contained bag (forget about number of them for now)
		principal_bag = ' '.join(contained_bag.split()[1:3])
		
		# match up new principal bag with its respective line in lines (the bag file)
		for line_j in lines:

			# just get the first two elements (the principal bag name) in the lines (bag file)
			line_principal_bag = ' '.join(line_j.split()[:2])

			# matching found
			if principal_bag == line_principal_bag:
				line_i = line_j
		
		# recursively call the count_bags function
		# here contained_bag[0] is the number of bags of the new principal bag (first char in string is number)
		# and contained_bag becomes the new principal bag, remember
		# number of new principal bags + (number of new principal bags * number bags contained by principal bag)
		bag_count += int(contained_bag[0]) + int(contained_bag[0])*count_number_bags_in_princpal_bag(principal_bag, line_i, lines)
		#print(bag_count)

	return bag_count







###
### MAIN CODE
###

if __name__ == "__main__":

	# open bag file and loop over lines, appending bag colours to dictionary
	bag_file = open('day7_bagcolours.txt', 'r')
	lines = bag_file.readlines()

	principal_bags_containing_shiny_gold = 0

	for line_i in lines:

		line_i = line_i.strip()

		# principal bag defined by first two words in line_i
		principal_bag  = ' '.join(line_i.split()[:2])




		# PART 1
		# how many of the principal bags eventually contain a shiny gold bag

		# DEPRECATED FUNCTION WITHOUT RECURSION
		#principal_bag_contained_bags, contains_shiny_gold = principal_bag_contains_shiny_gold_bag_old(principal_bag, line_i, lines)
		
		# NEW FUNCTION WITH RECURSION
		principal_bag_contained_bags, contains_shiny_gold = principal_bag_contains_shiny_gold_bag_new(principal_bag, line_i, lines)
		
		if contains_shiny_gold:
			print('\t', principal_bag, 'bag contains a shiny gold bag')
			principal_bags_containing_shiny_gold  += 1



		# PART 2
		# how many inidvidual bags are in the shiny gold principal bag
		
		if principal_bag == 'shiny gold':
			bag_count = count_number_bags_in_princpal_bag(principal_bag, line_i, lines)

		else:
			continue
			


	# print counts for PART 1 and PART 2
	print('Number principal bags containing shiny gold bags =', principal_bags_containing_shiny_gold )
	print('Number bags contained within a shiny gold bag = ', bag_count)