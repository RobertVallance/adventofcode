
# containers to hold ticket rules and values
rules = {}
my_ticket = []
nearby_tickets = []

# open and read in file
with open('day16_tickets.txt', 'r') as tickets_file:
#with open('test.txt', 'r') as tickets_file:

	# use bank line count as a separator between rules, my ticket, and nearby tickets 
	blank_line_count = 0		
	
	for line in tickets_file:
		if line == '\n':
			blank_line_count += 1
			continue
		
		# rules
		if blank_line_count == 0:
			rule_title, rule = line.split(':')
			rule1, rule2 = rule.strip().split(' or ')
			rule1 = list(map(int, rule1.split('-'))); rule2 = list(map(int, rule2.split('-')))
			rules[rule_title] = [rule1, rule2]
		
		# my ticket
		if blank_line_count == 1:
			if 'your ticket' in line:
				continue
			else:
				my_ticket = list(map(int, line.strip().split(',')))

		# nearby tikets
		if blank_line_count == 2:
			if 'nearby tickets' in line:
				continue
			else:
				nearby_tickets.append(list(map(int, line.strip().split(','))))


#print(rules)




# PART 1
# find invalid tickets and sum their invalid numbers

# intialise invalid ticket entry sum and valid nearby ticket list
invalid_ticket_entry_sum = 0
valid_nearby_tickets_map = [1 for i in range(len(nearby_tickets))]

# loop over all nearby tickets
# if an element in the ticket does not fit in with ANY RULE AT ALL from dictionary, ticket is invalid
for i, nearby_ticket in enumerate(nearby_tickets):

	for entry in nearby_ticket:

		# intialise whether element is valid to False
		valid_entry = False
		for key, value in rules.items():
			
			# ticket element (entry) matches a dictionary rule so that element could be valid
			if (entry >= value[0][0] and entry <= value[0][1]) or (entry >= value[1][0] and entry <= value[1][1]):
				valid_entry = True
		
		# an element in the ticket has no value matching any rule so we know it is an invalid ticket
		# add this element to invalid_ticket_entry_sum
		if not valid_entry:
			invalid_ticket_entry_sum += entry
			valid_nearby_tickets_map[i] = 0


# return sum of elements across all tickets that are invalid
print('PART 1 INVALID TICKET ENTRY SUM =', invalid_ticket_entry_sum)

# just keep nearby tickets that are valid
valid_nearby_tickets = [nearby_tickets[i] for i in range(len(nearby_tickets)) if valid_nearby_tickets_map[i] == 1]






# PART 2
# find which field in tickets corresponds to which rule.
# once you work out which field is which, look for the six fields on your ticket 
# that start with the word departure. what do you get if you multiply those six values together?

# first initialise all rules to each field as possibilities
rule_element_correspondance = {rule_title: [i for i in range(len(valid_nearby_tickets[0]))] for rule_title in rules.keys()}

# loop over all rule titles
for key, value in rules.items():

	# loop over first element in each ticket, then second element, third etc
	for i in range(len(valid_nearby_tickets[0])):
		
		# loop over each ticket for that element
		for j in range(len(valid_nearby_tickets)):

			# if any ticket at element 0, 1, 2, etc doesn't work, then remove this element from the rule_element_correspondance key
			if (valid_nearby_tickets[j][i] < value[0][0]) or (valid_nearby_tickets[j][i] > value[1][1]) \
				or (valid_nearby_tickets[j][i] > value[0][1] and valid_nearby_tickets[j][i] < value[1][0]):
					rule_element_correspondance[key].remove(i)

#print(rule_element_correspondance)

# now we have removed all element numbers that don't work for a rule, do a one-to-one mapping
# so if a key has a value of list length one, that list value must correspond to the key
# therefore remove this value from all the other keys
# keep repeating this until all keys bave value list length of one 

# dictionary to hold final mappings
rule_element_correspondance_final = {}

# iterate 100 times - arbitrarily large to ensure mapping has finished
n = 100
for iteration in range(n):
	
	# iterate over all rule names
	for key, value in rule_element_correspondance.items():

		# if value list associated with key is one 
		# and we haven't already considered this value list (by putting it in final dict)
		# then add this key, value pair to final dict
		if len(value) == 1 and key not in rule_element_correspondance_final.keys():
			value_to_remove = value[0]
			rule_element_correspondance_final[key] = value_to_remove

			# remove this value from all other keys in rule_element_correspondance
			for key, value in rule_element_correspondance.items():		
				if value != None and value_to_remove in value:
					value = value.remove(value_to_remove)


print('Mapping each rule to ticket element =', rule_element_correspondance_final)

# hence find which elements in my ticket corresponds to keys beginning with 'departure' and multiply them
departure_element_numbers = []
for key, value in rule_element_correspondance_final.items():
	if 'departure' in key:
		departure_element_numbers.append(rule_element_correspondance_final[key])

# so now have the element numbers in my ticket we shall multiply
multiplication_result = 1
for departure_element_number in departure_element_numbers:
	multiplication_result *= my_ticket[departure_element_number]

print('PART 2 DEPARTURE VALUES MULTIPLIED =', multiplication_result)



# lastpositions = {int(n): i+1 for i, n in enumerate(data.split(','))}